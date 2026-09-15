# Native engineering guide

[Curriculum](CURRICULUM.md) chooses active depth; [PRD](project/PRD.md) and [contracts](project/CONTRACTS.md) define correctness. Later engineering is not a hidden first-call prerequisite.

## Depth and tool fit

A learning build is one runnable slice with visible data flow, focused checks and a learner explanation/change. An engineered local release adds reusable boundaries where needed, evaluation, a minimal interface and reproducibility. An operational system requires actual deployment, access-control, recovery/load/cost/rollback evidence for its environment. A static PASS or polished demo proves none of those automatically.

Use native primitives before abstractions: existing Python/uv/Git and provider SDK; Pydantic at structured intake; lexical/vector retrieval before persistent indexes; direct SQL before tools; explicit state before a conditional graph. No compulsory full-stack installation. Architectural no-adoption judgment is not hands-on framework competence.

## Exact syntax and source grounding

Inspect actual versions/metadata and current primary documentation for changing APIs. [Provider reference](PROVIDER_REFERENCE.md) is documented syntax, not an observed live call. [DR-001](DECISIONS.md) is unverified and cannot support a Groq-embedding dependency. Generation and embedding providers can differ.

The SDK runs locally, inference remotely; wire JSON and parsed objects are different. Message roles organize context but do not enforce permissions. Preserve exact fields/indices and choose context by relevance, provenance, trust, budget and conflicts.

## Checks now, test engineering later

A runtime validator rejects bad input. A deterministic test checks that the validator behaves correctly. A model evaluation measures AI behavior against expected outcomes. Learner assessment measures the person's understanding. None substitutes for another.

Add a few pytest functions when a deterministic behavior first warrants checking, usually J1. Use local malformed payloads and fake tools; no paid calls are needed for parser, scope or state tests. Elaborate fixtures, coverage quotas and CI wait for named triggers. Maintainer repository checks do not make learner CI a J0 requirement.

Start evaluations small, preserve expected cases and configuration, and grow coverage with responsibilities. Compare meaningful non-AI baselines. Freeze unfamiliar/held-out cases before use; disclose contamination and sample-size limits. Count omissions as well as precision. Keep language-specific results and repeated-run variability visible. Bound time/calls/cost; unknown is not zero.

## First relevant boundary

Never print, request in chat or commit secret values. Local ignore rules do not remove tracked/history credentials. Provider use, external traces, deployment and business actions require their own task/data/spending authorization. Public repository access does not authorize publishing private learner transcripts or raw tickets. Use synthetic data; later real examples require permission and sanitization before transmission.

User text, retrieved documents, model responses and tool results are untrusted data. Ordinary code owns authorization. Trusted context supplies employee identity/scope, not model-generated customer IDs or role fields. Expose narrow parameterized operations, not unrestricted SQL/shell/URLs.

## Mechanism checks

Explicitly choose required fields, nullable values, coercion/strictness and extra-field policy. Separate parsing, schema validity, quote resolution and semantic support. Unknown is null; explicit negation is false; retain source identity, uncertainty and chronology. Show source/value together and preserve reviewer corrections with reasons.

Source spans are start-inclusive/end-exclusive Unicode code-point indices into the original, unnormalized Python str. They are not UTF-8 byte offsets or grapheme positions. Arabic combining marks can take separate indices. Removing marks can shift later positions; one-for-one replacement may preserve length but change equality. Preserve source or an explicit mapping, with UTF-8 decoding and consistent line endings. [Support fixtures](../fixtures/support/CASES.md) include a diacritic-bearing round trip. A matching quote does not establish the claim's truth.

For retrieval, preserve document/version/section/chunk lineage and inspect evidence before generation. Test absent/conflicting/superseded/instruction-like content. Apply scope before protected retrieval. Compare lexical and embedding routes on the same labeled questions. Similarity is not policy authority; Arabic quality must be measured, not assumed.

Development visibility starts with response inspection and grows to query, eligible sources, ranking, context, claims, tool args/results and errors. Use safe local records first. Adopt a tracing product for a concrete multi-step diagnosis need with authorization; production monitoring follows a chosen deployment.

For tools, write and test fixed parameterized queries before model integration. Validate args, match call/result identities, bound loops and distinguish failure from absence. BR01-BR08 in [contracts](project/CONTRACTS.md) are deterministic. Exact immutable approval binds actor, scope, target, arguments and versions; recheck permission/freshness/expiry/eligibility/stock/duplicates at execution. Consume once with the controlled local effect and retain audit evidence. Rejection, mutation, substitution, missing/stale approval and replay produce no additional effects.

Local sequential correctness is not concurrent or distributed exactly-once evidence. Durable restart, transaction coordination and external reconciliation need selected Q6/Q11 work. An unknown write outcome cannot be called success or retried blindly.

## Debugging and architecture

Expected/observed evidence -> failing layer -> hypothesis -> smallest experiment -> correction -> verification/regression. Distinguish configuration/provider/schema/source/retrieval/tool/state/infrastructure. Do not fix an evidence-retrieval miss by hiding it behind a prompt or framework.

Extract functions/modules when real repetition or complexity warrants them; no speculative plugin architecture. Record expensive decisions with alternatives, evidence, consequences and review triggers. Measure before claiming improvement.

## Later depth

Persistent indexes, hybrid/reranking, durable graphs, OIDC, worker queues, classifier comparisons, deployment, backup/restore and rollback remain selected extensions. Require evidence from the implemented environment. No production, business or employment claim follows from knowing tool names.
