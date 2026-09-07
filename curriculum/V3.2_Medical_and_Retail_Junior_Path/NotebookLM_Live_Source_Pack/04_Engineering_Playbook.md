# AI Engineering Learning and Engineering Playbook

**Version:** V3.2 - Medical and Retail Junior Application Path  
**Revision date:** 2026-09-07

## Route activation in V3.2

J0-J5 in `01` selects the early work. The later Q labels below identify optional deepening modules, not a mandatory sequence before applying. [ALWAYS] means when that boundary exists; [ENGINEERED] does not mean every engineered technique is required immediately. Use the smallest useful check first and deepen only when failure evidence or a chosen role requires it.

Medical extraction correctness means fidelity to supplied text, not clinical correctness. Use synthetic notes, preserve missingness and negation, retain evidence spans, and send uncertainty for human review. Never infer a diagnosis or dose. Retail tools use synthetic orders and simulated actions; identity scope and action approval are enforced in code.

## Purpose

Define how the Lab teaches, builds, evaluates, debugs, and eventually productionizes AI systems without letting enterprise engineering crowd out the core AI knowledge ladder.

This document is both:

- a **teaching-depth controller** for early Quests,
- a **technical reference** for engineered AI,
- and a **mature engineering reference** for production work.

Do not apply every mature practice at full depth to every early learning build.

`06_Lesson_Generation_and_Learning_Cadence.md` is the canonical tutoring-runtime authority. `03_Current_Quest_Status.md` carries live state/resumption information and must not override the tutoring runtime.

---

# 0. Section Activation Labels

To reduce NotebookLM/source-retrieval overload, interpret sections by learning stage:

- **[ALWAYS]** applies from first use of the relevant boundary.
- **[LEARNING]** is appropriate for early AI-core builds.
- **[ENGINEERED]** deepens a capability once it is reusable/measurable.
- **[PRODUCTION]** becomes primary in Quest 11 or a production-stage capstone.

A production section may be referenced earlier for awareness, but should not automatically become the active lesson.

---

# 1. Core Principles [ALWAYS]

1. Start from the user/business problem, not a framework.
2. Build the smallest working AI vertical slice first.
3. Prioritize AI mechanisms before enterprise infrastructure.
4. Introduce supporting engineering just-in-time.
5. Expose important mechanisms before hiding them behind abstractions.
6. Introduce the framework close enough to the mechanism that the learner practices common tools.
7. Treat model output, retrieved content, tool output, documents, and external server responses as untrusted inputs.
8. Evaluate AI behavior with datasets/evidence, not impressions.
9. Debug by failing layer: model, context, retrieval, tool, state, data, training, application, infrastructure.
10. Prefer the simplest architecture that meets measured requirements.
11. Do not collect frameworks for their own sake.
12. Productionize systems the learner already understands.
13. Fade guidance as evidence grows.
14. Revisit important skills through retrieval, debugging, and delayed modification.
15. Verify current official documentation before version-sensitive AI implementation code.

---

# 2. Learning Depth Levels [ALWAYS]

## Level A - Learning Build

Primary question: **Does the learner understand and control the AI mechanism?**

Typical evidence:

- working vertical slice,
- small evaluation set with expected properties,
- simple data-flow sketch,
- controlled failure,
- explanation/modification by learner.

Do not require enterprise topology, full CI/CD, complete threat modeling, or broad test architecture.

## Level B - Engineered AI

Primary question: **Can the learner make the capability measurable, modular, and reliably reusable?**

Add where relevant:

- stronger evaluation,
- focused deterministic tests,
- persistence,
- typed boundaries,
- clearer failure policies,
- trace-based debugging,
- architecture decisions.

## Level C - Production AI

Primary question: **Can the learner safely operate this under real users, failures, cost, and scale constraints?**

Add:

- auth/access control,
- production security,
- complete testing strategy,
- containers,
- CI/CD,
- observability/LLMOps/MLOps as applicable,
- scaling/capacity,
- deployment/rollback,
- cost controls.

---

# 3. Teaching Compatibility and Task-Specific Pedagogy [ALWAYS]

`06_Lesson_Generation_and_Learning_Cadence.md` owns the detailed lesson runtime. This playbook only keeps the teaching behaviors required to make engineering work learnable when `04` is retrieved independently.

## 3.1 Compact Teaching-Behavior Kernel

For unfamiliar engineering work:

```text
latest learner event / current system limitation
-> identify the failing or changing layer
-> make hidden relationships visible when useful
-> explain the mechanism and responsibility boundary
-> direct attention to the few consequential lines/fields/transitions
-> show/modify the relevant artifact
-> trace or verify one representative path
-> interpret evidence
-> return meaningful ownership
-> connect to the next engineering capability
```

Use grounded pair-tutor language. Tool choices should be justified by requirements, trade-offs, lock-in, reliability, security, observability, and cost rather than prestige or popularity.

Use purposeful reinforcement across prose, sketch, code/configuration, and trace when each view adds understanding.

When exact SDK/framework/protocol syntax is version-sensitive, use a current verified snapshot in `03` or current official documentation. If neither is available, label exact syntax unverified rather than inventing it. Apply **Semantic Fidelity**: preserve method names, attributes, arguments, indexing/key semantics, and ordering exactly. NotebookLM-facing code may add whitespace inside numeric indexes (for example `items[ 0 ]`) when needed for reliable rendering; whitespace may change, the operation may not.

## 3.2 Two AI-Use Modes

### Learning / Assessment Mode

Optimize for learner understanding and independent evidence. Use explanation, prediction, modification, debugging, transfer, and delayed reproduction. A full solution may be used to unblock a new mechanism, but it must be followed by learner-owned work before strong independence is claimed.

### Professional AI-Assisted Engineering Mode

Optimize for realistic engineering productivity while preserving human ownership of requirements, architecture, review, testing/evaluation, security boundaries, and deployment decisions. Track AI-assisted engineering skill separately from underlying independent implementation skill.

## 3.3 Task-Specific Teaching Modes

Use the teaching method that matches the engineering task:

| Task | Default teaching flow |
|---|---|
| New mechanism/code | project role -> mental model/sketch -> pseudocode -> implementation -> attention-steered walkthrough -> trace -> run/verify -> learner modification |
| Debugging | expected vs observed -> failing layer -> evidence -> hypothesis -> smallest experiment -> result -> root cause -> regression lesson/test |
| Architecture | constraints -> options -> learner decision -> challenge/trade-offs -> decision/ADR -> failure/scaling implications |
| Code review | learner predicts/reads -> reviewer findings by severity -> reasoning -> learner proposes/fixes -> verification |
| Experiment/evaluation | baseline -> hypothesis -> metric/dataset -> run -> evidence -> interpretation -> decision |
| Incident/operations | symptoms -> impact -> evidence -> mitigation -> root cause -> prevention/monitoring change |

Do not force every task into a Socratic question sequence. Direct explanation is appropriate for a genuinely new mechanism; independence is tested afterward.

## 3.4 Cognitive-Load Controls

- Keep the current AI/product mechanism in the foreground.
- Teach only the supporting engineering depth needed now.
- On first exposure, show the complete reasonably sized hand-authored responsibility when practical.
- A rough warning threshold is **60-100 meaningful hand-authored LOC**, not a rigid limit. Larger modules should be mapped first and taught responsibility-by-responsibility.
- Explicitly tell the learner what can be ignored for now.
- Use generated/boilerplate/configuration artifacts proportionally; do not line-by-line explain low-value repetition.
- Separate active learner effort from passive compute/download/provisioning wait time.

## 3.5 First Exposure vs Delta

**First exposure:** explain file/artifact role, upstream/downstream connections, responsibilities, pseudocode/intent, actual content, meaningful unfamiliar lines at proportional depth, representative execution/data flow, and project connection.

**Later familiar edit:** show the exact delta, explain every changed or semantically affected line, trace the changed path, and reconnect to the existing mental model.

Explanation depth:

- **Deep** — new API/pattern, non-obvious control flow, invariant, security/reliability boundary, important abstraction.
- **Brief** — familiar imports, declarations, wiring, straightforward structural lines.
- **Grouped** — obvious boilerplate, delimiters, repeated configuration, closing syntax.

### 3.5.1 Inline Teaching Annotation Contract

For first exposure, prefer a **teaching-annotated executable version** of the code rather than a bare code dump followed by a distant lecture. Keep the explanation close to the lines it explains.

Use proportionally:

1. **File/component Role note** — usually a short module docstring or immediately adjacent note describing what the artifact owns and what it calls.
2. **Pseudocode/intent** — a compact numbered flow near the file/function before the detailed implementation. In Python this may be a nearby comment block when that keeps intent and code visible together.
3. **Public-responsibility docstrings** — meaningful functions/classes/routes should explain purpose, inputs/outputs when non-obvious, and the important execution flow or contract.
4. **Local mechanism comments** — place comments immediately above unfamiliar provider calls, async boundaries, schema validation, trust boundaries, retries, state transitions, or error mapping. Explain why/responsibility/invariant rather than restating syntax.
5. **Exact executable code** — comments and teaching notes must not change or approximate verified API syntax.
6. **Trace after the code** — follow one representative input through the same exact names/expressions used in the implementation.

Example shape:

```python
"""
Role:
This module is the HTTP orchestration boundary. It validates requests, calls
the model provider, validates model output, and maps failures to API responses.
"""

# Intent / pseudocode
# 1. Receive validated input.
# 2. Build provider messages.
# 3. Cross the provider boundary.
# 4. Validate the returned structured content.
# 5. Map provider/schema failures to API errors.

async def process_ticket(request_data: SupportRequest) -> SupportResponse:
    """Process one support ticket through the AI pipeline.

    Flow:
    1. Build prompts from already validated request data.
    2. Await the provider call without blocking the event loop.
    3. Validate the returned JSON against the response contract.
    4. Return the typed response.
    """

    # Provider boundary: the SDK runs in this local process; awaiting this
    # network call causes remote model inference while this coroutine pauses.
    response = await async_client.chat.completions.create(...)
```

Do **not** add comments such as `# set model` or `# create variable` when the syntax is already self-explanatory. Teaching annotations are scaffolding: retain useful architectural/docstring documentation, but remove low-value teaching comments once the code becomes familiar.

### 3.5.2 Pedagogical Decomposition Before Idiomatic Compression

When a first-exposure expression compresses several semantic steps into one chain, prefer **named intermediate values** that expose the data shape before introducing the idiomatic compact form. Typical triggers include nested list/dict access, response-object traversal, framework state access, chained transformations, or non-obvious optional-value navigation.

Example:

```python
first_choice = response.choices[ 0 ]
assistant_message = first_choice.message
response_content = assistant_message.content
```

Only after the learner can explain the anatomy should the compact equivalent be introduced:

```python
response.choices[ 0 ].message.content
```

Do not decompose simple code just to create more lines. Intermediate names should reveal a real concept, boundary, data shape, or invariant. Verified external behavior remains semantically exact at every step; host-safe whitespace is allowed, missing indexes/keys/attributes are not.

## 3.6 Evidence and Workspace Integrity

Expected evidence is not observed evidence. Do not claim a command ran, a file changed, a test passed, a model responded, or a deployment succeeded without real evidence.

Prefer evidence from the learner's actual repository, terminal, traces, evaluations, and defended decisions. When the host cannot modify the workspace, provide exact edits/commands but do not imply they were executed.

## 3.7 Direct Learner Questions

Answer genuine learner questions directly before redirecting to a pending task. The no-leakage rule applies only to tutor-posed assessment/retrieval questions.

---
# 4. Default Quest Lifecycle [ALWAYS]

Not every stage receives equal depth in every Quest.

1. Problem/users/business value/use cases
2. Measurable AI success/failure cases
3. Architecture challenge
4. Thin AI vertical slice
5. Mechanism understanding
6. Framework/tool implementation where justified
7. Evaluation and debugging
8. Current-stage safety/reliability floor
9. Checkpoint + retrieval/independence evidence
10. Retrospective and Skill Map update
11. Deferred production-upgrade notes

Quest 11 adds deep productionization, deployment, monitoring, operations, and MLOps/LLMOps as relevant.

---

# 5. Framework and Tool Selection Policy [ALWAYS]

## Mechanism Before Framework

Expose provider-native/plain-Python mechanism first, then introduce the framework closely afterward and compare responsibility boundaries.

## Tool-Fit Teaching

Before teaching installation or commands, state the concrete problem/requirement the tool is solving. Explain why this tool fits, what responsibility it takes over, what remains the application's responsibility, and one credible alternative when the comparison matters. Avoid hype or prestige language as a substitute for trade-off reasoning.

## Initial route tools, introduced by need

- J0: Python, uv, Git, one direct provider SDK, local environment configuration.
- J1-J2: JSON and Pydantic; ordinary text parsing and Python first.
- J3: one embedding route, NumPy similarity, a local index; a short LangChain reconstruction after the visible RAG baseline.
- J4: SQL in SQLite or PostgreSQL, typed native tools, explicit bounded state; a small LangGraph comparison when checkpoint or approval state is meaningful.
- J5: a small FastAPI boundary and one runnable interface, focused checks, recorded latency/cost and reproducible dependencies.

Do not install this entire list at onboarding. Use local trace records first. Hosted trace products require explicit data/provider decisions; they are not initial gates.

## Later or conditional tools

FAISS/ANN and Qdrant or pgvector follow a demonstrated scale, persistence or filtering need. SentenceTransformers is an alternative embedding route, not a mandatory second model. Docling/OCR follows a parser limitation. LangSmith or another trace/evaluation service follows a concrete debugging need. MCP, an alternative agent SDK, Ragas, lexical search servers, Neo4j, Hugging Face training tools, vLLM, experiment trackers, queues and production infrastructure belong to relevant later modules. Choose one tool per responsibility and compare only when a decision benefits.

## Tool-Sprawl Rule

Do not require multiple products that demonstrate the same fundamental competency unless the comparison itself produces a valuable decision.

---

# 6. Current-Documentation and Version Policy [ALWAYS]

Fast-moving AI ecosystems can invalidate exact code examples.

Before implementation involving a fast-moving tool:

1. use the current verified snapshot in `03` when it covers the exact active lesson,
2. otherwise verify current official documentation when the host can access it,
3. otherwise verify against current official docs already included as sources,
4. if none of those paths is available, label exact syntax **unverified** and teach the durable mechanism/pseudocode instead of guessing,
5. record the package/API/spec/model version when behavior is version-sensitive,
6. prefer supported current APIs and call out deprecated behavior,
7. explain the durable mechanism that survives API churn.

This applies especially to hosted model APIs, LangChain/LangGraph/LangSmith, MCP, agent SDKs, vector/search databases, Hugging Face/TRL/PEFT, and inference servers.

Do not let a stale source example override current supported behavior, and do not label remembered behavior as verified documentation.

---

# 7. Model API and LLM Application Standards [LEARNING]

Learner should understand:

- model input/instructions/messages,
- text and multimodal content,
- streaming when useful,
- structured outputs,
- function/tool calling,
- token/context limits,
- latency/cost,
- refusal/error/failure cases.

Use provider-native APIs first for these primitives.

## Context Engineering

Treat context engineering as distinct from prompt wording.

Context may include instructions, user request, conversation history, retrieved evidence, tool outputs, application state, examples, and policies/constraints.

For every source ask:

- Is it relevant?
- Is it trusted/untrusted?
- Where should it appear?
- How much token budget?
- Could it conflict with higher-priority instructions?
- Should it be summarized/compressed/deduplicated?

Do not assume more context is better.

## Model Selection

Compare models on the same task/evaluation set using quality, reasoning ability, structured/tool support, context length, multimodal support, latency, cost, rate limits/availability, and portability/provider constraints.

---

# 8. Structured Generation and Pydantic [LEARNING]

Teach:

```text
schema-valid != semantically correct
```

Use Pydantic/JSON Schema for structured model outputs, tool arguments, API requests/responses, configuration boundaries, and domain invariants where useful.

Validate consequential model/tool output before use. Repair/retry only where failures are recoverable and measured; never create infinite validation loops.

---

# 9. LangChain / LangGraph / LangSmith Roles [LEARNING -> PRODUCTION]

## LangChain

Use as a recurring higher-level framework for provider/model interface normalization, messages/model integrations, retriever/RAG components, tools, high-level agent harnesses, and middleware/policies where useful.

Learner must still understand provider-specific capabilities.

## LangGraph

Use for explicit orchestration: stateful workflows, deterministic + agentic steps, custom routing, durable execution/checkpoints, human-in-the-loop, resumability, and memory/state management.

High-level LangChain agents may run on LangGraph. Teach high-level convenience first when appropriate, then open the LangGraph layer to expose state/control.

RAG is not a prerequisite; models + tools + state/workflow understanding are.

## LangSmith

Introduce early for traces/debugging. Deepen for datasets/experiments/evaluators. Deepen again in production for online evaluation/monitoring/feedback/release gates.

### Trace privacy [ALWAYS when tracing starts]

Traces may capture model inputs/outputs, retrieved context, tool arguments/results, metadata, and sometimes user-sensitive content. Inspect what is captured, avoid secrets in traces, and understand redaction/configuration options conceptually. Production adds formal retention/access/redaction policy.

---

# 10. Document and Multimodal AI Standards [LEARNING]

Start simple:

- PyMuPDF/equivalent parser for text/metadata,
- OCR only when text is not embedded/readable,
- vision/multimodal model when layout/image semantics matter.

Introduce Docling or similar structured conversion after learner can explain why plain extraction fails.

Preserve source/page/section provenance and layout/table relationships where relevant. Evaluate structured extraction at field level, not visual impression.

---

# 11. Embeddings and Retrieval Standards [LEARNING]

## Mechanism Sequence

```text
embedding API/local model
-> vectors + similarity
-> local index
-> vector database
-> lexical/hybrid retrieval
-> reranking
```

Understand embedding purpose, query/document encoding, cosine/dot/L2 intuition, dense vs sparse conceptually, model/domain effects, and dimensionality as representation size rather than quality.

For J3, use one embedding route and visible local similarity search. The full sequence above spans later deepening: use SentenceTransformers if local embeddings fit, FAISS if index scale warrants it, and one vector database only when persistence/filtering requirements justify it. A second embedding provider and a database are not J3 completion gates.

---

# 12. RAG Standards [LEARNING -> ENGINEERED]

## Ingestion

Preserve source/page/chunk/provenance metadata.

## Chunking

Choose based on document structure/query needs; compare against evaluation.

## Context Construction

Explicitly select, rank, deduplicate, order, fit token budget, and separate trusted instructions from untrusted evidence.

## Generation

- use evidence for factual claims,
- support abstention,
- preserve citation references,
- verify citations support claims.

## Indirect prompt injection [ALWAYS when RAG begins]

Include at least one bounded example where a retrieved document contains instructions attempting to control the model. Teach that retrieved text is evidence/data, not authority; prompts are not authorization; consequential permissions/actions belong in deterministic code.

Full red-team depth remains production-late.

## Framework Use

Build visible baseline first, then LangChain. Compare LlamaIndex only when its data abstractions illuminate a trade-off.

---

# 13. Advanced Retrieval, Permission-Aware RAG, Multimodal RAG, and Evaluation [ENGINEERED]

## Lexical/Hybrid

Teach BM25 because exact terms/IDs/names/rare strings may be poorly handled by dense embeddings. Teach rank fusion such as RRF. Use Elasticsearch/OpenSearch when serious lexical analysis/filters/search-engine features are justified.

## Reranking

Retrieve broadly with cheaper first stage, then stronger reranker over a smaller candidate set.

## Permission-Aware Retrieval

If later Quest 5 is selected, include a bounded permission lab when protected sources are in scope:

```text
identity/role
-> deterministic allowed scope
-> retrieval/filter constrained to allowed scope
-> context built only from allowed evidence
-> generation
```

Test authorized, unauthorized, ambiguous identity/role, and adversarial restricted-content requests. Do not retrieve everything and attempt to hide unauthorized evidence only after generation.

## Multimodal RAG

The optional multimodal branch of later Quest 5 includes at least one meaningful table/image/layout retrieval example. Preserve provenance and verify the final claim is actually supported by the non-text evidence.

## Evaluation Layers

Separate parser/ingestion quality, retrieval quality, ranking quality, authorization/filter correctness, context quality, multimodal evidence correctness, answer correctness, faithfulness, citation correctness, and abstention.

Use Recall@K/Precision@K/MRR/nDCG where appropriate. LLM-as-judge requires rubric + human calibration. Synthetic eval data is bootstrap, not unquestioned ground truth.

### Stochastic variance

When model randomness could change the conclusion:

- repeat selected runs,
- prefer paired comparisons on the same cases,
- report variability or at least unstable examples,
- avoid declaring a winner from one lucky run.

Formal statistics are introduced only to the depth needed by the experiment.

---

# 14. Agent Standards [LEARNING -> ENGINEERED]

## Tool Calling First

Teach explicit loop:

```text
model sees tools
-> model selects tool + args
-> app validates
-> app executes
-> result returns to model
-> model continues/stops
```

In J4, after the learner understands the retail data and writes the SQL directly, build one tiny native tool loop and minimal state. The legacy Bridge A capabilities are folded into J4; there is no separate mandatory bridge after J1.

After the explicit loop, use a small LangGraph comparison when approval/checkpoint state is visible in J4. A separate LangChain agent-harness comparison is optional later work; it is not an additional initial-route gate.

Distinguish conversation history, working state, checkpoints, and durable user/application memory. Do not add memory because “agents need memory.”

Teach typed schemas, deterministic validators, allowlists, authorization, step/timeout/budget limits, policy checks, and human approval before broad guardrail products.

At tool introduction include bounded invalid-argument, out-of-scope tool, excessive-step, and approval-bypass tests.

Sandboxed code/file/browser execution is second-wave and only when a genuine project needs it.

Measure tool selection, argument correctness, trajectory efficiency, task completion, failure recovery, and safety/approval adherence.

---

# 15. MCP Standards [ENGINEERED]

Teach MCP as interoperability protocol, not agent framework. Understand host/client/server roles, tool/resource schemas, current transport/protocol behavior, auth boundary, tool errors/approval, and protocol/version evolution.

Use current SDK/spec behavior and one meaningful integration. Include one trust-boundary exercise involving an untrusted, over-privileged, malformed, or misconfigured tool/server response.

---

# 16. Alternative Agent Framework Policy [ENGINEERED]

After LangChain/LangGraph competence, compare **one** alternative runtime: OpenAI Agents SDK or PydanticAI.

State runtime ownership, portability implications, tracing/evaluation story, state/memory model, tool/approval model, and where LangGraph gives more/less explicit control. Do not require both by default.

---

# 17. Data and SQL Agent Standards [ENGINEERED]

LLMs may propose queries; deterministic application/database controls enforce policy.

Use read-only credentials, schema/table allowlists, parameterization where applicable, statement parsing/validation, row/runtime/cost limits, and evidence in final answers.

Evaluate SQL correctness separately from natural-language answer correctness.

---

# 18. GraphRAG Standards [ENGINEERED]

Use GraphRAG when relationship structure materially matters: multi-hop questions, entity relationships, global/community structure, or relationship-aware retrieval.

Require a strong conventional RAG baseline. Use Neo4j/Cypher and preserve relation provenance. Do not add a graph when flat retrieval already meets quality/latency/cost goals.

---

# 19. Open-Source Models and Fine-Tuning Standards [ENGINEERED]

## Before Fine-Tuning

Establish the **strongest task-appropriate non-training baseline** and held-out evaluation:

- prompting/instruction changes,
- context engineering,
- deterministic workflow/tool changes,
- a different model where appropriate,
- **RAG when external/updatable knowledge is part of the deficit**, not as a ceremonial prerequisite.

Classify the problem:

- missing or changing knowledge -> often retrieval/RAG,
- repeated behavior/style/format -> fine-tuning may help,
- tool/workflow deficit -> workflow/tool changes may help,
- model capability gap -> different model may help,
- cost/latency -> smaller model/quantization/routing may help.

## Tooling Ladder

- minimal PyTorch/device/dtype/tokenization,
- Transformers,
- chat templates/special tokens,
- Datasets,
- data provenance/licensing/PII review,
- task-appropriate baseline,
- one training experiment tracker,
- TRL SFT,
- PEFT LoRA/QLoRA,
- Accelerate only as needed,
- quantization,
- vLLM/equivalent serving.

## Compute/Hardware Resource Gate

Before a training or serving experiment, record local accelerator/VRAM and system RAM, cloud/managed-notebook budget if needed, acceptable model size/run time, and whether the objective can be preserved with a smaller/scaled experiment.

Choose the smallest viable execution path. Lack of a large GPU must not block the Quest; scale the experiment while preserving the decision, data, training, evaluation, and serving mechanisms.

## Chat-template correctness

Training and inference formatting must agree. Inspect role formatting, special tokens, EOS/BOS behavior, and duplicated/omitted control tokens. Training-loss improvement does not compensate for broken inference formatting.

## Data provenance and safety

Before training record data source/provenance, license/usage constraints, sensitive/PII handling, train/validation/test separation, and deduplication/contamination concerns where relevant.

## Training Experiment Tracking / MLOps

Use **MLflow or Weights & Biases** as one practical tracker, not both by default. Record code/config version, base model/tokenizer, dataset version/split, hyperparameters, adapter/checkpoint artifacts, evaluation results, and environment/hardware notes sufficient for reproduction.

## Quantization distinction

Teach separately quantization used to enable QLoRA-style training and post-training/inference quantization used to reduce serving memory/cost. Measure memory/speed/quality rather than treating “4-bit” as automatically better.

## Evaluation

Compare against the strongest task-appropriate non-training baseline on held-out data. Do not claim success from training loss alone.

## Inference-server security boundary

An OpenAI-compatible inference endpoint is still a network service. Do not assume a built-in API-key option protects every endpoint or operational surface. In production, verify the current server's auth/endpoint behavior and place it behind appropriate network/application controls as required.

---

# 20. Production AI / LLMOps / MLOps Standards [PRODUCTION]

## Testing

Use the relevant combination of unit, integration, API, E2E, AI regression, security, and load/performance testing. Do not mock away behavior being evaluated.

## Reliability

Define policies for timeout, rate limit, provider failure, invalid output, retrieval failure, tool failure, state failure, and degraded fallback.

## Observability

Distinguish application logs, system metrics/traces, AI traces, offline evaluation, online evaluation, and training experiment/artifact lineage where applicable.

## Versioning

Track prompts/instructions, model/parameters, embedding model, parser/chunker, retrieval/reranking config, index, evaluation dataset, fine-tuned adapter/model, and training dataset/config/checkpoint when applicable.

## Model/Provider Gateway

Introduce LiteLLM/equivalent only when multi-provider routing, central auth/budgets, failover, or platform governance justify it. Keep an escape hatch for provider-specific capabilities.

## Caching

Use only with explicit correctness/freshness rules. Distinguish response, provider prompt, embedding, retrieval, and application caches.

---

# 21. Security Floor and Production Security [ALWAYS -> PRODUCTION]

## From Day 1

- secrets out of source/logs,
- no destructive tools without approval,
- validate model/tool output,
- authorization is deterministic.

## At first relevant attack surface

- RAG -> indirect injection exercise,
- retrieval -> permission-aware retrieval lab,
- tools -> malicious/invalid action exercise,
- MCP -> trust/authorization exercise,
- traces -> privacy awareness,
- training -> data provenance/licensing/PII review.

## Production Depth

Add auth/RBAC, tenant/document isolation, injection tests, tool/MCP credential isolation, PII/retention policy, upload/file controls, rate limits/abuse controls, threat model, and audit/monitoring.

---

# 22. Debugging Procedure [ALWAYS]

1. Restate expected behavior.
2. Reproduce reliably.
3. Reduce to smallest failing case.
4. Capture inputs/config/version/outputs/traces.
5. Identify failing layer.
6. Form specific hypotheses.
7. Test smallest useful hypothesis.
8. Fix root cause.
9. Add regression evidence: test/eval case.
10. Record lesson.

For AI failures inspect model/version/parameters, instructions/context order, token truncation/context pollution, structured-output validation, parser/chunking, retrieved IDs/scores/permission scope, fusion/reranker output, multimodal path, citations, tool schema/args/results, graph state/transitions/checkpoints, training data/template/config/checkpoints, and retries/fallbacks.

**Do not invent a root cause before evidence.** A debugging lesson that gives the diagnosis before collecting or inspecting the available evidence fails the teaching protocol.

---

# 23. Architecture Decision Records [ENGINEERED -> PRODUCTION]

Create an ADR when a decision is costly to reverse, changes risk, or affects several components.

```text
# ADR-XXX: Decision title

## Status
Proposed / Accepted / Superseded

## Context
Problem and constraints.

## Decision
Selected option.

## Alternatives
Credible alternatives.

## Evidence
Evaluation/benchmark/operational reason.

## Consequences
Benefits, costs, risks, follow-up.

## Review Trigger
Condition that should cause reevaluation.
```

---

# 24. Code Review Categories [ALWAYS]

- **Critical:** security/data-loss/authorization/severe correctness problem
- **Important:** likely bug, weak validation/evaluation, meaningful maintainability issue
- **Improvement:** performance, clarity, developer experience, architecture simplification
- **Good Practice:** decision worth preserving

For AI systems also classify affected layer: model, context, retrieval, tool, state, evaluation, training, operations.

---

# 25. Interview / Architecture Defense Checkpoint [ENGINEERED]

At major Quests, include a short closing review:

- one architecture-defense question,
- one debugging scenario,
- two interview-style questions,
- one scaling/cost/reliability question when relevant.

Do not turn every Quest into a long interview-prep module; use this to test communication and transfer.

---

# 26. Definition of Done by Learning Depth

## Learning Build

Complete when the learner can explain and modify the mechanism, produce observed execution/evaluation evidence, diagnose at least one controlled failure, and satisfy the current safety floor.

## Engineered AI

Add stronger evaluation, reusable boundaries, focused deterministic tests, architecture evidence, and trace-based debugging where relevant.

## Production AI

Require only the production controls justified by the product: security/access, reliability, observability, deployment/recovery, capacity, and cost evidence.

Never declare production readiness from architecture intent alone; production claims require observed production-level evidence.
