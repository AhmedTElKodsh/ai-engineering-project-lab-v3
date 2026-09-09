# Native engineering guide

[Curriculum](CURRICULUM.md) chooses the active increment; [teaching](TEACHING_GUIDE.md) controls delivery. This native adaptation replaces V3.2 source 04 as current authority. Later practices are references, not hidden J0 gates.

## Depth and tool fit

**Learning build:** a small working AI slice, expected-vs-observed cases, visible data flow, a controlled failure, and learner explanation/modification. **Engineered AI:** add reusable boundaries, stronger evaluation, focused tests, and failure policies where useful. **Production AI:** require actual deployment, authorization, monitoring, recovery, load/cost and rollback evidence for the chosen environment. A demo or static PASS does not establish production readiness.

Expose native primitives before frameworks and observe/debug them. Compare an abstraction only to answer a demonstrated design or learning need. A justified no-adoption decision qualifies when it traces the native mechanism, identifies responsibilities the framework would move, names its costs, and gives a concrete reconsideration trigger. J0 uses Python/uv/Git and one provider SDK; J1–J2 add typed validation; J3 compares visible retrieval with a simple baseline before any conditional LangChain slice; J4 permits direct SQL/native read tools after J2 and adds retrieved policy before completion, with LangGraph conditional on a state/checkpoint need; J5 adds one small API/interface and focused checks. Do not install all tools on resume. Full tracing products, vector databases, OCR, Docker, CI/CD, LLMOps, MCP, GraphRAG, and fine-tuning need an observed limitation or later selected module.

## Exact syntax and source grounding

Durable mechanisms can use these guides. For changing SDK/model/API/CLI behavior, inspect actual project declarations and versions, and verify current primary documentation before claiming exact current syntax. [Provider reference](PROVIDER_REFERENCE.md) is a dated inherited baseline with unknown local versions. If current verification is unavailable, explicitly label the code/syntax unverified and explain the durable mechanism without inventing details. Preserve required indices, keys, attributes, arguments, import names and configuration order in any adaptation.

The SDK executes in the local process, remote inference occurs across the network, and a parsed response object is distinct from JSON on the wire. Structured message roles organize context but do not enforce authorization. Choose context by relevance, provenance, trust, size and conflict; more context is not automatically better.

## First relevant boundary

Keep secret values out of source, logs, screenshots, traces and chat. A local `.env` must be loaded into process environment before client creation when that configuration workflow is used. Ignore rules do not remove already tracked/history secrets. Inspect metadata and redacted evidence without opening secret values. Provider calls, hosted traces, outbound messages, and consequential external actions require explicit scope; ordinary lesson help is not permission to execute them.

Treat user, retrieved, model and tool content as data. Validate before use; permissions and action approval belong in deterministic code. Use synthetic medical notes and retail orders. Medical extraction preserves explicit facts, missingness, negation, chronology, uncertainty and source spans for human review; it never infers diagnosis/treatment/dose or claims clinical validation. Retail tools scope rows from trusted caller identity, not model arguments. Actions are simulated unless separately authorized.

## Mechanism checks

JSON syntax, schema validity, and source truth are distinct. Validate output and invariants; verify evidence spans against input. Null represents absent facts. Measure unsupported facts and missing/negated handling, with counts and denominator; empty predictions cannot win by precision alone.

At J0's first JSON experiment use explicit JSON Object Mode and local validation, with the separately dated capability check in [provider reference](PROVIDER_REFERENCE.md). Set an explicit request time budget appropriate to the exercise and distinguish timeout from provider rejection, parse failure and model-quality failure; do not add retries before their safety and cost are understood. At J1 decide field types, required/null behavior and extra-field policy explicitly; JSON mode cannot enforce these rules or source fidelity. Distinguish missing/truncated content, JSON parse failure, schema failure and unsupported source claims. A stricter provider schema mode is an optional capability-dependent comparison, not a reason to skip local invariants.

Start small executable boundary checks alongside the mechanism: J0/J1 malformed output, schema types and source-span fixtures; J3 citation/provenance fixtures; J4 query scope and state transitions. Hand-written payloads and fake tools keep these checks local and deterministic. J5 consolidates them and adds API boundary cases; no early test framework or coverage quota is required.

For retrieval, preserve document/version/section/chunk provenance, inspect chunks before generation, and evaluate retrieval independently from answer support/citations/abstention. Start with a lexical or exact-term non-AI baseline on the same labeled cases before claiming an embedding improvement. Include missing, conflicting, expired and instruction-like evidence. Permission scope must constrain retrieval whenever protected documents exist. In J3 use one embedding route and visible local similarity; persistent or hybrid indexes follow measured needs.

For J4, write parameterized SELECT/WHERE/JOIN/aggregation against synthetic data before model integration. Use fixed read-only tools first. Validate typed arguments, scope data, return provider-linked tool results using current documentation, bound steps and time, and expose failures accurately. Proposed -> awaiting approval -> approved/rejected -> simulated result is application state; approval text is not approval. Check wrong-customer, missing-order, malformed argument, unapproved action, duplicate request and tool failure paths. Never blindly retry a consequential action.

Approval attaches to an immutable proposal record: proposal ID and version or digest, trusted actor identity, action target and exact normalized parameters. Store that binding outside model-controlled text. Before a simulated effect, compare the current proposal and trusted actor with the approved record, check approval is current and unused, then consume it with the effect under one controlled execution boundary. Changing parameters/target/actor or using a stale version requires new approval. Local tests must show the original approved proposal executes once and mutation, substitution, rejection, missing approval and replay produce zero effects. Preserve the consumed record for audit. This local state exercise does not establish concurrency safety or distributed exactly-once behavior; those require later operational evidence.

Evaluate AI behavior separately from deterministic software. Use the simplest credible non-AI baseline: fixed rules for extraction/classification, lexical retrieval for RAG, and expected SQL rows or explicit state tables for tools. Freeze at least one small unseen case early in J1/J2 before tuning, then expand the blinded set at J5. Change one variable, record configuration/date/sample size, keep development and held-out cases separate, and disclose contamination. Report per-language Arabic/English/code-switch results when tested. Repeat a small subset to expose variability. Define per-request and batch budgets for time, provider calls and cost before evaluation; stop or label incomplete rather than silently exceeding them. Unknown latency/token/cost is unknown, never zero. J0 uses 5–10 purposeful cases; J5's 20–30 cases/product is a scope/cost heuristic, not statistical sufficiency.

## Debugging and architecture

Use exact expected/observed evidence -> failing layer -> hypothesis -> smallest experiment -> result -> correction -> regression evidence. Distinguish interpreter/import/configuration, HTTP/provider, response/schema, context/model, retrieval, SQL/tool scope, state, and infrastructure failures. Do not infer an authentication failure from a client initialization error. Do not run learner code merely to validate this curriculum.

Choose the simplest architecture meeting measured needs. A costly or cross-component choice warrants a small decision record: context, decision, alternatives, evidence, consequences, review trigger. Explain file roles, trust boundaries and one representative data path. Tests should cover meaningful boundary behavior and defects; avoid broad early ceremony or tests that merely repeat code.

## Later depth

Q5 compares advanced/hybrid/reranked retrieval against a baseline and scopes protected evidence. Q6 adds durable replay/recovery without duplicate effects. Q7 permits generated SQL only with read-only credentials, allowlists and row/runtime bounds. Q8 teaches MCP host/client/server contracts with one mock/read-only integration and explicit trust boundaries. Q9 requires relational questions and a conventional RAG baseline before graph adoption. Q10 starts from task-appropriate non-training baselines, licensed/provenanced data, a held-out split, resource budget and matching train/inference formatting; use one tracker and measure adaptation/quantization results. Q11 deepens auth, tests, CI/CD, traces, monitoring, cache freshness, cost, deployment and recovery on a chosen target. Q12 defends independent delivery. Do not infer clinical, operational or job claims from familiarity with these names.

## Recurring command meanings

Run commands in the verified learner app directory only when they are appropriate to the current task. These are reference commands, not commands executed by workspace validation.

| Command | State or evidence affected |
|---|---|
| `uv add <package>` | Declares a needed dependency and updates/synchronizes project state |
| `uv sync` | Synchronizes declared dependencies; does not declare missing packages |
| `uv run <command>` | Runs using the project's environment |
| `uv run python -m app.main` | Inherited app launch example, applicable only after that module is confirmed |
| `git diff` | Inspects tracked changes before a meaningful commit |
| `git check-ignore .env` | Checks ignore matching, not history removal |

Add new recurring commands when first needed, including what they change or prove. Do not turn this reference into a setup checklist.
