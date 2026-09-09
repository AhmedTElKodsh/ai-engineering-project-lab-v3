# Project Quest Map: Medical and Retail

**Native adaptation:** 2026-09-08, from frozen V3.2 source 01. This document owns the active route; the archive is reference history.

## Mission and three distinct outcomes

Build useful AI applications while learning each mechanism at the moment a real problem needs it. Target junior applied AI/LLM application roles in Egypt and remote roles that accept Egypt-based applicants. This is not a general ML research curriculum.

1. **Initial application checkpoint:** J0-J5 evidence plus a match to a specific vacancy. Start selective applications sooner when the role fits and evidence is already sufficient.
2. **Broader curriculum completion:** additional selected Q modules and independent transfer.
3. **Production readiness:** deployment, operations and risk evidence for a specific system and environment. A portfolio demo does not establish this.

No fixed number of projects, course hours or tools guarantees eligibility. Degree, experience, language, location and employment restrictions remain separate checks. The inherited 5-hour study day is provisional. After two observed sessions estimate the next stage from actual pace, record setup vs learning time, and revise; do not promise a job in a set number of weeks.

## Two products with different jobs

| Product | User and problem | Initial input -> output | Distinct engineering work |
|---|---|---|---|
| Medical Document Review Assistant | A document reviewer spends time locating explicitly stated facts and checking omissions | Synthetic note -> typed facts, source spans, missing/uncertain fields and review flags | Extraction, schema validation, negation, chronology, provenance and human correction |
| Retail Support and Order Assistant | A support worker must find policy and order facts before responding | Synthetic request + policies + orders -> cited draft, verified order facts, proposed bounded action | Classification, RAG, SQL, tools, state, approval and workflow evaluation |

Medical scope is document processing and human review. Do not offer diagnosis, treatment, dose recommendations or clinical triage. Never label synthetic extraction accuracy as clinical validation. An explicitly mentioned medication may be extracted as text with evidence; do not derive an unstated regimen. Public medical literature is an optional later source with provenance and licensing review. Real patient data and clinical use require a separately scoped expert/governance process.

Retail is the companion domain because the same skills transfer to customer operations, commerce and enterprise support while yielding an accessible operational workflow. This is a portfolio design recommendation, not a quantified ranking of Egyptian vacancies. Arabic/English cases make regional relevance visible; measure each language separately.

## Initial route and dependency map

J0 -> J1 -> J2 -> J3 -> J4 -> J5 is the recommended narrative, not a universal prerequisite chain. Keep the route structured: offer only a dependency-safe next branch, not an unstructured menu. Demonstrated prior ability can satisfy a prerequisite without repeating the lesson. After J2, direct parameterized SQL and a scoped read tool may begin in J4 while J3 retrieval is incomplete. The combined policy-and-order workflow still requires both branches, so J4 cannot complete before J3 readiness; J5 follows completed J4. Keep only the active mechanism and any explicit open branch visible during ordinary tutoring. Completion requires both behavior and understanding; do not create artificial ceremony around every small edit.

Use only the active increment's [assessment card](ASSESSMENT_CARDS.md) for J1–J5 observable cases, assistance and remediation. A milestone may be `ready` to advance with non-transfer gates satisfied while delayed transfer remains pending under the protocol's single readiness-event contract. `complete` still requires all gates. Readiness does not certify retained independence; use [the protocol](PROGRESS_PROTOCOL.md) for delay, prerequisite and reconciliation rules. Do not hold useful work idle solely for a review date.

| Stage | Useful increment | Mechanism introduced | Evidence before advancing |
|---|---|---|---|
| J0 | First provider call and tiny structured fact experiment | SDK boundary, messages, JSON, configuration and errors | Actual run, modified input, boundary explanation, small purposeful cases |
| J1 | Medical facts with evidence and review flags | Structured extraction, Pydantic, missingness, negation and deterministic validation | Expected-vs-observed field checks, unsupported-fact detection, learner-owned fix |
| J2 | Retail request classifier and response draft | Transfer of structured outputs to a different domain | New schema built with reduced help; ambiguous cases handled explicitly |
| J3 | Retail policy answers with citations | Embeddings, similarity, chunks, retrieval, grounded generation and abstention | Retrieval and answer failures separated; visible baseline and a small framework comparison |
| J4 | Order lookup and controlled support workflow | SQL, typed tools, tool-result messages, bounded loop, state and approval | Entry: J2 for SQL/scoped read tool; completion: J3 retrieval plus correct scope and synthetic workflow checks |
| J5 | Two explainable portfolio releases and applications | Minimal API/interface, reproducibility, focused verification and evidence presentation | Independent change/debug, held-out results, runnable demos, truthful role-specific application |

### J0 — Resume Q0 and make the first boundary visible

**Prerequisite:** current status reconciliation, not new onboarding. Existing Q0 milestone 0.3 remains pending in [current state](../progress/current.json) with Groq selected. Preserve the existing working example and run command. Do not create files on the learner's behalf during tutoring unless requested.

Retain milestone identifiers for continuity:

- 0.1 practical diagnostic and 0.2 project setup: only revisit a failing prerequisite. These carry no gates, but a genuine failure is recorded as ordinary evidence against milestone `0.1` or `0.2`; never relabel it under `0.3`.
- 0.3 provider-native call: actual terminal evidence AND explanation of local deterministic logic vs probabilistic generation.
- 0.4 inspect messages/input/response; 0.5 change one prompt/input and predict the effect.
- 0.6 inspect available usage/latency information and distinguish a request timeout from model or schema failure without creating an observability project.
- 0.7 use JSON Object Mode plus local JSON/Pydantic validation on one synthetic note with two explicitly stated fields and a missing value; verify the selected model's current capability using [provider reference](PROVIDER_REFERENCE.md). Prompt-only JSON requests do not enforce a schema. Use one local malformed/schema fixture before another provider request.
- 0.8 run 5-10 purposeful examples; record what succeeded, failed and was not checked.
- 0.9 explain/reproduce a small variation after guidance fades; revisit a different case in a later session.

**Small business story after the current call:** a reviewer needs to know which facts are actually present in a note. A fluent answer cannot be safely treated as a record. Structured output is the next useful limitation.

**Early support:** Python values, dictionaries/lists, functions, modules, exceptions, reading tracebacks, Git diff/commit and local secret configuration as needed. One controlled local/schema failure is sufficient now; do not intentionally spend tokens to manufacture an auth failure. No Docker, deployment or framework installation gate.

### J1 — Medical Document Review Assistant v1

**Prerequisite:** J0 boundary and basic JSON understood.

1. Define a tiny reviewer workflow and acceptance examples before coding. Start with plain text, one document, and a few fields.
2. Design a schema: document ID, explicitly stated facts, evidence text with location, unknown values, uncertainty/negation and review reason. Use null for absent facts; do not guess.
3. Build a direct-SDK extraction call, parse and validate the response. Distinguish syntactic JSON validity, schema validity and fidelity to the source.
4. Verify spans against the input deterministically. Add small executable schema/span checks now, using synthetic cases for absent facts, negation, uncertain language, old/current statements, malformed output and instruction-like text inside a note. Keep provider quality evaluation separate.
5. Provide a simple reviewer display with source alongside extracted values and an editable correction record. A terminal/table interface is enough initially.
6. Compare one meaningful prompt/schema change against a simple non-AI or deterministic baseline on the same development cases. Keep failures visible. Reserve one small unseen case now for diagnosis; later add the larger held-out set in J5.

**Behavior evidence:** field precision/recall or an explicit exact-match rubric, unsupported-fact count, source-span validity and correct handling of missing/negated facts. Report counts and denominator; an empty prediction set cannot win by precision alone. Define which errors require review before measuring.

**Ownership evidence:** learner explains why a schema-valid answer can still be wrong, fixes an unseen extraction failure, and changes one field without copying a completed solution. Delayed transfer is revisited in J2.

**Defer:** OCR, scanned records, embeddings, medical RAG, automatic coding decisions and full clinical systems. Add PDF parsing only after a plain-text version works; add Docling/OCR only for an observed layout/text extraction problem.

### J2 — Retail request triage v1 and cross-domain transfer

**Prerequisite:** J1 structured extraction with source checks.

The support worker receives refund, delivery and product questions. Build a new schema with request category, stated order ID, missing information, concise draft and escalation reason. Begin with a small explicit policy excerpt in context. Do not pretend the model has access to orders or a refund system.

First ask the learner to sketch the schema and adapt known validation independently; provide hints only after the attempt or an explicit help request. Transfer must change a meaningful constraint—not just names or surface wording—such as ambiguity policy, missing-order behavior, language, or escalation rules. Use cases where the request is ambiguous, mixes two intents or lacks an order ID, and reserve one unfamiliar case before the implementation is tuned. Add a small Arabic or English equivalent set after the initial mechanism works; keep Arabic, English and code-switch results separate rather than inferring language ability from translated UI labels.

**Evidence:** schema validity, category correctness on labeled examples, unsupported order/status claims, correct requests for missing information, and a brief explanation of which medical techniques transferred and which domain rules changed. A deliberate wrong classification should be investigated by layer, not fixed by adding a framework.

**Next limitation:** policies grow beyond the prompt; stale or missing policy context motivates retrieval.

### J3 — Retail policy RAG

**Prerequisite:** J2 and enough Python to inspect lists, vectors and functions. Teach vector/cosine intuition through a few support questions; no linear-algebra course is a gate.

1. Create a small versioned synthetic policy collection: returns, delivery, warranty and exceptions. Preserve document ID, section and effective date.
2. Write a visible ingestion/chunking step. Start with a simple lexical or exact-term retrieval baseline, then use one embedding route and NumPy similarity. Inspect retrieved chunks before generation and compare both routes on the same labeled questions.
3. Add cited answers and an explicit insufficient-evidence path. Unknown, conflicting and expired-policy questions belong in the evaluation set.
4. Separate retrieval failure from generation failure: was the relevant passage retrieved, did the answer use it, and does each citation support the attached claim?
5. Treat retrieved instructions as data. Include an instruction-like passage and verify it does not authorize tools or override application rules.
6. Assess abstraction literacy only after the native path is traceable. If a demonstrated need exists, rebuild one small slice with LangChain using current docs and explain which responsibilities moved. Otherwise, a changed trace plus a justified no-adoption comparison—what the framework would own, costs it adds, and the trigger to reconsider—satisfies this comparison. Keep the clearer implementation as the project baseline.

**Evidence:** labeled relevant document IDs for retrieval Recall@k, supported-answer/citation rubric, abstention outcomes, and one comparison changing only chunking or retrieval configuration. Small corpus limitations must be stated. Later Arabic questions should be evaluated against deliberately labeled evidence, including cross-language retrieval if used.

**Defer:** multiple vector databases, hybrid/reranking research, LLM judges, multimodal RAG and full hosted tracing. Add a persistent index only when persistence/filtering/scale requires it. Deterministic access scope is required immediately if any protected documents are introduced.

### J4 — Retail order tools and state

**Entry prerequisite:** J2 for a short direct SQL and scoped read-tool branch. Write SELECT, WHERE, JOIN and aggregation by hand against synthetic customers/orders/items; validate expected results before model integration. Start SQLite locally or PostgreSQL if already available. Use parameterized queries. **Completion prerequisite:** J3 retrieval readiness, because the finished response combines verified order facts with retrieved policy.

1. Implement a typed read-only `get_order` tool whose trusted caller scope determines which synthetic customer's rows are accessible. A model-supplied customer ID is not authorization.
2. Expose the provider-native tool schema. Inspect proposed arguments, execute validated code, and return the result with the matching tool-call identity using current provider docs.
3. Build a bounded loop with explicit stop conditions, maximum steps and errors for missing orders, invalid arguments and tool failure. Do not disguise an error as a successful order result.
4. Combine verified order facts with retrieved policy to draft a support response. Evaluate tool correctness separately from final response quality.
5. Add a simulated return request: proposed -> awaiting approval -> approved or rejected -> simulated result. Bind approval to an immutable proposal identity/version or digest, trusted actor, target and exact parameters. The executable layer rechecks the binding immediately before the effect and consumes approval once. Test post-approval mutation, actor/target substitution, stale version, rejection and replay locally; all rejected paths produce zero effects. Text saying “approved” is insufficient.
6. Compare the explicit state flow with LangGraph only when checkpointing, branching or recovery creates a demonstrated need. A justified no-adoption decision may qualify when the learner can trace a changed transition, identify what the framework would own, and state a concrete adoption trigger. If adopted, reconstruct only the useful slice and retain whichever implementation the learner can justify.

**Evidence:** normal lookup, wrong-customer lookup, nonexistent order, injected tool argument, rejected action, changed approval binding, repeated request and tool exception. Write focused executable checks as each SQL/tool/state boundary arrives, before model integration. Record expected result, observed result, tool trace and source evidence. No live refund, outbound message or real customer data.

**Defer:** free-form text-to-SQL agents (fixed query tools first), multi-agent delegation, MCP server design, durable distributed queues and enterprise IAM. These follow later only when useful.

### J5 — Delivery pass and initial application checkpoint

**Prerequisite:** J1 medical and J4 retail outcomes plus recorded ownership evidence. Finish one product's delivery pass, then transfer only the necessary pieces to the other.

- Extract clear functions/modules; expose one small FastAPI endpoint and a simple usable interface. Validate request/response boundaries and show understandable errors. A local demo is sufficient for this curriculum checkpoint; a specific vacancy may warrant a hosted demo or Docker practice.
- Handle provider timeouts and bounded retry only for suitable transient failures. Never blindly retry a consequential tool action. Explain HTTP request/response behavior; introduce async only when an actual concurrent I/O task needs it.
- Consolidate the deterministic checks introduced with schema/source validation in J1 and query scope/approval transitions in J4; add API request/response cases now. Keep AI behavior evaluation separate. Full coverage targets, complex fixtures, CI/CD and infrastructure are later work.
- Assemble held-out cases separated from development examples, extending the small unseen probes introduced earlier. A practical starting target is 20-30 cases per product with explicit failure categories, adjusted to cost and scope; this is a planning heuristic, not a statistical sufficiency claim. Freeze expected outcomes before running, record model/config/date and sample size, and disclose if a previously held-out case was used for tuning.
- Report observed quality, critical failures, latency and cost when available. Repeat a small subset to expose variability. Missing token/cost information is unknown, not zero. Do not invent improvements or business impact.
- Have the learner make one unfamiliar change and diagnose one unfamiliar failure with normal docs allowed and support recorded. Require the learner's own architecture/dataflow explanation and one rejected alternative. J5 ownership gates (explanation, modification, debug and transfer) require `none`/`docs`; execution may be supported. J5 readiness requires E01–E22 at least practiced; full route completion also requires E22 independently applied or stronger, including delayed transfer. Supported final work is retained as practice and reassessed on a different task.
- Observe one small usability task with a person other than the builder when practical: give only the normal README/interface, capture where they hesitate or fail, and make or defer one evidence-backed correction. This is lightweight interface evidence, not a usability study.
- Prepare the two project READMEs, demo recording or reproducible demo commands, evaluation report, limitations, dependency lock and role-specific CV bullets using [portfolio evidence](PORTFOLIO.md).
- Compare real vacancies against demonstrated skills and explicit eligibility. Start applying to suitable roles; record gaps as targeted short branches, not a reason to complete every later module first.

## Later curriculum: deepen an existing product

These are selectable modules after the initial route, with prerequisites checked by evidence. They retain the old Q identifiers for reference. They are not all required for initial applications.

| Module | Trigger and prerequisite | Project extension and completion evidence |
|---|---|---|
| Q5 advanced retrieval | J3; measured retrieval or access limitation | Compare lexical/hybrid/reranking against the same baseline; protected-source lab if applicable; optional table/image evidence with provenance |
| Q6 deeper agents | J4; need for recovery or longer workflows | Durable checkpoints, recovery and action semantics; prove replay/retry behavior without duplicate effects |
| Q7 data/SQL assistant | J4 SQL/tool correctness | Natural-language analytics over a scoped database; read-only permissions, bounded queries, expected SQL results and separate answer evaluation |
| Q8 research/MCP | J4; genuine external-tool boundary | Integrate one mock/read-only MCP service, inspect trust boundaries; compare one alternative agent SDK only if it answers a design question |
| Q9 GraphRAG | J3 and graph-shaped question evidence | Model entities/relations with provenance; compare with conventional retrieval before adopting a graph |
| Q10 open models/adaptation | J1/J3 eval literacy; data/compute fit | Local inference and task baseline first; minimal tensor/training concepts as needed; optional LoRA/QLoRA with held-out evaluation or justified no-tune decision |
| Q11 production/LLMOps | J5; a chosen deployment target | Docker, CI/CD, auth, tests, traces, monitoring, cost, rollback and load/recovery work in staged increments; prove operation in the actual target |
| Q12 independent capstone | J5 plus only the branches the problem requires | New scoped user problem, architecture defense, meaningful baseline comparison and independent delivery; production claims only with Q11-type operational evidence |

MCP, multi-agent systems, GraphRAG and fine-tuning are not automatic signs of a stronger project. A simple measurable improvement is better evidence than unused infrastructure.

## Legacy mapping and continuity

| V3.1.4.3 reference | V3.2 location |
|---|---|
| Q0 / milestones 0.1-0.9 | J0; current 0.3 preserved |
| Q1 LLM applications | J1-J2 plus J5 minimal delivery |
| Bridge A | Native tools and small state workflow in J4 |
| Q2 document AI | J1 text extraction; OCR/layout branch only when needed |
| Q3 embeddings | J3 visible local retrieval |
| Q4 RAG | J3 grounded policy assistant |
| Q5-Q12 | Later selectable catalog above |

The old Q1-Q4 milestone numbers are historical references, not extra parallel tasks. [Progress protocol](PROGRESS_PROTOCOL.md) defines evidence, [current state](../progress/current.json) tracks the active point, [engineering](ENGINEERING_GUIDE.md) supplies depth-specific standards, [portfolio](PORTFOLIO.md) owns portfolio proof, and [teaching](TEACHING_GUIDE.md) controls tutoring. Do not import maintainer reports as live lesson instructions.
