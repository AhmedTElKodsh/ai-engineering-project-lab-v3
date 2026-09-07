# AI Engineering Skill Map

**Version:** V3.2 - Medical and Retail Junior Application Path  
**Revision date:** 2026-09-07

## Evidence authority

This is the canonical skill-status ledger. Curriculum revisions do not award skills. All initial statuses below remain **Not started** because this revision adds no observed learner evidence. `03` retains lesson exposure/context, including the pending first call; it does not establish completed competence. Reconcile against the newest real evidence before updating.

Status meanings: **Not started** = no qualifying evidence recorded; **Introduced** = mechanism explained with learner engagement; **Practiced** = learner performed a supported task; **Applied independently** = learner completed a new task with normal documentation allowed and solution support recorded; **Production understanding** = additional operational decisions and failure evidence in a real scoped setting. Merely running a generated solution cannot establish independent application.

Use a small active slice (normally 5-12 skills internally); show 3-6 only if it helps the learner. Do not make the full table an onboarding quiz. Record behavior and understanding independently and retain the learner's explanation verbatim or with a link to the original response.

## Initial application route

| ID | First useful stage | Capability | Current status | Evidence target |
|---|---|---|---|---|
| E01 | J0 | Python/project execution | Not started | Launch, modify and interpret a traceback in the actual project |
| E02 | J0 | Configuration, secrets and Git | Not started | Keep a key local, explain environment loading, inspect a meaningful diff |
| E03 | J0 | Provider request/response boundary | Not started | Run a native call and explain messages, response structure and local/model behavior |
| E04 | J0 | JSON and typed validation | Not started | Distinguish valid JSON, valid schema and correct content |
| E05 | J1 | Grounded extraction | Not started | Return stated facts with valid spans; flag missing/negated/uncertain content |
| E06 | J1 | AI behavior evaluation | Not started | Define expected outcomes, count failures and compare one change |
| E07 | J1 | Human review interface | Not started | Show source and editable extracted values with a correction record |
| E08 | J2 | Independent domain transfer | Not started | Build a new retail schema with reduced support |
| E09 | J2-J3 | Arabic/English behavior | Not started | Report separate language results; document untested code-switch/cross-language cases |
| E10 | J3 | Embeddings and similarity | Not started | Inspect vectors, rank passages and explain similarity limitations |
| E11 | J3 | Ingestion/chunking/provenance | Not started | Trace an answer source to a versioned document section |
| E12 | J3 | Grounded RAG | Not started | Separate retrieval/answer errors, verify citations and abstain on missing evidence |
| E13 | J3 | Framework responsibility | Not started | Compare a visible RAG slice and LangChain implementation |
| E14 | J4 | SQL fundamentals | Not started | Write parameterized filters, joins and aggregation; validate expected rows |
| E15 | J4 | Native tool calling | Not started | Validate arguments, execute a bounded tool and return linked tool results |
| E16 | J4 | Authorization and action scope | Not started | Block cross-customer access and unapproved simulated actions in code |
| E17 | J4 | State and bounded workflows | Not started | Explain transitions, stop conditions, failures and a small LangGraph comparison |
| E18 | J5 | HTTP/API and interface | Not started | Run a small usable app with validated boundaries and clear errors |
| E19 | J5 | Basic failure handling | Not started | Handle timeout/transient failure without unbounded or unsafe retries |
| E20 | J5 | Focused deterministic checks | Not started | Verify schema/span, data scope and approval transitions separately from model quality |
| E21 | J5 | Held-out evaluation and tradeoffs | Not started | Report counts, denominators, limits, latency/cost and repeat variability |
| E22 | J5 | Independent delivery and explanation | Not started | Make an unfamiliar change, debug a new failure and explain architecture |

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
