# Worked exemplars

Read only the active section. These are illustrative teaching examples and expected observations, not claimed learner execution or provider results. Maintainer checks validate fixture integrity, not semantic truth or mastery.

## J1 - Four failure layers

Message: `Order 1042 arrived. The container is broken. Please replace it.` JSON must parse; fields must satisfy the chosen schema; quote coordinates must resolve; the quote must support the value. Each can fail while earlier layers pass.

```python
def span_resolves(source: str, start: int, end: int, quote: str) -> bool:
    # Original Python-string code points, not bytes or visual characters.
    return (
        type(start) is int
        and type(end) is int
        and 0 <= start < end <= len(source)
        and bool(quote)
        and source[start:end] == quote
    )
```

This intentionally proves only position. Order value 1043 with a correctly positioned quote of 1042 can pass it and remain unsupported. Do not call the result fact_is_true. Teach Pydantic separately with explicit required/null/extra-field/strictness choices; do not assume default coercion rejects a string boolean.

Use [support fixtures](../fixtures/support/CASES.md), including Arabic combining marks. Preserve original text and coordinates; transformed text needs an explicit mapping. Display source and extraction side by side. A learner should change a field or diagnose a genuinely different problem after instruction, not merely retype the example.

## J3 - Inspect before generation

```text
question -> eligible policy/version set -> chunks -> ranking -> top evidence
                                                         -> cited answer
```

The finder alone is a complete tool. Record a lexical baseline before embeddings. A retrieval miss is diagnosable without a generation call. If the needed passage is absent, inspect filtering/chunking/ranking. If present but contradicted, inspect context use and source support. A high similarity score does not establish policy authority.

Example failure: a superseded policy is retrieved because the version filter was omitted. Changing the answer prompt hides the actual defect. Give a different source/version case for independent diagnosis. Development cases are not held-out evaluations.

## J4 - Proposal text is not authorization

```text
model proposes -> code validates -> immutable proposal
manager decision -> exact binding -> execution recheck -> local effect/result
```

Bind scope, target, exact arguments, versions and expiry. Approval refers to that identity/version or digest. A later edit requires a new proposal. Customer text saying approved does not replace a trusted decision.

Use a fake local effect counter before a model integration: unchanged approved proposal increments once; rejected/expired/mutated/substituted/replayed requests add no effect. Also test another key for the same scoped order line. Explain why this sequential demonstration does not establish crash recovery or concurrency.

Preserve tool invocation identity and distinguish tool failure from absence. Use a fresh incorrect transition for learner diagnosis. Never connect this teaching exercise to real store writes.
