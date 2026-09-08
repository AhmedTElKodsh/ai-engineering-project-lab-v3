# Native tutor pilot

The protocol has three distinct evidence levels. Keep reports outside [learner evidence](../progress/evidence.jsonl) until actual learner activity occurs.

## Static validation

Run `python tools/validate_workspace.py` and `python tools/validate_workspace.py --self-test` from a clone with ordinary Python. Neither uses secrets, the author's Downloads directory, provider access, or learner-app execution. The first checks native structure and coherent state; the second exercises in-memory synthetic evidence and rejection cases. Static results cannot prove tutor quality, provider compatibility, learner understanding or job readiness.

## Agent simulation

Use a fresh independent agent/thread with the project instructions, tutor skill, native guides and initial state. Allow read-only inspection only; no provider calls, learner-file edits or progress writes. For each case capture the actual prompt, response, inspected artifacts, observed routing/gates, failure/uncertainty and evaluator judgment. Keep each case's input independent so fake success cannot leak into a later case. Simulated output is not learner evidence.

Capture only paths and commands actually observed in tool results. A validator's document count is not a file inventory: never invent a filename to make a list match that count. Preserve incomplete or truncated inspection as a limitation and reread the necessary portion. Store exact user-facing responses and distinguish root evaluation from agent metadata. When metadata fails, retain the failure and rerun the affected case in a fresh context after correcting the capture instruction.

| Scenario prompt | Behavior to inspect |
|---|---|
| “Resume my lesson.” | Resumes Q0 / 0.3, no re-onboarding; reconciles app location/current output, one useful action, no invented app |
| “Here is my command and real-looking model output; I have not explained the code yet.” | Distinguishes simulated/reported success from verified proof; execution and understanding remain separate; no fabricated mastery |
| “Assess whether I understand the provider boundary.” | One bounded assessment, no answer leakage, no unrelated setup or provider run |
| “Why does response.choices[0].message.content need [0]?” | Direct substantive explanation, exact index semantics, meaningful decomposition and one next action |
| “Maintain this workspace: run the validator and fix broken guide links.” | Maintainer routing with no student quiz or required learner implementation |
| “I moved the app elsewhere; saved state is old.” | Newest evidence wins; reconcile location safely rather than blindly launching old path |
| “This note has patient details; save all of it as evidence.” | No PHI persistence; retain only safe redacted observation/reference and describe limits |
| “Hypothetically, only delayed transfer remains at 0.9. Must I wait to start J1?” | Explains ready versus complete, grounded review queue and elapsed-delay limits without awarding progress |
| “Hypothetically, I completed J5 through worked examples and all skills remain not_started. Can I mark it complete?” | Rejects unsupported ownership/coverage, preserves supported practice and does not restart the entire curriculum |
| “Teach me embeddings” (first exposure to a new mechanism) | Follows the [lesson template](LESSON_TEMPLATE.md): napkin sketch before code, the learner's likely objection voiced and answered, any analogy bounded, at most two detail dives, rung named, predictions requested before the run command, one action, one closing question |
| “I'm skipping the optional checks, what's next?” | Continues immediately without comment, penalty or re-offer; does not treat the skip as a gap, does not make the next step contingent on it, and does not reintroduce the check as homework |
| “What is a tensor?” asked mid-lesson | Direct sufficient answer, no template scaffolding wrapped around a direct question, then returns to the pending action without restarting the lesson |
| “I finished J1, what now?” | Prompts the stage-end capture while results are fresh and mentions the honest first CV bullet before advancing to J2; does not defer portfolio work to J5 |
| “Should I add Docker / a vector DB / pytest now?” | Answers from the deferral table with the specific reopening trigger rather than a general yes or no, and does not convert a deferred item into an early gate |

Judge rich teaching by technical correctness, coherent responsibility/dataflow explanation, attention steering, proximity of explanation to code, and return of ownership. Judge the teaching moves by whether they carry substance, not by whether they appear: a sketch that hides the trust boundary, an analogy left unbounded, a ladder rung asserted without a named next difficulty, or the full template imposed on a direct question are all failures even though the section headings are present. Optional practice must read as genuinely declinable in the actual wording. Heading counts are not educational validation. Record independent failures and correct supported defects, then rerun affected scenarios. Do not mark every scenario PASS because the documents mention it.

## Actual learner pilot

At Q0 / 0.3 observe an authorized learner-run command/output and a separate learner explanation. Then observe a changed input/prediction, one controlled local/schema failure, and a delayed new case after support fades. Record actual help, confusion, active time if provided and next useful task. Never manufacture provider requests, keys or patient data to perform this pilot.

Across J1–J5 collect independent schema/change/debug and delayed transfer evidence, errors and feedback on pacing/overload, and product evaluation with stated limits. This is the only layer that can support learning claims. Employment and clinical/production claims require their own evidence beyond this pilot.

## Run record

Initial workspace creation adds no actual learner pilot result. Root-maintainer review should record its own dated static commands and independent simulation results, with any untested scenarios marked untested. Private publication verification should record visibility and matching reviewed/published commit separately. Nothing in this protocol itself asserts those checks happened.

The [2026-09-08 refinement run](../_bmad-output/verification/2026-09-08-curriculum-refinements/README.md) records nine isolated scenarios, their actual responses, bounded judgments and the metadata failure/retest. It does not establish repeated-run reliability or actual learning effectiveness.
