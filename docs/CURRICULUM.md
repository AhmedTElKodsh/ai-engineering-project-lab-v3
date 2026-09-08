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

## What ships when, and what waits

**Every stage ends with something you could show another person.** Not finished — recordable. A short screen capture, a README paragraph and the exact command that reproduces it. Portfolio evidence accumulates from J1 onward; [portfolio](PORTFOLIO.md) is a running file, not a final phase. A stage that produced no showable artifact is a stage that has to be reconstructed from memory later, which is the slowest possible route to an application.

**Boundary checks are the product; test engineering is deferred.** Span verification, schema invariants, query scope and approval transitions arrive with the mechanism they guard, because an extractor without a span check is not an untested extractor — it is a text generator with a confident tone. Being able to say *how you knew the output was wrong* is the most interview-relevant thing this route teaches. What is deferred is test *engineering*: framework architecture, coverage targets, fixture libraries and CI. See [the engineering guide](ENGINEERING_GUIDE.md).

**Deferred, and the observation that brings it back:**

| Deferred | Not now, because | Reopen when |
|---|---|---|
| Docker, hosting, CI/CD | A reproducible local demo satisfies the initial checkpoint | A target vacancy requires it, or a reviewer cannot run the demo |
| Test frameworks, coverage targets, fixture libraries | Checks written beside each mechanism catch the real defects at this size | The checks outgrow a single file, or one regression escapes twice |
| Tracing products, monitoring, cost dashboards, LLMOps | Nothing is deployed or serving traffic | Q11, against an actual chosen deployment target |
| Vector databases, hybrid search, rerankers, LLM judges | Visible similarity over a small corpus stays inspectable and honest | A measured retrieval limit in J3, then Q5 |
| Multi-agent systems, MCP servers, GraphRAG, fine-tuning | Each adds surface area without a measured problem | Q6–Q10, once there is a baseline to beat |
| Async and concurrency | The workload is one request at a time | An actual concurrent I/O need at J5 or later |
| OCR, PDF layout, scanned documents | Plain text exposes the extraction problem faster | An observed text-extraction failure inside J1 |

Deferral is a scheduling decision, not a claim that these are unimportant. Record the trigger when deferring, so a later "should I add this now?" has an answer other than anxiety.

**When applications start.** Applying is not gated on route completion. After J1's recordable slice the CV and profile carry one honest measured bullet. From J3 onward, apply to roles whose must-have list is already covered by demonstrated work, and record the remainder as role gaps in [portfolio](PORTFOLIO.md) rather than as a reason to finish every later module first. Eligibility — degree, experience, language, location, work authorization — stays a separate check that no amount of portfolio work removes.

## Initial route and dependency chain

J0 -> J1 -> J2 -> J3 -> J4 -> J5. New mechanisms follow this order; demonstrated prior ability can satisfy a prerequisite without repeating the lesson. Keep only the active milestone visible during ordinary tutoring. Completion requires both behavior and understanding; do not create artificial ceremony around every small edit.

Use only the active increment's [assessment card](ASSESSMENT_CARDS.md) for J1–J5 observable cases, assistance and remediation. A milestone may be `ready` to advance with non-transfer gates satisfied while delayed transfer remains pending in a grounded review queue. `complete` still requires all gates. Readiness does not certify retained independence; use [the protocol](PROGRESS_PROTOCOL.md) for delay, prerequisite and reconciliation rules. Do not hold useful work idle solely for a review date.

| Stage | Useful increment | Mechanism introduced | Evidence before advancing |
|---|---|---|---|
| J0 | First provider call and tiny structured fact experiment | SDK boundary, messages, JSON, configuration and errors | Actual run, modified input, boundary explanation, small purposeful cases |
| J1 | Medical facts with evidence and review flags | Structured extraction, Pydantic, missingness, negation and deterministic validation | Expected-vs-observed field checks, unsupported-fact detection, learner-owned fix |
| J2 | Retail request classifier and response draft | Transfer of structured outputs to a different domain | New schema built with reduced help; ambiguous cases handled explicitly |
| J3 | Retail policy answers with citations | Embeddings, similarity, chunks, retrieval, grounded generation and abstention | Retrieval and answer failures separated; visible baseline and a small framework comparison |
| J4 | Order lookup and controlled support workflow | SQL, typed tools, tool-result messages, bounded loop, state and approval | Correct data scope; invalid tools/actions blocked; workflow tested on synthetic orders |
| J5 | Two explainable portfolio releases and applications | Minimal API/interface, reproducibility, focused verification and evidence presentation | Independent change/debug, held-out results, runnable demos, truthful role-specific application |

### J0 — Resume Q0 and make the first boundary visible

**The problem this stage serves:** a document reviewer needs to know which facts are actually present in a note. The model will answer fluently whether or not they are. J0 exists to make that gap visible in the learner's own terminal before J1 tries to close it.

**Prerequisite:** current status reconciliation, not new onboarding. Existing Q0 milestone 0.3 remains pending in [current state](../progress/current.json) with Groq selected. Preserve the existing working example and run command. Do not create files on the learner's behalf during tutoring unless requested.

J0 is three working blocks, not nine separate assignments. The identifiers are retained for continuity with earlier records; each block is roughly one sitting, and none of them should be presented to the learner as a numbered gate to clear.

**Block A — the call and its controls (0.3–0.5).** 0.3 provider-native call: actual terminal evidence AND explanation of local deterministic logic vs probabilistic generation. 0.4 inspect messages, input and response object. 0.5 change one prompt or input, predict the effect before running, then compare. Milestones 0.1 practical diagnostic and 0.2 project setup are inherited; revisit only a prerequisite that current evidence shows failing.

**Block B — cost and the first structured output (0.6–0.7).** 0.6 is a short look at whatever usage and latency information the response exposes, not an observability project; it exists so those numbers are familiar before they matter. 0.7 use JSON Object Mode plus local JSON/Pydantic validation on one synthetic note with two explicitly stated fields and a missing value; verify the selected model's current capability using [provider reference](PROVIDER_REFERENCE.md). Prompt-only JSON requests do not enforce a schema. Use one local malformed/schema fixture before spending another provider request.

**Block C — a small honest case set (0.8–0.9).** 0.8 run 5–10 purposeful examples and record what succeeded, what failed and what was never checked. 0.9 explain and reproduce a small variation after guidance fades, then revisit a different case in a later session.

**Exit signal:** the learner can point at their own output and say which parts they can verify against the note and which they cannot check from the output alone — naming an ungrounded claim if one appeared, and otherwise naming why a correct-looking answer still is not evidence. That observation is the entire reason J1 exists: a fluent answer cannot be treated as a record, and structured output with source spans is the next useful limitation.

**Early support:** Python values, dictionaries/lists, functions, modules, exceptions, reading tracebacks, Git diff/commit and local secret configuration as needed. One controlled local/schema failure is sufficient now; do not intentionally spend tokens to manufacture an auth failure. No Docker, deployment or framework installation gate.

### J1 — Medical Document Review Assistant v1

**Prerequisite:** J0 boundary and basic JSON understood.

1. Define a tiny reviewer workflow and acceptance examples before coding. Start with plain text, one document, and a few fields.
2. Design a schema: document ID, explicitly stated facts, evidence text with location, unknown values, uncertainty/negation and review reason. Use null for absent facts; do not guess.
3. Build a direct-SDK extraction call, parse and validate the response. Distinguish syntactic JSON validity, schema validity and fidelity to the source.
4. Verify spans against the input deterministically. Add small executable schema/span checks now — these are the product, not test ceremony. Start with three synthetic cases: an absent fact, a negated fact, and a value whose span does not resolve to the note. Add uncertain language, old-versus-current statements, malformed output and instruction-like text inside a note as real notes break them rather than as an upfront checklist; all six are required before J1 is complete. Keep provider quality evaluation separate.
5. Provide a reviewer display with source alongside extracted values and an editable correction record. A terminal or table interface is enough to start, but put the note text and the extracted value where they can be read together: a negated fact or an ungrounded span is nearly invisible in raw JSON and obvious side by side. This is a debugging instrument first and a demo second.
6. Compare one meaningful prompt/schema change against the same development cases. Keep failures visible. Later add a small held-out set in J5.
7. Capture the slice before moving on: one short recording or reproducible command sequence showing a successful extraction, a correctly-flagged missing fact, and one honest failure. Write the README paragraph and the first measured CV bullet now, while the numbers are in front of you. This is the first artifact that can go in front of another person; [portfolio](PORTFOLIO.md) owns the format.

**Behavior evidence:** field precision/recall or an explicit exact-match rubric, unsupported-fact count, source-span validity and correct handling of missing/negated facts. Report counts and denominator; an empty prediction set cannot win by precision alone. Define which errors require review before measuring.

**Ownership evidence:** learner explains why a schema-valid answer can still be wrong, fixes an unseen extraction failure, and changes one field without copying a completed solution. Delayed transfer is revisited in J2.

**Exit signal:** a stranger could watch the recording and understand what the tool does and where it fails.

**Defer:** OCR, scanned records, embeddings, medical RAG, automatic coding decisions and full clinical systems. Add PDF parsing only after a plain-text version works; add Docling/OCR only for an observed layout/text extraction problem.

### J2 — Retail request triage v1 and cross-domain transfer

**Prerequisite:** J1 structured extraction with source checks.

The support worker receives refund, delivery and product questions. Build a new schema with request category, stated order ID, missing information, concise draft and escalation reason. Begin with a small explicit policy excerpt in context. Do not pretend the model has access to orders or a refund system.

First ask the learner to sketch the schema and adapt known validation independently; provide hints only after the attempt or an explicit help request. Use cases where the request is ambiguous, mixes two intents or lacks an order ID. Add a small Arabic or English equivalent set after the initial mechanism works; keep Arabic, English and code-switch results separate rather than inferring language ability from translated UI labels.

**Evidence:** schema validity, category correctness on labeled examples, unsupported order/status claims, correct requests for missing information, and a brief explanation of which medical techniques transferred and which domain rules changed. A deliberate wrong classification should be investigated by layer, not fixed by adding a framework.

**Next limitation:** policies grow beyond the prompt; stale or missing policy context motivates retrieval.

### J3 — Retail policy RAG

**Prerequisite:** J2 and enough Python to inspect lists, vectors and functions. Teach vector/cosine intuition through a few support questions; no linear-algebra course is a gate.

1. Create a small versioned synthetic policy collection: returns, delivery, warranty and exceptions. Preserve document ID, section and effective date.
2. Write a visible ingestion/chunking step. Use one embedding route and NumPy similarity. Inspect retrieved chunks before generation.
3. Add cited answers and an explicit insufficient-evidence path. Unknown, conflicting and expired-policy questions belong in the evaluation set.
4. Separate retrieval failure from generation failure: was the relevant passage retrieved, did the answer use it, and does each citation support the attached claim?
5. Treat retrieved instructions as data. Include an instruction-like passage and verify it does not authorize tools or override application rules.
6. Wire one slice — ingestion or retrieval, not the whole pipeline — through LangChain using current docs, time-boxed, and name exactly which responsibilities moved into the library. Do not rewrite working code to match it. The visible implementation stays the project baseline and the one explained in an interview; the point of the exercise is to discuss the abstraction honestly and to have used it, not to maintain two pipelines.

**Evidence:** labeled relevant document IDs for retrieval Recall@k, supported-answer/citation rubric, abstention outcomes, and one comparison changing only chunking or retrieval configuration. Small corpus limitations must be stated. Later Arabic questions should be evaluated against deliberately labeled evidence, including cross-language retrieval if used.

**Capture before moving on:** a short recording of a cited answer, an abstention on a question the corpus cannot support, and one retrieval miss you diagnosed. Retrieval that visibly refuses to answer is more persuasive to a reviewer than one that always answers.

**Defer:** multiple vector databases, hybrid/reranking research, LLM judges, multimodal RAG and full hosted tracing. Add a persistent index only when persistence/filtering/scale requires it. Deterministic access scope is required immediately if any protected documents are introduced.

### J4 — Retail order tools and state

**Prerequisite:** J3 plus a short direct SQL lab. Write SELECT, WHERE, JOIN and aggregation by hand against synthetic customers/orders/items; validate expected results before model integration. Start SQLite locally or PostgreSQL if already available. Use parameterized queries.

1. Implement a typed read-only `get_order` tool whose trusted caller scope determines which synthetic customer's rows are accessible. A model-supplied customer ID is not authorization.
2. Expose the provider-native tool schema. Inspect proposed arguments, execute validated code, and return the result with the matching tool-call identity using current provider docs.
3. Build a bounded loop with explicit stop conditions, maximum steps and errors for missing orders, invalid arguments and tool failure. Do not disguise an error as a successful order result.
4. Combine verified order facts with retrieved policy to draft a support response. Evaluate tool correctness separately from final response quality.
5. Add a simulated return request: proposed -> awaiting approval -> approved or rejected -> simulated result. Bind approval to an immutable proposal identity/version or digest, trusted actor, target and exact parameters. The executable layer rechecks the binding immediately before the effect and consumes approval once. Test post-approval mutation, actor/target substitution, stale version, rejection and replay locally; all rejected paths produce zero effects. Text saying “approved” is insufficient.
6. Express the same state machine in LangGraph only once a checkpoint or persistence need is actually visible, and keep it to the transitions. Explain what the framework holds and what the application still owns. The approval binding in step 5 is the harder and more valuable piece of engineering here; do not trade a working one for a graph diagram.

**Evidence:** normal lookup, wrong-customer lookup, nonexistent order, injected tool argument, rejected action, changed approval binding, repeated request and tool exception. Write focused executable checks as each SQL/tool/state boundary arrives, before model integration. Record expected result, observed result, tool trace and source evidence. No live refund, outbound message or real customer data.

**Capture before moving on:** a recording of the normal lookup, the blocked wrong-customer lookup, and a rejected approval producing zero effects. The refusals are the demo — anyone can show a happy path.

**Defer:** free-form text-to-SQL agents (fixed query tools first), multi-agent delegation, MCP server design, durable distributed queues and enterprise IAM. These follow later only when useful.

### J5 — Delivery pass and initial application checkpoint

**Prerequisite:** J1 medical and J4 retail outcomes plus recorded ownership evidence. Finish one product's delivery pass, then transfer only the necessary pieces to the other. Run J5 as three separate passes rather than one large release; each pass ends somewhere the work can be paused without losing it. If the recordings and README paragraphs from J1–J4 exist, Pass 3 is assembly rather than authorship.

**Pass 1 — make it runnable by someone else.**

- Extract clear functions/modules; expose one small FastAPI endpoint and a simple usable interface. Validate request/response boundaries and show understandable errors. A local demo is sufficient for this curriculum checkpoint; a specific vacancy may warrant a hosted demo or Docker practice.
- Handle provider timeouts and bounded retry only for suitable transient failures. Never blindly retry a consequential tool action. Explain HTTP request/response behavior; introduce async only when an actual concurrent I/O task needs it.
- Consolidate the deterministic checks introduced with schema/source validation in J1 and query scope/approval transitions in J4; add API request/response cases now. Keep AI behavior evaluation separate. Full coverage targets, complex fixtures, CI/CD and infrastructure are later work.

**Pass 2 — make the numbers honest.**

- Assemble held-out cases separated from development examples. A practical starting target is 20-30 cases per product with explicit failure categories, adjusted to cost and scope; this is a planning heuristic, not a statistical sufficiency claim. Freeze expected outcomes before running, record model/config/date and sample size, and disclose if a previously held-out case was used for tuning.
- Report observed quality, critical failures, latency and cost when available. Repeat a small subset to expose variability. Missing token/cost information is unknown, not zero. Do not invent improvements or business impact.

**Pass 3 — own it, then go out.**

- Have the learner make one unfamiliar change and diagnose one unfamiliar failure with normal docs allowed and support recorded. Require the learner's own architecture/dataflow explanation and one rejected alternative. J5 ownership gates (explanation, modification, debug and transfer) require `none`/`docs`; execution may be supported. J5 readiness requires E01–E22 at least practiced; full route completion also requires E22 independently applied or stronger, including delayed transfer. Supported final work is retained as practice and reassessed on a different task.
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


Readiness advancement, its append-only maintainer decision, the grounded review queue, historical-readiness rules and final J5 completion are defined once in [the progress protocol](PROGRESS_PROTOCOL.md). That machinery is teaching administration, not learner competence, and it is not part of the lesson the learner sees.
