# Decision records

Costly or cross-component choices get a short record in the format [ENGINEERING_GUIDE.md](ENGINEERING_GUIDE.md)
already specifies: context, decision, alternatives, evidence, consequences, review trigger.
A record states what was decided and on what evidence; it is not a claim that the decision
was executed or measured.

## DR-001 — J3 embedding route

**Status:** provisional default, decided 2026-09-09. Reopen at J3 entry.

### Context

[CURRICULUM.md](CURRICULUM.md) J3 says *"Use one embedding route and NumPy similarity"*
and never names it. [PROVIDER_REFERENCE.md](PROVIDER_REFERENCE.md) covers chat completions
and JSON Object Mode only. Meanwhile E09 in [skills.json](../progress/skills.json) requires
Arabic and English results reported separately, and J3 asks for cross-language retrieval
evaluation if used.

So the first genuinely cross-component choice on the route had no owner: which embedding
model, from which provider, at what setup cost, with what Arabic behavior.

### Decision

Default to **Groq's embeddings endpoint** for the first working J3 slice, English only.
Treat Arabic retrieval as an explicitly open risk to be decided with evidence, not now.

### Alternatives considered

| Option | Cost | Arabic | Why not the default |
|---|---|---|---|
| Groq embeddings endpoint | No new key, no new SDK, no download | Weak — see below | **Chosen** for the first slice |
| Local sentence-transformer (multilingual) | New dependency, model download, no API cost | Strong | Real setup cost before the mechanism is understood; violates one-new-thing-at-a-time |
| Second hosted provider for embeddings | New key, new billing, new SDK | Varies | Two provider boundaries while learning the first one |

### Evidence

Checked 2026-09-09, no provider call made:

- Groq publishes an embeddings endpoint serving `nomic-embed-text-v1_5`, float or base64
  output, on the same client as the chat endpoints.
- `nomic-embed-text-v1.5` is not the multilingual member of that family. The multilingual
  model is `nomic-embed-text-v2-moe` (~100 languages, MoE), and it is **not** what the
  Groq endpoint serves. Published Arabic–English cross-lingual retrieval comparisons place
  v1.5 below purpose-built multilingual alternatives.

Sources: [Groq supported models](https://console.groq.com/docs/models),
[Groq embeddings API](https://apis.io/apis/groq/groq-embeddings-api/),
[nomic-embed-text-v2-moe](https://simonwillison.net/2025/Feb/12/nomic-embed-text-v2/),
[Arabic–English RAG embedding comparison](https://hosn.om/blog/bilingual-rag-embeddings-arabic-english.html).

Availability, account access and actual retrieval quality on this corpus are unverified.
This is a documentation check, exactly as scoped in [PROVIDER_REFERENCE.md](PROVIDER_REFERENCE.md).

### Consequences

The English J3 slice costs nothing new: no key, no SDK, no download, one endpoint on a
client the learner already built. That preserves the route's own rule about introducing
one mechanism at a time.

**Arabic retrieval on this route is expected to underperform, and that is a tooling
property, not a learner failure.** This is the consequence that matters. Without this
record, a learner whose Arabic Recall@k comes back poor has no way to tell a bad chunking
decision from a bad embedding model, and the available conclusion — *"I don't understand
embeddings"* — is both wrong and the likeliest to end the project.

State this before the Arabic evaluation runs, not after it disappoints.

### Review trigger

Reopen when **either** condition holds:

1. Labeled Arabic questions exist and measured Arabic Recall@k is materially below the
   English figure on the same content. `note_001` / `note_007` in
   [fixtures](../fixtures/medical/CASES.md) are the same pattern for extraction and show
   how the comparison is built: same facts, two languages, scored separately.
2. A target vacancy requires demonstrated Arabic retrieval quality.

On either trigger, evaluate a multilingual model against this baseline on the same labeled
set and keep whichever is justified. Do not switch models on intuition; the point of the
baseline is to make the switch measurable.
