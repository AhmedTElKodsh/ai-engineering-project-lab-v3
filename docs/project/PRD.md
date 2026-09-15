# SupportOps AI: focused product requirements

Status: planned learner implementation, not a delivered application. Adapted from the uploaded Commerce Support Copilot baseline on 2026-09-15. Keep native J0-J5, E01-E22 and the existing progress protocol. Uploaded FR/NFR identifiers are traceability labels, not new learning milestones.

## Purpose and non-goals

Help an internal support employee understand a customer message, retrieve policy evidence, inspect authorized order facts, and prepare one human-approved simulated damaged-item replacement. The learner coach teaches construction; the product copilot is the application being built. Documents explain policies, tools provide operational facts, and ordinary code enforces permissions and business rules.

Build one evolving application in `projects/supportops/`, or continue an already verified app elsewhere. A terminal result is enough early. Use synthetic small-appliance examples and separately evaluate English and Arabic. Business-inspired examples are useful but do not imply business adoption or permission to transmit raw tickets.

No real refunds, payments, shipping, replacement fulfillment, outbound messages, arbitrary SQL/shell tools, autonomous policy edits, or production customer data. Do not require a multi-agent platform, a large dataset, a web service or an enterprise database before the first useful result.

## Actors and completion levels

The support employee proposes; a different authorized same-scope manager approves the exact proposal once actions arrive. Knowledge administration does not imply approval permission. Early exercises use explicit synthetic identities in trusted application/test context, never roles inferred from model arguments. Real login and concurrent/multitenant operation require selected operational work.

A closed mini-tool fulfills one input/output promise, runs with documented inputs, has focused normal/failure cases, and can be explained and modified by the learner. Initial J5 completion is one reproducible local release with honest evaluations and independent delivery evidence. Operational readiness requires separate evidence for a chosen deployment. None guarantees employment or universal security.

## Requirements retained and staged

| ID | Retained intent | Initial scope and later trigger | Planned acceptance evidence |
|---|---|---|---|
| FR01 | Create and resume cases | Intake J1; durable resume Q6 when selected | Unknowns preserved; restart behavior tested only when implemented |
| FR02 | Validated ticket analysis | J1-J2 | Distinguish parse/schema/source failures, negation and uncertainty |
| FR03 | Knowledge lifecycle | Versioned files J3; persistent ingestion Q5/Q11 | Source lineage; update/deletion behavior when introduced |
| FR04 | Eligible evidence and cited answers | J3 | Relevant source, supported citation, abstention and conflict cases |
| FR05 | Safe operational reads | J4 | Parameterized queries; allowed/denied/missing/error outcomes |
| FR06 | Deterministic eligibility | J4 action slice | Fictional BR01-BR08 checked on synthetic cases |
| FR07 | Bounded workflow | Local J4; restart durability Q6 | Step/time limits and honest outcomes; persistence tested separately |
| FR08 | Exact proposal review | J4 | Mutation, stale/rejected/missing approval and actor substitution denied |
| FR09 | Safe writes and reconciliation | Local simulated J4; concurrency/external work Q6/Q11 | Defined local replay tests; unknown outcome never called success |
| FR10 | Inspectable employee interface | Terminal/table J1; small API/interface J5 | Source/value visible, proposal and actual result distinguishable |
| FR11 | Evaluation and execution evidence | J0 onward; hosted tracing conditional | Fixed cases, config, component errors and safe run records |
| FR12 | Classical routing comparison | Selected ML extension | Grouped splits; TF-IDF classifier versus LLM on the same test cases |
| FR13 | Asynchronous ingestion | Selected Q11 extension | Job retry/restart/quarantine evidence in the actual worker |
| FR14 | Reproducible packaging/operation | Local J5; deployment Q11 | Clean local run; containers/migrations/rollback only when selected |
| NFR01 | Authorization/isolation | First protected boundary | Negative tests before model integration; no blanket security claim |
| NFR02 | No unsafe or duplicate effects | Local J4; concurrency Q6/Q11 | Explicit scope and effect counts; no distributed guarantee from local tests |
| NFR03 | Measurable quality | Small cases throughout; held-out J5 | Counts, denominators, failures and limits; uploaded percentages are candidate targets |
| NFR04 | Diagnosability | First call, then retrieval/tools | Actual input/evidence/tool/error path with sensitive data excluded |
| NFR05 | Bounded latency/cost | First authorized model call | Explicit time/call/batch budget; available usage; unknown is not zero |
| NFR06 | Reproducibility | Every mini-tool and J5 | Actual command, declared dependencies, labeled fake/live execution |
| NFR07 | Privacy/configuration safety | First setup | No secrets/raw tickets in logs or commits; external transmission authorized |

No requirement row is a passing-test claim. FR12/FR13 and advanced forms of FR07/FR09/FR14 are not hidden initial J5 requirements.

## Evidence and change control

Begin with the seven small support fixture patterns, a few malformed outputs, and three short policies at J3. Add cases when a new failure or constraint warrants them, not to satisfy an arbitrary corpus size. Development fixtures are visible and are not a held-out set. Freeze unfamiliar assessment/test cases before use, disclose tuning contamination, and report language-specific scope.

At a mini-project close retain its input/output, command, expected versus observed result, one limitation, actual assistance, independent variation and exact next action. Attach interview practice to the artifact rather than adding a new prerequisite course.

[Contracts](CONTRACTS.md) define source and action semantics. [Release cards](RELEASES.md) define runnable results. [Curriculum](../CURRICULUM.md) owns sequence and deferrals; [progress protocol](../PROGRESS_PROTOCOL.md) alone owns advancement. Changing a business rule requires an explicit decision and regression case. A plan edit does not authorize a provider budget or award learner progress.
