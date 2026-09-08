# Active increment assessment cards

Tutor reference for [the route](CURRICULUM.md), governed by [teaching](TEACHING_GUIDE.md) and [evidence protocol](PROGRESS_PROTOCOL.md). Read only the current increment. These are acceptance contracts, not additional milestones or a script to expose during Assess. J0 retains its small 0.3–0.9 route; do not load later cards on first-call resume.

For each attempt capture task/input, expected and observed behavior, safe output/source pointer, learner explanation, actual assistance and failure layer. Local boundary checks use synthetic fixtures without provider calls; AI quality needs separate observed cases. Supported early work is valid practice. For independent claims only `none` or `docs` counts; a hint/scaffold/example requires a different independent attempt. Select one unfamiliar task at a time, withhold its answer in Assess, and return to Learn on a help request.

Readiness means required non-transfer behavior and understanding are evidenced. Where transfer is pending, `ready` requires the protocol's grounded delayed-practice queue; it permits advancement but does not certify retention. `complete` requires every gate. The elapsed-time floor is a scheduling safeguard, never scientific sufficiency. Remediation reopens the demonstrated missing prerequisite and preserves valid artifacts.

## J1 — Medical extraction

**Prerequisite:** J0 JSON/boundary readiness; **stage gates:** execution, explanation, debug; **capabilities:** E05–E07, continued E04.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Schema and extraction | Required fields/types/nulls are explicit. Valid payload passes; malformed JSON and wrong type fail locally; absent fact remains null. Learner distinguishes syntax, schema and truth. | Add a field for an explicitly stated document fact and justify its absent-value rule. | Isolate parsing versus schema validation on a hand-written payload before another model request. |
| Source checks | Exact spans resolve to the input; unsupported values are flagged. Cases include absent, negated, uncertain, old/current statements and instruction-like note text. A schema-valid unsupported claim fails source review. | Diagnose a new mismatched span or chronology case and explain which layer owns the correction. | Trace one field to source and fix its deterministic invariant, then try a different note. |
| Review and comparison | Source and extracted values are visible together; a human correction retains original and corrected values/reason. Compare one change on fixed cases, reporting counts and denominator including omissions. | Explain a previously unseen review flag and correct it without losing provenance. | Reduce to one source/value/correction path; restore the missing audit information and rerun it. |

Worked examples and scaffolds are permitted in Learn. The stage debug gate must reflect the learner's actual diagnosis, not assistant-authored repair. Independently applied skill claims need separate explanation, modification, debug and delayed transfer; J1 execution alone cannot grant them. Revisit extraction transfer in J2.

## J2 — Retail classification and transfer

**Prerequisite:** J1 source-grounded schema behavior; **stage gates:** modification, explanation, transfer; **capabilities:** E08–E09.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| New domain schema | Learner adapts known validation to category, stated order ID, missing information, draft and escalation reason. Test missing ID, ambiguous request, mixed intent and invented order status. No order system access is claimed. | Design a new bounded request category and explain which medical rules transfer and which change. | Return to one schema/value invariant; provide only the requested help, then use a fresh category. |
| Language and delay | Record Arabic and English results separately against explicit expected labels; identify untested code-switch cases. A later unfamiliar request demonstrates transfer with recorded assistance and elapsed delay. | Adapt validation to a new request without copying a finished schema. | Keep supported modification as practice, queue a grounded later attempt and continue useful work if `ready`. |

Start with a learner sketch; hints are available after an attempt or direct request. Same-session transfer is useful practice but cannot certify delayed retention. Do not block J3 solely to wait for retention when the ready contract is met.

## J3 — Retrieval and grounded answers

**Prerequisite:** J2 readiness and Python lists/functions plus a small vector explanation; **stage gates:** execution, explanation, debug; **capabilities:** E09–E13.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Visible retrieval | Versioned document/section/chunk IDs survive ingestion. Inspect vectors and rank passages; measure Recall@k against labeled IDs. Include a relevant passage split across a chunk boundary. | Trace an unfamiliar question to ranked passages and explain a missed expected source. | Inspect chunks/ranking before changing the answer prompt; compare one chunking choice. |
| Answers and abstention | Every citation supports its attached claim; missing, conflicting, expired and instruction-like passages produce the defined handling. Fixture checks catch nonexistent citation IDs and wrong versions. | Diagnose whether a new wrong answer came from retrieval or generation. | Freeze retrieved context, then isolate the unsupported answer claim or missing retrieval. |
| Framework comparison | Reproduce one slice in LangChain and name which ingestion/retrieval/prompt responsibilities moved. Keep a justified baseline and disclose corpus/language limits. | Change one retrieval setting and explain its effect across the visible and framework paths. | Trace one input through both paths; avoid adding another abstraction to hide a failing step. |

Allow documentation and supported learning. Do not call a framework-produced result independent understanding. Protected data is optional; if introduced, add deterministic access-scope checks before retrieving it.

## J4 — Scoped tools and approval

**Prerequisite:** J3 plus hand-written parameterized SQL filters, joins and aggregation on known synthetic rows; **stage gates:** execution, explanation, debug; **capabilities:** E14–E17.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| SQL and read tool | Expected query rows match. Trusted caller scope controls `get_order`; own order passes, wrong-customer and missing-order queries fail safely. Invalid/injected arguments never broaden scope. | Diagnose a new cross-customer lookup without relying on prompt wording. | Run the fixed query directly against two synthetic customers and trace the trusted scope. |
| Native loop | Validate arguments, link tool result to its call identity, bound steps and expose tool exceptions. Test missing tool, invalid arguments and exhausted step budget without false success. | Trace and repair an unfamiliar tool-result or stopping failure. | Isolate one proposal/validated call/result cycle with a fake tool before model integration. |
| Approval state | Before any simulated effect, bind approval to immutable proposal ID/version or digest, trusted actor, target and exact parameters. Test mutation after approval, changed actor, changed target, stale version, rejection, missing approval and replay; all rejected paths produce zero effects. Approved original executes once. | Diagnose a replay or changed-parameter proposal and justify the execution-time check. | Use a local transition fixture and effect counter; repair binding/consumption before another workflow run. |
| State comparison | Reconstruct a small slice in LangGraph and explain state/checkpoint responsibilities. The same rejection and once-only cases hold. | Change a transition and explain how the framework preserves the approval contract. | Trace application-owned state separately from framework persistence. |

Assistance is recorded; deterministic acceptance cases begin when each boundary is introduced, before model integration. No live refunds or outbound messages. A local once-only demonstration does not prove distributed concurrency or production recovery.

## J5 — Independent delivery

**Prerequisite:** medical J1 and retail J4 outcomes with valid prerequisite evidence; **stage gates:** execution, explanation, modification, debug, transfer; **capabilities:** E18–E22 plus route coverage.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Reproducible interface | Each product runs from documented locked dependencies and exposes a small API/interface. Invalid request/response, provider timeout and suitable bounded retry have understandable outcomes. Existing schema/span/scope/approval checks still pass. | Make a bounded unfamiliar interface change and explain the request-to-result path. | Reproduce the failing boundary locally; repair only the missing mechanism before reassessing on a new case. |
| Honest evaluation | Freeze held-out expectations before use; report counts, denominator, model/config/date, critical failures and unmeasured cost/latency as unknown. Disclose tuning contamination and repeated-case variability. | Diagnose an unfamiliar failure and defend one design tradeoff from actual evidence. | Separate deterministic failure from model behavior; fix the report or mechanism and use a fresh assessment case. |
| Ownership and handoff | Runnable demos, readable READMEs and contribution disclosure match actual artifacts. Learner explains architecture, changes and debugs independently, then performs delayed unfamiliar transfer. | Transfer a delivery change to the other product after the eligible delay with normal docs allowed. | Preserve the assisted result as learning work; return to Learn if requested and schedule a different independent attempt. |

J5 explanation, modification, debug and transfer gates require assistance `none` or `docs`; execution may use supported code. Generated code, worked examples and answer-shaped hints cannot satisfy final ownership. J5 `ready` requires E01–E22 at least `practiced` and supports useful next work while transfer is queued. Final route completion requires all gates and E22 `applied_independently` or the stronger `production_understanding`. Inspect cross-stage failures and reconcile independent claims explicitly. No test count, portfolio polish or elapsed time alone establishes employment or production readiness.


Readiness advancement requires an append-only maintainer readiness decision referencing the then-current passing non-transfer proof and its review time/task/trigger, as well as the grounded live queue required by the evidence protocol. Historical readiness uses that prior decision, never a retroactive queue; preserve valid history through later regression, reopen claims whose proof was corrected, and reassess with fresh prerequisite and downstream evidence. Final J5 completion requires every initial-route milestone complete, including earlier delayed transfer. The readiness decision is teaching administration, not learner competence.
