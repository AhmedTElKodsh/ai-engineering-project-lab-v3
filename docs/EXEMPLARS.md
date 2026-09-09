# Worked exemplars

One exemplar per stage. **Read only the active stage's section**; the others are
noise until you reach them, and the same load-only-what-you-need rule that governs
[the route](CURRICULUM.md) and [assessment cards](ASSESSMENT_CARDS.md) applies here.

These are teaching artifacts, not the learner's application. Each one was executed and
the output shown is that run's actual output. They deliberately stop short of the
project: each isolates the one mechanism its stage introduces and omits everything
else, so it can be read in a sitting and cannot be pasted in as a finished feature.

A worked example is support, never ownership. Reading these satisfies no gate. See
[the teaching guide](TEACHING_GUIDE.md) on fading assistance and
[the protocol](PROGRESS_PROTOCOL.md) on what evidence a worked example can and cannot support.

## J1 — three failure layers, kept apart

The mechanism: JSON validity, schema validity and source truth are three different
questions, and a payload can pass the first two while failing the third. That third
failure is the entire reason the medical product exists.

```python
"""
Role:
This module owns the local half of medical extraction: the shape a fact must have,
and the deterministic check that a claimed span really occurs where it says it does.
It owns no provider call. That separation is the point of the exemplar.

Connections:
note text (str) -> [provider extraction, elsewhere] -> raw JSON -> parse -> schema
                -> span verification against the ORIGINAL note -> review flags
"""

import json
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class Fact(BaseModel):
    # extra="forbid" is a decision, not a default: a field the model invented should
    # fail loudly here rather than travel silently into the review interface.
    model_config = ConfigDict(extra="forbid")

    field: str
    value: str | float | None = Field(
        description="None means the note does not state it. Never a guess, never \"\"."
    )
    # A span is a promise about the ORIGINAL note: note[start:end] == quote.
    start: int | None = None
    end: int | None = None
    quote: str | None = None


class Extraction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document_id: str
    facts: list[Fact]
    review_flags: list[str] = []


# --- three distinct failure layers, kept distinct -----------------------------

def parse(raw: str) -> dict:
    """Layer 1: is it JSON at all?"""
    return json.loads(raw)


def validate(obj: dict) -> Extraction:
    """Layer 2: is it the right shape? Says nothing about truth."""
    return Extraction.model_validate(obj)


Verdict = Literal["ok", "absent", "unsupported", "span_mismatch"]


def verify_against_source(fact: Fact, note: str) -> Verdict:
    """Layer 3: is it actually in the note? This is the only layer that reads the source."""
    if fact.value is None:
        return "absent"                      # a stated absence needs no span
    if fact.start is None or fact.end is None or fact.quote is None:
        return "unsupported"                 # a value with no evidence is a claim, not a fact
    if note[fact.start:fact.end] != fact.quote:
        return "span_mismatch"               # the span does not resolve -- see the Arabic case
    return "ok"


# --- the four lines that carry the idea ---------------------------------------
# parse -> validate -> verify. A payload can clear the first two and fail the third,
# and that failure is the entire reason this project exists.

if __name__ == "__main__":
    note = (
        "Patient ID: SYN-1001\n"
        "Patient reports a persistent cough for eleven days. Temperature recorded at 37.9 C.\n"
        "Blood pressure was not measured at this visit.\n"
    )
    start = note.index("37.9")

    good = json.dumps({
        "document_id": "SYN-1001",
        "facts": [
            {"field": "temperature_c", "value": 37.9,
             "start": start, "end": start + 4, "quote": "37.9"},
            {"field": "blood_pressure", "value": None},
        ],
        "review_flags": ["blood_pressure not measured"],
    })

    extraction = validate(parse(good))
    for fact in extraction.facts:
        print(f"  {fact.field:16} {verify_against_source(fact, note)}")

    print("\nnow the payload that passes both earlier layers and is still wrong:")
    unsupported = json.dumps({
        "document_id": "SYN-1001",
        "facts": [{"field": "diagnosis", "value": "pneumonia",
                   "start": 0, "end": 8, "quote": "Patient "}],
        "review_flags": [],
    })
    bad = validate(parse(unsupported))          # parses, validates
    fact = bad.facts[0]
    print(f"  {fact.field:16} {verify_against_source(fact, note)}   <- span resolves!")
    print("  the span is real, the quote matches, and 'pneumonia' is nowhere in the note.")
    print("  span validity is necessary and not sufficient: the quote must also SUPPORT the value.")

    print("\nand a schema failure, for contrast:")
    try:
        validate(parse('{"document_id": "SYN-1001", "facts": [{"field": "x", "value": 1, "colour": "red"}]}'))
    except ValidationError as exc:
        print("  ValidationError:", exc.errors()[0]["type"], "->", exc.errors()[0]["loc"])
```

Actual output:

```text
  temperature_c    ok
  blood_pressure   absent

now the payload that passes both earlier layers and is still wrong:
  diagnosis        ok   <- span resolves!
  the span is real, the quote matches, and 'pneumonia' is nowhere in the note.
  span validity is necessary and not sufficient: the quote must also SUPPORT the value.

and a schema failure, for contrast:
  ValidationError: extra_forbidden -> ('facts', 0, 'colour')
```

Attention: the four lines that carry the idea are `parse`, `validate`,
`verify_against_source`, and the `Verdict` values. Everything else is scaffolding.

Note the second case carefully, because it is the one worth the reading. The span
`[0, 8]` resolves perfectly — `note[0:8]` really is `"Patient "` — and the verdict is
`ok`, and the extraction is still a fabrication. A valid span proves the quote exists,
not that the quote supports the value. Your source check needs both, and the exemplar
deliberately only does one, so the gap is visible rather than described.

### Arabic breaks this first

Source spans are offsets into a specific byte sequence. Normalising Arabic — folding
alef variants, dropping diacritics — produces a different byte sequence, so an offset
found in the normalised copy does not address the same characters in the original.
The corpus ships a note built to demonstrate exactly this, and a script that runs it:

```powershell
uv run python data/synthetic/medical/check_arabic_spans.py
```

It reports the true offset, the offset a normalised search returns, and the two-character
error between them. Measure Arabic, English and code-switch results separately; never
infer one language's behaviour from another's.

## J3 — retrieval that can be wrong while succeeding

The mechanism: retrieval failure and generation failure are different failures, and
provenance is what lets you tell which one happened. Similarity is written out by hand
here; NumPy replaces this arithmetic without changing the idea.

```python
"""
Role:
The smallest honest retrieval slice: rank chunks, then answer ONLY from what was
retrieved. Similarity is hand-written here so nothing is hidden; NumPy replaces
this arithmetic at J3 without changing the idea.

Connections:
policy docs -> chunks (id, version, section kept) -> vectors -> ranked -> answer or abstain
"""

import math
import re
from collections import Counter

# Two versions of the same policy exist on purpose. Retrieving the wrong one is a
# *successful* retrieval of the *wrong document*, and no similarity score catches it.
CHUNKS = [
    {"id": "POL-RET#returns@1.0", "status": "superseded", "effective": "2025-06-01",
     "text": "Items may be returned within 14 days of delivery for a full refund."},
    {"id": "POL-RET#returns@2.0", "status": "current", "effective": "2026-01-15",
     "text": "Items may be returned within 30 days of delivery for a full refund."},
    {"id": "POL-DEL#delivery@1.0", "status": "current", "effective": "2025-11-01",
     "text": "Standard delivery is 3-5 business days. Express delivery is next business day."},
    {"id": "POL-EXC#exceptions@1.0", "status": "current", "effective": "2026-01-15",
     "text": "Consumable items and gift cards are not returnable once opened or activated."},
]


def vector(text):
    """Bag of words. Deliberately crude -- you should be able to predict its failures."""
    return Counter(re.findall(r"[a-z]+", text.lower()))


def cosine(a, b):
    dot = sum(a[t] * b[t] for t in a.keys() & b.keys())
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def rank(question, k=2):
    q = vector(question)
    scored = [(cosine(q, vector(c["text"])), c) for c in CHUNKS]
    return sorted(scored, key=lambda pair: pair[0], reverse=True)[:k]


def answer(question, k=2, min_score=0.05):
    """Abstention is a first-class outcome, not an error path.

    min_score is a knob, not a constant. It was set by looking at scores on this
    corpus; it is exactly the kind of number you must justify and re-measure when
    the corpus or the embedding changes. Freeze your cases before you tune it.
    """
    top = rank(question, k)
    usable = [(s, c) for s, c in top if s >= min_score and c["status"] == "current"]
    if not usable:
        return None, top
    return usable[0], top


if __name__ == "__main__":
    for question in ("How many days do I have to return something?",
                     "Do you price match against other shops?"):
        print("Q:", question)
        chosen, top = answer(question)
        print("   ranked:")
        for score, chunk in top:
            print("     %.3f  %-26s %s" % (score, chunk["id"], chunk["status"]))
        if chosen is None:
            print("   -> ABSTAIN: nothing current and relevant enough. This is a correct answer.")
        else:
            score, chunk = chosen
            print("   -> answer from %s: %s" % (chunk["id"], chunk["text"]))
        print()

    print("Both returns versions scored IDENTICALLY on question one -- they differ by a")
    print("single number, and bag-of-words cannot see it. Similarity did not choose v2;")
    print("the status filter did, and only because ingestion kept the version metadata.")
    print("That filter is application logic, not retrieval. It is the whole reason")
    print("provenance has to survive chunking.")
    print()
    print("Question two scored 0.000 against everything: no shared content word, nothing")
    print("to ground an answer in, so abstaining is the correct output rather than a failure.")
```

Actual output:

```text
Q: How many days do I have to return something?
   ranked:
     0.096  POL-RET#returns@1.0        superseded
     0.096  POL-RET#returns@2.0        current
   -> answer from POL-RET#returns@2.0: Items may be returned within 30 days of delivery for a full refund.

Q: Do you price match against other shops?
   ranked:
     0.000  POL-RET#returns@1.0        superseded
     0.000  POL-RET#returns@2.0        current
   -> ABSTAIN: nothing current and relevant enough. This is a correct answer.
```

Attention: the two returns chunks score **identically**. They differ by one number, and
the bag-of-words model cannot see it. Similarity did not choose the current version —
the status filter did, and only because ingestion preserved `version` and `status`
through chunking. That filter is application logic, not retrieval.

`min_score` is a knob, not a constant. It was set by looking at scores on this corpus.
Freeze your evaluation cases before you tune it, or you will tune against the answer.

## J4 — approval bound to an identity, not to text

The mechanism: an approval attaches to an immutable proposal digest, a trusted actor,
a target and exact parameters. The executor rechecks that binding at the moment of
effect and consumes it once. Text saying "approved" is not approval.

```python
"""
Role:
The approval binding. A proposal is immutable; approval attaches to its exact
identity, actor, target and parameters; the executor rechecks that binding at the
moment of effect and consumes the approval once.

Connections:
proposal (frozen) -> digest -> approval record (actor, digest) -> execute() rechecks -> effect

Text saying "approved" is not approval. The digest is what makes that true.
"""

import hashlib
import json
from dataclasses import dataclass, field, replace

EFFECTS = []          # stands in for the thing that would actually cost money


@dataclass(frozen=True)
class Proposal:
    proposal_id: str
    version: int
    actor: str                    # the trusted caller, never a model-supplied value
    target: str
    params: dict = field(default_factory=dict)

    def digest(self) -> str:
        # Canonical: sorted keys, so an equal proposal always digests equally and a
        # changed one never does. This is the identity approval binds to.
        payload = json.dumps(
            {"id": self.proposal_id, "v": self.version, "actor": self.actor,
             "target": self.target, "params": self.params},
            sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode()).hexdigest()[:16]


@dataclass
class Approval:
    digest: str
    approver: str
    consumed: bool = False


def execute(proposal: Proposal, approval: Approval | None) -> str:
    """Every rejection path returns before touching EFFECTS. That ordering is the design."""
    if approval is None:
        return "rejected: no approval"
    if approval.consumed:
        return "rejected: approval already used (replay)"
    if approval.digest != proposal.digest():
        return "rejected: proposal does not match what was approved"
    approval.consumed = True                     # consume, then act, under one boundary
    EFFECTS.append(proposal.proposal_id)
    return "executed"


if __name__ == "__main__":
    original = Proposal("P-1", 1, "agent:support-1", "order:A-1004", {"refund": 55.00})
    approval = Approval(digest=original.digest(), approver="human:reviewer-1")

    cases = [
        ("mutated parameters after approval", replace(original, params={"refund": 5500.00}), approval),
        ("substituted actor",                 replace(original, actor="agent:someone-else"), approval),
        ("substituted target",                replace(original, target="order:A-2001"), approval),
        ("stale version",                     replace(original, version=2), approval),
        ("no approval at all",                original, None),
    ]
    for label, proposal, appr in cases:
        print("  %-34s %s" % (label, execute(proposal, appr)))

    print("  %-34s %s" % ("the original, approved proposal", execute(original, approval)))
    print("  %-34s %s" % ("the same one again (replay)", execute(original, approval)))

    print("\n  effects produced:", EFFECTS)
    assert EFFECTS == ["P-1"], "exactly one effect, from the one approved proposal"
    print("  exactly one effect, from the one proposal a human actually approved.")
    print("\n  Note the ordering inside execute(): every rejection returns before EFFECTS is")
    print("  touched, and the approval is consumed before the effect, not after. Reverse")
    print("  either and a crash mid-effect leaves an approval that can be replayed.")
```

Actual output:

```text
  mutated parameters after approval  rejected: proposal does not match what was approved
  substituted actor                  rejected: proposal does not match what was approved
  substituted target                 rejected: proposal does not match what was approved
  stale version                      rejected: proposal does not match what was approved
  no approval at all                 rejected: no approval
  the original, approved proposal    executed
  the same one again (replay)        rejected: approval already used (replay)

  effects produced: ['P-1']
  exactly one effect, from the one proposal a human actually approved.
```

Attention: the ordering inside `execute`. Every rejection returns *before* `EFFECTS` is
touched, and the approval is consumed *before* the effect rather than after. Reverse
either and a crash mid-effect leaves a live approval that can be replayed.

`digest()` sorts its keys. That is not tidiness — it is what makes an equal proposal
digest equally and a changed one never digest equally, which is the property the whole
binding rests on.

This is a local, single-process demonstration. It establishes nothing about concurrency,
distributed exactly-once delivery, or crash recovery; those need the operational evidence
described in [the engineering guide](ENGINEERING_GUIDE.md).
