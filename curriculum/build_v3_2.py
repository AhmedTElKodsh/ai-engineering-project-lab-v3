"""Build a separate curriculum pack; never modify the supplied baseline."""
from pathlib import Path
import argparse
import hashlib
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument("--source", type=Path, required=True)
args = parser.parse_args()
source = args.source.resolve()
target = Path(__file__).resolve().parent / "V3.2_Medical_and_Retail_Junior_Path"
live = target / "NotebookLM_Live_Source_Pack"
maint = target / "Maintainer_Only"
live.mkdir(parents=True, exist_ok=True)
maint.mkdir(parents=True, exist_ok=True)
version = "V3.2 - Medical and Retail Junior Application Path"
header = f"**Version:** {version}  \n**Revision date:** 2026-09-07\n"
hashes = {p.relative_to(source).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(source.rglob("*")) if p.is_file()}
(maint / "SOURCE_BASELINE_HASHES.json").write_text(json.dumps({"source_directory": str(source), "sha256": hashes}, indent=2) + "\n", encoding="utf-8")

def write(name, title, body, folder=live):
    (folder / name).write_text(f"# {title}\n\n{header}\n{body.strip()}\n", encoding="utf-8")

def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new, 1)

def insert_after_header(text, addition):
    return replace_once(text, "**Revision date:** 2026-09-07\n", "**Revision date:** 2026-09-07\n\n" + addition.strip() + "\n")

for number in ("00", "03", "04", "06"):
    p, = (source / "NotebookLM_Live_Source_Pack").glob(number + "_*.md")
    text = p.read_text(encoding="utf-8")
    text = replace_once(text, "V3.1.4.3 - NotebookLM Host-Safe Code & Continuity", version)
    text = replace_once(text, "**Revision date:** 2026-09-06", "**Revision date:** 2026-09-07")
    if number == "00":
        text = insert_after_header(text, """
## Active curriculum contract

The learner targets junior applied AI/LLM application roles in Egypt and remote roles for which Egypt-based applicants are eligible. Use two evolving products: a Medical Document Review Assistant and a Retail Support and Order Assistant. `01` owns the J0-J5 initial route and the later Q5-Q12 catalog. Initial application readiness, full curriculum completion, and production readiness are separate outcomes.

Resume the recorded Q0 / milestone 0.3 inside J0. Do not restart onboarding. Teach a useful problem first, then one new mechanism at a time. Medical work begins with explicitly stated facts from synthetic text; retail provides a separate retrieval and operational workflow. Do not turn both into generic chatbots.

During J0-J5, activate only the playbook sections needed for the current deliverable. Deep testing architecture, deployment infrastructure, full LLMOps, multi-agent systems, GraphRAG, fine-tuning and enterprise operations belong to later study. Basic correctness checks, source grounding, secret handling, and deterministic authorization apply as soon as their boundary exists. Later material is a reference, not an implied graduation gate.

Two defensible portfolio projects are this curriculum's recommended initial application package, not a universal hiring minimum. Match each actual vacancy's experience, degree, location, language and technology requirements. Do not promise employment or a fixed completion time.
""")
        text = replace_once(text, "The learner studies roughly **5 active hours/day**. Carry cumulative active time across lesson estimates and mark study-day boundaries accordingly.", "The inherited planning assumption is roughly **5 active hours/day**, not a newly confirmed commitment. Use actual available time and observed pace to revise estimates; do not reopen generic onboarding. Carry cumulative active time across lesson estimates and mark study-day boundaries accordingly. Treat estimates as provisional, never as evidence of mastery.")
    elif number == "03":
        text = insert_after_header(text, """
## V3.2 continuity note

Curriculum design changed on 2026-09-07; learner execution and understanding have not been newly observed. The active route is J0-J5, with the existing Q0 / milestone 0.3 retained as the exact resume point. Domain direction: medical document review plus retail support and order assistance. All later J stages remain pending.

The provider syntax below is an inherited reference snapshot dated 2026-09-06, not a new provider/runtime verification in this revision. Installed versions and current model availability must be reconciled at lesson time. The expected learner repository below has not been inspected during this document revision; the curriculum workspace is not proof that `app/main.py` exists there.
""")
        text = replace_once(text, "- **Current path:** Core", "- **Current path:** J0-J5 initial junior application route; Q0 milestone IDs retained within J0")
        text = replace_once(text, "| Evidence dependency | Real terminal output is required before Milestone 0.3 can be marked complete |", "| Evidence dependency | Real terminal output and the learner's explanation of the deterministic/model boundary are required before Milestone 0.3 can be marked complete |")
        text = replace_once(text, "4. Move into Quest 0 message/input/output inspection and simple evaluation.", "4. Move into the remaining J0 / Quest 0 message/input/output inspection and simple evaluation; use a tiny synthetic medical note to motivate explicit facts and missing values. J1 later turns this into the Medical Document Review Assistant.")
    elif number == "04":
        text = insert_after_header(text, """
## Route activation in V3.2

J0-J5 in `01` selects the early work. The later Q labels below identify optional deepening modules, not a mandatory sequence before applying. [ALWAYS] means when that boundary exists; [ENGINEERED] does not mean every engineered technique is required immediately. Use the smallest useful check first and deepen only when failure evidence or a chosen role requires it.

Medical extraction correctness means fidelity to supplied text, not clinical correctness. Use synthetic notes, preserve missingness and negation, retain evidence spans, and send uncertainty for human review. Never infer a diagnosis or dose. Retail tools use synthetic orders and simulated actions; identity scope and action approval are enforced in code.
""")
        start = text.index("## Core Stack\n")
        end = text.index("## Tool-Sprawl Rule\n", start)
        text = text[:start] + """## Initial route tools, introduced by need

- J0: Python, uv, Git, one direct provider SDK, local environment configuration.
- J1-J2: JSON and Pydantic; ordinary text parsing and Python first.
- J3: one embedding route, NumPy similarity, a local index; a short LangChain reconstruction after the visible RAG baseline.
- J4: SQL in SQLite or PostgreSQL, typed native tools, explicit bounded state; a small LangGraph comparison when checkpoint or approval state is meaningful.
- J5: a small FastAPI boundary and one runnable interface, focused checks, recorded latency/cost and reproducible dependencies.

Do not install this entire list at onboarding. Use local trace records first. Hosted trace products require explicit data/provider decisions; they are not initial gates.

## Later or conditional tools

FAISS/ANN and Qdrant or pgvector follow a demonstrated scale, persistence or filtering need. SentenceTransformers is an alternative embedding route, not a mandatory second model. Docling/OCR follows a parser limitation. LangSmith or another trace/evaluation service follows a concrete debugging need. MCP, an alternative agent SDK, Ragas, lexical search servers, Neo4j, Hugging Face training tools, vLLM, experiment trackers, queues and production infrastructure belong to relevant later modules. Choose one tool per responsibility and compare only when a decision benefits.

""" + text[end:]
        text = replace_once(text, "Use SentenceTransformers/equivalent for open embeddings/rerankers. Use FAISS/equivalent to expose ANN/index concepts without infrastructure distractions. Choose Qdrant or pgvector as the primary vector DB based on constraints; alternatives are conceptual comparisons unless justified.", "For J3, use one embedding route and visible local similarity search. The full sequence above spans later deepening: use SentenceTransformers if local embeddings fit, FAISS if index scale warrants it, and one vector database only when persistence/filtering requirements justify it. A second embedding provider and a database are not J3 completion gates.")
        text = text.replace("Quest 5 requires a bounded practical lab:", "If later Quest 5 is selected, include a bounded permission lab when protected sources are in scope:")
        text = text.replace("Quest 5 requires at least one meaningful table/image/layout retrieval example.", "The optional multimodal branch of later Quest 5 includes at least one meaningful table/image/layout retrieval example.")
        text = replace_once(text, "Bridge A follows Quest 1 with one tiny native tool loop + minimal state graph so agent concepts are not chronologically delayed behind all RAG work.", "In J4, after the learner understands the retail data and writes the SQL directly, build one tiny native tool loop and minimal state. The legacy Bridge A capabilities are folded into J4; there is no separate mandatory bridge after J1.")
        text = replace_once(text, "Use the LangChain agent harness after the explicit loop to understand high-level runtime ownership. Open LangGraph when explicit state or custom orchestration is needed.", "After the explicit loop, use a small LangGraph comparison when approval/checkpoint state is visible in J4. A separate LangChain agent-harness comparison is optional later work; it is not an additional initial-route gate.")
    else:
        text = insert_after_header(text, """
## Early-route teaching and motivation contract

Use `01` J0-J5 to choose the current business problem and scope. A useful segment normally moves through problem -> prediction -> brief worked example -> learner completion/modification -> observed run -> explanation -> delayed transfer. This is a flexible learning pattern, not seven mandatory headings. Show one main new mechanism per segment; return to the same product so progress is visible.

Start a session from the latest output or product limitation. Let the learner choose small meaningful cases or a feature variation within the active scope. Alternate a worked example with a completion task, then fade support to an independent change. If stuck repeatedly, isolate a smaller prerequisite, model it, and retry a different example. Answer direct questions clearly; do not force guessing before instruction or reveal the answer during a designated assessment.

Use a short retrieval prompt next session and a new transfer case after a delay (for example 2-7 days, adjusted to the actual schedule). Do not stack overdue quizzes before useful work. Record support level, success and explanation separately. A later independent fix is stronger evidence than copying a working snippet now.

End a meaningful build segment by showing what the product can now do and the next useful limitation. Occasionally ask for a brief confidence/interest/overload signal and adapt the next chunk. Do not declare the curriculum motivating or effective from tutor-format checks alone; the maintainer pilot measures learner outcomes.
""")
        text = replace_once(text, "Use the learner's roughly **5 active hours/day** study budget to place cumulative work across study days.", "Treat the inherited **5 active hours/day** budget as provisional. Use the learner's actual available time and observed pace to place cumulative work across study days; do not equate elapsed hours with mastery.")
        text = replace_once(text, "> **Milestone 0.3 complete.** We now have observed evidence that this project can make an authenticated provider request and receive a model response.", "> **Milestone 0.3 execution check passed; understanding is still pending unless already observed.** We now have evidence that this project can make an authenticated provider request and receive a model response. Mark the milestone complete only after the learner also explains the deterministic local path and probabilistic model boundary.")
    (live / p.name).write_text(text, encoding="utf-8")

write("01_AI_Engineer_Project_Quest_Map.md", "Project Quest Map: Medical and Retail", r"""
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

## Initial route and dependency chain

J0 -> J1 -> J2 -> J3 -> J4 -> J5. New mechanisms follow this order; demonstrated prior ability can satisfy a prerequisite without repeating the lesson. Keep only the active milestone visible during ordinary tutoring. Completion requires both behavior and understanding; do not create artificial ceremony around every small edit.

| Stage | Useful increment | Mechanism introduced | Evidence before advancing |
|---|---|---|---|
| J0 | First provider call and tiny structured fact experiment | SDK boundary, messages, JSON, configuration and errors | Actual run, modified input, boundary explanation, small purposeful cases |
| J1 | Medical facts with evidence and review flags | Structured extraction, Pydantic, missingness, negation and deterministic validation | Expected-vs-observed field checks, unsupported-fact detection, learner-owned fix |
| J2 | Retail request classifier and response draft | Transfer of structured outputs to a different domain | New schema built with reduced help; ambiguous cases handled explicitly |
| J3 | Retail policy answers with citations | Embeddings, similarity, chunks, retrieval, grounded generation and abstention | Retrieval and answer failures separated; visible baseline and a small framework comparison |
| J4 | Order lookup and controlled support workflow | SQL, typed tools, tool-result messages, bounded loop, state and approval | Correct data scope; invalid tools/actions blocked; workflow tested on synthetic orders |
| J5 | Two explainable portfolio releases and applications | Minimal API/interface, reproducibility, focused verification and evidence presentation | Independent change/debug, held-out results, runnable demos, truthful role-specific application |

### J0 — Resume Q0 and make the first boundary visible

**Prerequisite:** current status reconciliation, not new onboarding. Existing Q0 milestone 0.3 remains pending in `03` with Groq selected. Preserve the existing working example and run command. Do not create files on the learner's behalf during tutoring unless requested.

Retain milestone identifiers for continuity:

- 0.1 practical diagnostic and 0.2 project setup: only revisit a failing prerequisite.
- 0.3 provider-native call: actual terminal evidence AND explanation of local deterministic logic vs probabilistic generation.
- 0.4 inspect messages/input/response; 0.5 change one prompt/input and predict the effect.
- 0.6 inspect available usage/latency information without creating an observability project.
- 0.7 use JSON/Pydantic on one synthetic note with two explicitly stated fields and a missing value.
- 0.8 run 5-10 purposeful examples; record what succeeded, failed and was not checked.
- 0.9 explain/reproduce a small variation after guidance fades; revisit a different case in a later session.

**Small business story after the current call:** a reviewer needs to know which facts are actually present in a note. A fluent answer cannot be safely treated as a record. Structured output is the next useful limitation.

**Early support:** Python values, dictionaries/lists, functions, modules, exceptions, reading tracebacks, Git diff/commit and local secret configuration as needed. One controlled local/schema failure is sufficient now; do not intentionally spend tokens to manufacture an auth failure. No Docker, deployment or framework installation gate.

### J1 — Medical Document Review Assistant v1

**Prerequisite:** J0 boundary and basic JSON understood.

1. Define a tiny reviewer workflow and acceptance examples before coding. Start with plain text, one document, and a few fields.
2. Design a schema: document ID, explicitly stated facts, evidence text with location, unknown values, uncertainty/negation and review reason. Use null for absent facts; do not guess.
3. Build a direct-SDK extraction call, parse and validate the response. Distinguish syntactic JSON validity, schema validity and fidelity to the source.
4. Verify spans against the input deterministically. Add synthetic cases for absent facts, negation, uncertain language, old/current statements, malformed output and instruction-like text inside a note.
5. Provide a simple reviewer display with source alongside extracted values and an editable correction record. A terminal/table interface is enough initially.
6. Compare one meaningful prompt/schema change against the same development cases. Keep failures visible. Later add a small held-out set in J5.

**Behavior evidence:** field precision/recall or an explicit exact-match rubric, unsupported-fact count, source-span validity and correct handling of missing/negated facts. Report counts and denominator; an empty prediction set cannot win by precision alone. Define which errors require review before measuring.

**Ownership evidence:** learner explains why a schema-valid answer can still be wrong, fixes an unseen extraction failure, and changes one field without copying a completed solution. Delayed transfer is revisited in J2.

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
6. Rebuild one small slice with LangChain using current docs; explain which responsibilities moved to the library. Keep the clearer implementation as the project baseline.

**Evidence:** labeled relevant document IDs for retrieval Recall@k, supported-answer/citation rubric, abstention outcomes, and one comparison changing only chunking or retrieval configuration. Small corpus limitations must be stated. Later Arabic questions should be evaluated against deliberately labeled evidence, including cross-language retrieval if used.

**Defer:** multiple vector databases, hybrid/reranking research, LLM judges, multimodal RAG and full hosted tracing. Add a persistent index only when persistence/filtering/scale requires it. Deterministic access scope is required immediately if any protected documents are introduced.

### J4 — Retail order tools and state

**Prerequisite:** J3 plus a short direct SQL lab. Write SELECT, WHERE, JOIN and aggregation by hand against synthetic customers/orders/items; validate expected results before model integration. Start SQLite locally or PostgreSQL if already available. Use parameterized queries.

1. Implement a typed read-only `get_order` tool whose trusted caller scope determines which synthetic customer's rows are accessible. A model-supplied customer ID is not authorization.
2. Expose the provider-native tool schema. Inspect proposed arguments, execute validated code, and return the result with the matching tool-call identity using current provider docs.
3. Build a bounded loop with explicit stop conditions, maximum steps and errors for missing orders, invalid arguments and tool failure. Do not disguise an error as a successful order result.
4. Combine verified order facts with retrieved policy to draft a support response. Evaluate tool correctness separately from final response quality.
5. Add a simulated return request: proposed -> awaiting approval -> approved or rejected -> simulated result. The executable layer checks approval and prevents duplicate effects; text saying “approved” is insufficient.
6. Reconstruct this small approval workflow in LangGraph when the state/checkpoint need is visible. Explain state transitions and retain whichever implementation the learner can justify.

**Evidence:** normal lookup, wrong-customer lookup, nonexistent order, injected tool argument, rejected action, repeated request and tool exception. Record expected result, observed result, tool trace and source evidence. No live refund, outbound message or real customer data.

**Defer:** free-form text-to-SQL agents (fixed query tools first), multi-agent delegation, MCP server design, durable distributed queues and enterprise IAM. These follow later only when useful.

### J5 — Delivery pass and initial application checkpoint

**Prerequisite:** J1 medical and J4 retail outcomes plus recorded ownership evidence. Finish one product's delivery pass, then transfer only the necessary pieces to the other.

- Extract clear functions/modules; expose one small FastAPI endpoint and a simple usable interface. Validate request/response boundaries and show understandable errors. A local demo is sufficient for this curriculum checkpoint; a specific vacancy may warrant a hosted demo or Docker practice.
- Handle provider timeouts and bounded retry only for suitable transient failures. Never blindly retry a consequential tool action. Explain HTTP request/response behavior; introduce async only when an actual concurrent I/O task needs it.
- Add focused deterministic checks for schema/source validation, query scope and approval transitions. Keep AI behavior evaluation separate. Full coverage targets, complex fixtures, CI/CD and infrastructure are later work.
- Assemble held-out cases separated from development examples. A practical starting target is 20-30 cases per product with explicit failure categories, adjusted to cost and scope; this is a planning heuristic, not a statistical sufficiency claim. Freeze expected outcomes before running, record model/config/date and sample size, and disclose if a previously held-out case was used for tuning.
- Report observed quality, critical failures, latency and cost when available. Repeat a small subset to expose variability. Missing token/cost information is unknown, not zero. Do not invent improvements or business impact.
- Have the learner make one unfamiliar change and diagnose one unfamiliar failure with normal docs allowed and support recorded. Give a short architecture/dataflow explanation and discuss one rejected alternative.
- Prepare the two project READMEs, demo recording or reproducible demo commands, evaluation report, limitations, dependency lock and role-specific CV bullets using `05`.
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

The old Q1-Q4 milestone numbers are historical references, not extra parallel tasks. `02` tracks evidence, `03` tracks the active point, `04` supplies depth-specific standards, `05` owns portfolio proof, and `06` controls tutoring. Do not import maintainer reports as live lesson instructions.
""")

skills = [
 ("E01", "J0", "Python/project execution", "Launch, modify and interpret a traceback in the actual project"),
 ("E02", "J0", "Configuration, secrets and Git", "Keep a key local, explain environment loading, inspect a meaningful diff"),
 ("E03", "J0", "Provider request/response boundary", "Run a native call and explain messages, response structure and local/model behavior"),
 ("E04", "J0", "JSON and typed validation", "Distinguish valid JSON, valid schema and correct content"),
 ("E05", "J1", "Grounded extraction", "Return stated facts with valid spans; flag missing/negated/uncertain content"),
 ("E06", "J1", "AI behavior evaluation", "Define expected outcomes, count failures and compare one change"),
 ("E07", "J1", "Human review interface", "Show source and editable extracted values with a correction record"),
 ("E08", "J2", "Independent domain transfer", "Build a new retail schema with reduced support"),
 ("E09", "J2-J3", "Arabic/English behavior", "Report separate language results; document untested code-switch/cross-language cases"),
 ("E10", "J3", "Embeddings and similarity", "Inspect vectors, rank passages and explain similarity limitations"),
 ("E11", "J3", "Ingestion/chunking/provenance", "Trace an answer source to a versioned document section"),
 ("E12", "J3", "Grounded RAG", "Separate retrieval/answer errors, verify citations and abstain on missing evidence"),
 ("E13", "J3", "Framework responsibility", "Compare a visible RAG slice and LangChain implementation"),
 ("E14", "J4", "SQL fundamentals", "Write parameterized filters, joins and aggregation; validate expected rows"),
 ("E15", "J4", "Native tool calling", "Validate arguments, execute a bounded tool and return linked tool results"),
 ("E16", "J4", "Authorization and action scope", "Block cross-customer access and unapproved simulated actions in code"),
 ("E17", "J4", "State and bounded workflows", "Explain transitions, stop conditions, failures and a small LangGraph comparison"),
 ("E18", "J5", "HTTP/API and interface", "Run a small usable app with validated boundaries and clear errors"),
 ("E19", "J5", "Basic failure handling", "Handle timeout/transient failure without unbounded or unsafe retries"),
 ("E20", "J5", "Focused deterministic checks", "Verify schema/span, data scope and approval transitions separately from model quality"),
 ("E21", "J5", "Held-out evaluation and tradeoffs", "Report counts, denominators, limits, latency/cost and repeat variability"),
 ("E22", "J5", "Independent delivery and explanation", "Make an unfamiliar change, debug a new failure and explain architecture"),
]
skill_rows = "\n".join(f"| {sid} | {stage} | {name} | Not started | {evidence} |" for sid, stage, name, evidence in skills)
write("02_AI_Engineering_Skill_Map.md", "AI Engineering Skill Map", """
## Evidence authority

This is the canonical skill-status ledger. Curriculum revisions do not award skills. All initial statuses below remain **Not started** because this revision adds no observed learner evidence. `03` retains lesson exposure/context, including the pending first call; it does not establish completed competence. Reconcile against the newest real evidence before updating.

Status meanings: **Not started** = no qualifying evidence recorded; **Introduced** = mechanism explained with learner engagement; **Practiced** = learner performed a supported task; **Applied independently** = learner completed a new task with normal documentation allowed and solution support recorded; **Production understanding** = additional operational decisions and failure evidence in a real scoped setting. Merely running a generated solution cannot establish independent application.

Use a small active slice (normally 5-12 skills internally); show 3-6 only if it helps the learner. Do not make the full table an onboarding quiz. Record behavior and understanding independently and retain the learner's explanation verbatim or with a link to the original response.

## Initial application route

| ID | First useful stage | Capability | Current status | Evidence target |
|---|---|---|---|---|
""" + skill_rows + """

These targets are curriculum evidence, not a universal employer checklist. Requiring an advanced status for every atom of a broad technology would delay useful applications. Reuse evidence across stages only when it actually demonstrates the new context.

## Later specialization ledger

All modules below are **Not started**. Activate only a chosen branch; add granular rows when active.

| Module | Capabilities | Evidence target |
|---|---|---|
| Q5 | Hybrid retrieval, reranking, filters, optional multimodal retrieval, calibrated judges | Improvement against a fixed baseline with failure and permission checks |
| Q6 | Durable agent state, replay, recovery | Interrupted workflow resumes correctly without duplicate effects |
| Q7 | Text-to-SQL, database permissions and query bounds | Expected query results plus authorized scope under adversarial inputs |
| Q8 | MCP, alternative SDK, justified delegation | Observable contract/trust handling and comparison explaining tool choice |
| Q9 | Graph modeling, entity linking, GraphRAG | Provenance and better results on genuinely relational questions |
| Q10 | Local models, tensors/training basics, datasets, optional PEFT | Reproducible baseline and held-out quality/resource comparison |
| Q11 | Containers, CI/CD, broad tests, deployment, LLMOps, security and operations | Actual deployment/recovery/rollback/monitoring evidence |
| Q12 | Independent scoping, design and delivery | Defended decisions and measured outcomes on a new problem |

NumPy similarity is early; deep tensor math is later when required. Fixed SQL tools are early; unrestricted generated SQL is not. Basic logs and failure handling are early; full observability infrastructure is later. Concept awareness never substitutes for an applied skill claim.

## Evidence record and review queues

Append actual records only. Template:

| Date | Skill ID | Project/stage | Task and expected behavior | Observed artifact/output | Learner explanation | Assistance level | Status decision | Follow-up |
|---|---|---|---|---|---|---|---|---|
| Pending | — | — | — | No new execution observed | Not recorded | Not assessed | No status change | Resume Q0 / 0.3 |

Maintain three small queues when evidence appears: active blockers, delayed retrieval/transfer, and role-specific gaps. Each entry needs a concrete observation, one next task and a review trigger. Avoid duplicate bookkeeping with `03`: this file owns competence; `03` owns the current action and resume context.

At a milestone review, distinguish: code works, learner can explain, learner can modify, learner can debug, and later learner can transfer. Only update the properties supported by evidence. Assistance from AI is allowed and should be documented; a polished AI-produced artifact alone is insufficient proof of ownership.
""")

write("05_Portfolio_Index.md", "Portfolio and Junior Application Evidence", r"""
## Initial package

Recommend two featured projects: the Medical Document Review Assistant and Retail Support and Order Assistant. They demonstrate different applied work and share transferable AI mechanisms. These are planned artifacts, not finished projects; neither is currently marked complete. Two is a curriculum recommendation, not a universal minimum demanded by employers.

| Project | Status | What the initial showcase should prove | Honest scope label |
|---|---|---|---|
| Medical Document Review Assistant | Planned; learner implementation not observed | Typed source-grounded extraction, missingness/negation, review workflow, measured field errors | Synthetic document-processing prototype; not clinically validated |
| Retail Support and Order Assistant | Planned; learner implementation not observed | Cited policy RAG, scoped order lookup, bounded tool/state flow and simulated approval | Synthetic support workflow; actions simulated |

## Artifact maturity is separate from visibility

- **A — Learning build:** small runnable slice, a few expected-vs-observed cases, explanation and a known failure. It can already be shown as learning work.
- **B — Demonstrable engineered project:** reproducible interface, focused boundary checks, honest held-out evaluation, independent modification/debugging and a readable README. This is the target for the initial featured portfolio.
- **C — Operational system:** deployment, access controls, monitoring, load/recovery, cost and rollback evidence for the actual environment. This is later work. Portfolio visibility does not imply C.

Do not label a repository production ready because it has Docker, many tests or a polished UI. Do not wait for maturity C to apply to suitable junior positions.

## Evidence bundle for each featured project

1. Problem, intended user, input/output example and concise scope.
2. Data origin, synthetic-generation method or license, and what was manually reviewed.
3. Small architecture/dataflow diagram: deterministic code, model call, retrieval/data boundary and human decision point.
4. Reproducible setup with dependency lock, example environment variable names only, exact local run/demo commands, and a fake-data or fixture mode when provider access is unavailable. Clearly label prerecorded or mocked outputs.
5. Evaluation report: development/held-out split, expected-outcome rubric, sample size, model/config/date, counts and denominators, critical failures, language breakdown and limits. Include actual latency/cost only if measured.
6. Focused deterministic checks plus AI evaluation kept conceptually separate. Show at least one failed case and the change it motivated.
7. Brief design decisions, one credible alternative rejected for a stated reason, known limitations and a realistic next step.
8. Learner contribution and AI assistance disclosure, plus one independent change/debugging record. Preserve references to real commits/output where available.

Useful demo: show one successful case, one missing/ambiguous case and one controlled failure with an honest explanation. A short recording or local reproduction is sufficient for this curriculum; a hosted app may be a useful vacancy-specific extension. Never require reviewers to supply patient/customer data or send their secrets to an unknown service.

## Suggested measurements, never fabricated results

| Product | Core measurements | Failure evidence that matters |
|---|---|---|
| Medical | Field precision/recall or defined exact-match rubric; unsupported-fact count; source-span validity; review flag behavior | Missing vs negated facts, chronology, uncertain source text and valid-schema hallucinations |
| Retail | Classification correctness; retrieval Recall@k; citation/answer support; abstention; tool/workflow success | Wrong-customer lookup, missing order, wrong policy version, rejected action, repeated request and tool error |

Record the evaluation dataset size and ambiguity handling. Small synthetic evaluations show bounded engineering behavior, not clinical efficacy or proven commercial savings. If claiming a reduction in review time, measure it with an explicit baseline and comparable tasks; otherwise describe it as an intended benefit.

## Vacancy matching for Egypt and remote roles

Maintain a small list of current vacancies and revisit it as projects mature. Capture: employer/title/link/date, Egypt/on-site/hybrid/remote eligibility, experience/degree, English/Arabic requirements, must-have skills, preferred tools, evidence links and unresolved gaps. “Remote” alone does not mean applicants in Egypt are eligible. Listings may expire; verify before applying.

Use the route to prepare a strong applied core, then add short branches for repeated requirements in eligible roles. If target roles consistently require Docker/Azure or deeper ML, schedule a focused extension with actual practice; do not pretend this initial route covers it. Some junior titles still demand prior experience or a degree, and a portfolio does not erase those constraints.

Application checkpoint: can the learner reproduce the demo, explain every major boundary, make an unfamiliar change, debug a controlled failure, discuss measured limitations and point to their own contribution? If yes and the vacancy's requirements fit, apply while continuing selected later study. Never claim employment readiness solely from document validation.

## Resume bullets — fill only after measurement

- Built a synthetic medical document review prototype using [actual stack] to extract [defined fields] with source evidence; evaluated on [N] held-out cases and reported [measured results and important limitations].
- Developed a retail support assistant combining cited policy retrieval with scoped SQL order tools and human-approved simulated returns; demonstrated [actual workflow cases] and measured [actual quality/latency results].

Replace brackets with observed facts before use. State prototype/synthetic scope when relevant. Do not claim clinical validation, live refunds, real revenue gains, production scale or business adoption without evidence.

## Later portfolio expansion

Expand an existing product when a measured limitation or target role calls for it. An optional third independent project can demonstrate a missing capability such as SQL analytics or open-model adaptation. Do not require four to six repositories or every Q5-Q12 framework before the first application. Prefer a small number of explainable, evaluated projects over copied demos.
""")

route = [{"id": f"J{i}", "depends_on": [f"J{i-1}"] if i else [], "required_for_initial_checkpoint": True} for i in range(6)]
route += [{"id": f"Q{i}", "depends_on": ["J3" if i in (5,9) else "J1" if i == 10 else "J5" if i in (11,12) else "J4"], "required_for_initial_checkpoint": False} for i in range(5,13)]
(maint / "ROUTE_CONTRACT.json").write_text(json.dumps({"initial_path": [f"J{i}" for i in range(6)], "resume": "Q0 / 0.3", "products": ["Medical Document Review Assistant", "Retail Support and Order Assistant"], "stages": route}, indent=2) + "\n", encoding="utf-8")
print(target)
