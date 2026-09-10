# Active increment assessment cards

Tutor reference for [the route](CURRICULUM.md), governed by [teaching](TEACHING_GUIDE.md) and [evidence protocol](PROGRESS_PROTOCOL.md). Read only the current increment. These are acceptance contracts, not additional milestones or a script to expose during Assess. J0 retains its small 0.3–0.9 route; do not load later cards on first-call resume.

For each attempt capture task/input, expected and observed behavior, safe output/source pointer, learner explanation, actual assistance and failure layer. Local boundary checks use synthetic fixtures without provider calls; AI quality needs separate observed cases. Supported early work is valid practice. For independent claims only `none` or `docs` counts; a hint/scaffold/example requires a different independent attempt. Select one unfamiliar task at a time, withhold its answer in Assess, and return to Learn on a help request.

Readiness means required non-transfer behavior and understanding are evidenced. Where transfer is pending, `ready` requires the protocol's single append-only readiness event carrying the evidence, eligible time, next task and trigger; it permits advancement but does not certify retention. `complete` requires every gate. The elapsed-time floor is a scheduling safeguard, never scientific sufficiency. Remediation reopens only the overlapping demonstrated prerequisite and preserves unrelated current evidence and valid artifacts.

Each assessment checks a conceptual anchor as well as output: what the mechanism owns, what deterministic application code still owns, and how evidence distinguishes the relevant failure layers. A memorized framework recipe cannot substitute for that explanation. An unfamiliar probe must change a meaningful rule, input shape, trust boundary or failure—not merely identifiers or wording.

## J1 — Medical extraction

**Prerequisite:** J0 JSON/boundary readiness; **stage gates:** execution, explanation, modification, debug; **capabilities:** E05–E07, continued E04.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Schema and extraction | Required fields/types/nulls are explicit. Valid payload passes; malformed JSON and wrong type fail locally; absent fact remains null. Learner distinguishes syntax, schema and truth. | Add a field for an explicitly stated document fact and justify its absent-value rule. | Isolate parsing versus schema validation on a hand-written payload before another model request. |
| Source checks | Exact spans resolve to the input; unsupported values are flagged. First pass requires three cases: absent fact, negated fact, unresolvable span. Uncertain language, old/current statements and instruction-like note text are added as observed notes break them, and are required before J1 completion. A schema-valid unsupported claim fails source review. | Diagnose a new mismatched span or chronology case and explain which layer owns the correction. | Trace one field to source and fix its deterministic invariant, then try a different note. |
| Review and comparison | Source and extracted values are readable together, not only present in output; a human correction retains original and corrected values/reason. The stage closes with a capture: one success, one flagged omission, one honest failure. Compare one change and a simple deterministic/non-AI baseline on fixed cases, reporting counts and denominator including omissions. | Explain a previously unseen review flag and correct it without losing provenance. | Reduce to one source/value/correction path; restore the missing audit information and rerun it. |

**Common wrong models at J1.** *"Valid JSON means the extraction is correct."* — separate the three questions out loud: it parsed, it matched the schema, and neither one looked at the note. *"The field is missing, so I'll leave it out."* — absent is a finding; null records it, omission hides it. *"The span resolved, so the fact is supported."* — a span proves the quote exists at that position, not that it supports the value; see the second case in [worked exemplars](EXEMPLARS.md).

Worked examples and scaffolds are permitted in Learn. The stage debug gate must reflect the learner's actual diagnosis, not assistant-authored repair. Independently applied skill claims need separate explanation, modification, debug and delayed transfer; J1 execution alone cannot grant them. Revisit extraction transfer in J2.

## J2 — Retail classification and transfer

**Prerequisite:** J1 source-grounded schema behavior; **stage gates:** modification, explanation, transfer; **capabilities:** E08–E09.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| New domain schema | Learner adapts known validation to category, stated order ID, missing information, draft and escalation reason. Test missing ID, ambiguous request, mixed intent and invented order status. No order system access is claimed. | Design a new bounded request category and explain which medical rules transfer and which change. | Return to one schema/value invariant; provide only the requested help, then use a fresh category. |
| Language and delay | Record Arabic and English results separately against explicit expected labels; identify untested code-switch cases. A later unfamiliar request demonstrates transfer with a changed ambiguity, language or escalation rule, recorded assistance and elapsed delay. | Adapt validation to a new request whose missing-information or escalation contract differs materially; renaming fields does not qualify. | Keep supported modification as practice, record the later task in the readiness event and continue useful work if `ready`. |

**Common wrong models at J2.** *"The model can look up the order."* — it cannot; nothing is connected yet, and a stated order ID is text the customer typed. *"Translating the labels makes it work in Arabic."* — interface language and model behaviour on Arabic input are unrelated; measure the second directly.

Start with a learner sketch; hints are available after an attempt or direct request. Same-session transfer is useful practice but cannot certify delayed retention. Do not block J3 solely to wait for retention when the ready contract is met.

## J3 — Retrieval and grounded answers

**Prerequisite:** J2 readiness and Python lists/functions plus a small vector explanation; **stage gates:** execution, explanation, modification, debug; **capabilities:** E09–E13.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Visible retrieval | Versioned document/section/chunk IDs survive ingestion. Compare a simple lexical/exact-term baseline with vectors on the same labeled questions; measure Recall@k against labeled IDs. Include a relevant passage split across a chunk boundary. | Trace an unfamiliar question to ranked passages and explain a missed expected source. | Inspect chunks/ranking before changing the answer prompt; compare one chunking choice. |
| Answers and abstention | Every citation supports its attached claim; missing, conflicting, expired and instruction-like passages produce the defined handling. Fixture checks catch nonexistent citation IDs and wrong versions. | Diagnose whether a new wrong answer came from retrieval or generation. | Freeze retrieved context, then isolate the unsupported answer claim or missing retrieval. |
| Abstraction decision | When a framework need is demonstrated, route one slice — ingestion or retrieval, not the pipeline — through LangChain, time-boxed, and name which responsibilities moved. Otherwise, compare a changed native trace with the framework contract and justify no adoption, costs and a reconsideration trigger. Either way the visible implementation stays the baseline; working code is not rewritten to match. Disclose corpus/language limits. | Predict and then trace the effect of one changed retrieval setting or boundary through the chosen path. | Trace one input through owned versus delegated responsibilities; do not add an abstraction to hide a failing step. |

**Common wrong models at J3.** *"It retrieved something, so retrieval worked."* — retrieving the superseded version of a policy is a successful retrieval of the wrong document. *"A wrong answer means the prompt needs work."* — check what was retrieved first; changing the prompt to fix a retrieval failure hides it. *"Higher similarity means more correct."* — similarity cannot see a version number or an effective date.

Allow documentation and supported learning. Do not call a framework-produced result independent understanding. Protected data is optional; if introduced, add deterministic access-scope checks before retrieving it.

## J4 — Scoped tools and approval

**Entry prerequisite:** J2 readiness for hand-written parameterized SQL and the scoped read tool. **Completion prerequisite:** J3 retrieval readiness for the combined policy/order behavior. **Stage gates:** execution, explanation, modification, debug; **capabilities:** E14–E17.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| SQL and read tool | Expected query rows match. Trusted caller scope controls `get_order`; own order passes, wrong-customer and missing-order queries fail safely. Invalid/injected arguments never broaden scope. | Diagnose a new cross-customer lookup without relying on prompt wording. | Run the fixed query directly against two synthetic customers and trace the trusted scope. |
| Native loop | Validate arguments, link tool result to its call identity, bound steps and expose tool exceptions. Test missing tool, invalid arguments and exhausted step budget without false success. | Trace and repair an unfamiliar tool-result or stopping failure. | Isolate one proposal/validated call/result cycle with a fake tool before model integration. |
| Approval state | Before any simulated effect, bind approval to immutable proposal ID/version or digest, trusted actor, target and exact parameters. Test mutation after approval, changed actor, changed target, stale version, rejection, missing approval and replay; all rejected paths produce zero effects. Approved original executes once. | Diagnose a replay or changed-parameter proposal and justify the execution-time check. | Use a local transition fixture and effect counter; repair binding/consumption before another workflow run. |
| State abstraction decision | Adopt LangGraph only when checkpoint, branch or recovery needs are demonstrated, and keep it to the transitions; otherwise justify no adoption by comparing ownership, complexity and a concrete trigger. Explain what the framework holds versus what the application owns. The same rejection and once-only cases hold either way, and a working approval binding is never traded for a graph. | Change a transition and trace how the chosen design preserves the approval contract. | Trace application-owned state separately from any framework persistence. |

**Common wrong models at J4.** *"The model said the customer ID, so I can query it."* — a model-supplied identifier is an argument, never authorization; scope comes from the trusted caller. *"The user replied 'approved', so it is approved."* — approval binds to a proposal identity, not to text; see the J4 exemplar. *"The tool returned an error, so I'll say the order was not found."* — a failure and an absence are different results and the learner must not collapse them.

Assistance is recorded; deterministic acceptance cases begin when each boundary is introduced, before model integration. No live refunds or outbound messages. A local once-only demonstration does not prove distributed concurrency or production recovery.

## J5 — Independent delivery

**Prerequisite:** medical J1 and retail J4 outcomes with valid prerequisite evidence; **stage gates:** execution, explanation, modification, debug, transfer; **capabilities:** E18–E22 plus route coverage.

| Increment | Observable outcome and minimum acceptance cases | Unfamiliar ownership probe | Remediation |
|---|---|---|---|
| Reproducible interface | Each product runs from documented locked dependencies and exposes a small API/interface. Invalid request/response, provider timeout and suitable bounded retry have understandable outcomes. Existing schema/span/scope/approval checks still pass. | Make a bounded unfamiliar interface change and explain the request-to-result path. | Reproduce the failing boundary locally; repair only the missing mechanism before reassessing on a new case. |
| Honest evaluation | Freeze held-out expectations before use; report counts, denominator, model/config/date, critical failures and unmeasured cost/latency as unknown. Disclose tuning contamination and repeated-case variability. | Diagnose an unfamiliar failure and defend one design tradeoff from actual evidence. | Separate deterministic failure from model behavior; fix the report or mechanism and use a fresh assessment case. |
| Ownership and handoff | Runnable demos, readable READMEs and contribution disclosure match actual artifacts. Learner explains architecture, changes and debugs independently, then performs delayed unfamiliar transfer. | Transfer a delivery change to the other product after the eligible delay with normal docs allowed. | Preserve the assisted result as learning work; return to Learn if requested and schedule a different independent attempt. |
| Lightweight usability | One person other than the builder attempts a small normal task from the README/interface when practical. Capture task, observed hesitation/failure and one correction or explicit deferral; do not script their success. | Explain which observed behavior supports the change and what remains untested. | Narrow to one discoverability or error-message task; never substitute tutor-generated opinion for an observation. |

J5 explanation, modification, debug and transfer gates require assistance `none` or `docs`; execution may use supported code. Generated code, worked examples and answer-shaped hints cannot satisfy final ownership. J5 `ready` requires E01–E22 at least `practiced` and supports useful next work while transfer is queued. Final route completion requires all gates and E22 `applied_independently` or the stronger `production_understanding`. Inspect cross-stage failures and reconcile independent claims explicitly. No test count, portfolio polish or elapsed time alone establishes employment or production readiness.

Readiness advancement, its append-only maintainer decision, the grounded review queue, historical-readiness rules and final J5 completion are defined once in [the progress protocol](PROGRESS_PROTOCOL.md). That machinery is teaching administration, not learner competence, and it is not part of the lesson the learner sees.
