---
title: 'Align curriculum readiness, evidence enforcement and tutor behavior'
type: 'bugfix'
created: '2026-09-08'
status: 'done'
baseline_commit: 'd6f8e51a582c45c16cace04696074e70ed800de2'
route: 'dispatch'
review_loop_iteration: 1
context: ['{project-root}/AGENTS.md', '{project-root}/docs/TEACHING_GUIDE.md']
---

<frozen-after-approval reason="User approved all nine review refinements in this conversation">

## Intent

**Problem:** The curriculum describes independent delivery and evidence-led teaching, but stage completion can accept heavily supported work, invalidated prerequisite history and unreconciled skill failures. Delayed-transfer gates can unnecessarily block useful learning; later stages lack compact assessment contracts and several technical boundaries need explicit acceptance cases.

**Approach:** Implement all nine approved refinements as one readiness correction: strengthen evidence enforcement, separate advancement readiness from retention certification, supply tutor-facing assessment cards, specify JSON and approval boundaries, introduce tests with their mechanisms, and retain auditable independent tutor simulations.

## Boundaries & Constraints

**Always:** Preserve actual learner evidence and initial pending state. Keep supported early learning valid. Require independent final ownership evidence and meaningful capability coverage. Retain downstream artifacts after reassessment without allowing invalid evidence to support completion. Keep native documents and tutor routing coherent. Make simulations explicitly synthetic and separate from learner progress.

**Never:** Edit learner apps, award achievements from this work, call providers, store sensitive data, alter archived curriculum or vendor skill definitions, publish or deploy. Existing vendor maintenance limitations are documented, not repaired in this scope.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Supported final delivery | J5 ownership uses worked examples | Reject independent final claim | Name unsupported gate |
| Missing coverage | Complete route with all skills not started | Reject final completion | Name missing capability evidence |
| Invalid prerequisite | Correction invalidates earlier prerequisite evidence | Cannot justify downstream completion | Retain artifacts, reopen affected claims |
| Genuine regression | Valid historical prerequisite followed by failure | Preserve supported downstream history | Return to prerequisite needing review |
| Cross-stage failure | New failure tagged to previously independent skill | Require explicit reconciliation before retaining claim | Downgrade or document scoped retain decision |
| Pending retention | Current readiness demonstrated; delayed transfer queued | Permit next useful stage without certifying retention | Reject absent or ungrounded review queue |
| Midnight transfer | New date only minutes after practice | Does not certify delayed retention | Keep practice evidence without promotion |
| Structured output | First JSON experiment | Explicit JSON Object Mode plus local validation, current capability check | Surface invalid/schema/source failures separately |
| Changed approval | Approved proposal mutated, replayed, or used by other caller | Deterministic rejection in J4 acceptance contract | No simulated effect |

</frozen-after-approval>

## Code Map

- `tools/validate_workspace.py`: standard-library validator, embedded synthetic fixtures, current history and assistance checks; reuse read-only validation and append-only evidence model.
- `docs/PROGRESS_PROTOCOL.md`: authoritative evidence schema and promotion policy; update alongside validator.
- `docs/CURRICULUM.md`, `docs/TEACHING_GUIDE.md`, `docs/ENGINEERING_GUIDE.md`: route, pedagogical cadence and engineering depth; keep J0 small.
- `docs/PROVIDER_REFERENCE.md`: dated first-call baseline; add separately dated structured-output decision without asserting learner runtime verification.
- `.agents/skills/ai-engineering-tutor/SKILL.md`, `AGENTS.md`, `AGENT.md`: native routing and pointer; preserve maintenance/teaching separation and singular pointer.
- `docs/PILOT.md`, `docs/VALIDATION_REPORT.md`: simulation protocol and bounded verification; retain actual case artifacts under `_bmad-output`.

## Tasks & Acceptance

**Execution:**
- [x] `tools/validate_workspace.py`, `docs/PROGRESS_PROTOCOL.md` -- implement ownership, coverage, correction, reconciliation and retention rules together with positive/negative regression fixtures.
- [x] `docs/ASSESSMENT_CARDS.md` -- define observable outcomes, prerequisites, acceptance cases, assistance, unfamiliar tasks and remediation for J1-J5; load only active card.
- [x] `docs/CURRICULUM.md`, `docs/TEACHING_GUIDE.md`, tutor skill and `AGENTS.md` -- link cards and distinguish readiness from retained independence.
- [x] `docs/PROVIDER_REFERENCE.md`, `docs/ENGINEERING_GUIDE.md`, curriculum -- specify JSON mode, immutable approval identity and early focused tests.
- [x] `docs/PILOT.md`, simulation artifacts and `docs/VALIDATION_REPORT.md` -- execute independent bounded scenarios, evaluate their actual outputs, report limitations and fresh checks.

**Acceptance Criteria:**
- Given the unchanged initial learner state, when native checks run, then validation passes without installing or executing learner apps.
- Given the edge cases above, when candidate checkpoints are tested in memory, then unsafe claims fail and legitimate supported learning remains accepted.
- Given a tutor in a fresh isolated context, when each simulation is presented, then routing, explanation, ownership, relocation and redaction behavior follow the native contract with inspectable outputs.
- Given the completed maintenance diff, when preservation is checked, then progress, archived sources and vendor definitions match the original tree.

## Implementation Notes

- User authorization is the preceding review and explicit request to proceed with all refinements; no additional scope approval is needed. Changes are local and reversible. No external side effects are required.
- Implementation adds `ready` only for milestones awaiting transfer with grounded queues. J5 execution can be supported; four ownership gates require none/docs. All E skills must be practiced for J5 readiness; E22 requires independence for completion. The 24-hour/date-only two-day floor is a conservative scheduling policy, not scientific sufficiency.
- Root inspected the code/docs and ran 66 fixtures. Nine fresh tutor contexts plus a fresh maintenance retest were evaluated; responses and limits are retained outside learner evidence. One metadata-inventory defect was corrected by tightening capture instructions, not by inventing a successful original run.
- Final root verification: 92 fixtures pass with 19 local documents. Independent verification review confirmed the four ownership guards, E22 guard, date-only floor and historical readiness chronology are individually protected by mutation-detecting fixtures. Independent edge review confirmed the remaining chronology finding resolved. Retention and final-completion tutor cases were rerun in fresh contexts after the policy correction and passed.
- Preservation: `git diff --exit-code d6f8e51a582c45c16cace04696074e70ed800de2 -- progress curriculum .agents/skills ':(exclude).agents/skills/ai-engineering-tutor'` returned 0. All 22 core skills remain unawarded and current state remains J0/Q0/0.3 with an unverified app location. No provider, publication or deployment action occurred.

## Spec Change Log

- Frozen review exposed historical-readiness ambiguity: live queues cannot both track current evidence and serve as immutable prior authorization. Add an append-only maintainer readiness decision grounded in then-current passing non-transfer evidence and its review task; current readiness and downstream history must reference it. Preserve the existing initial learner state, supported execution exemption, queue requirement, original acceptance intent and all valid simulations. This is evidence bookkeeping, not new learner achievement.
- Final route completion must require all initial milestones complete. Verify explicit E/Q collection membership and isolate each new ownership/coverage condition in tests. Use canonical dates or timestamps and calendar-date comparison for mixed precision. Preserve valid reconciliation history after resolution and bound decision dates to the snapshot.

## Review Triage Log

| Reviewer finding | Verdict | Evidence and disposition |
|---|---|---|
| Blind 1: J5 complete with earlier retention pending | high | Existing positive fixture ends J5 complete/J2 ready. Fix final route condition; use J3 for advancement fixture. |
| Blind 2: E row moved to later_modules bypasses coverage | high | Combined ID validation does not validate partitions. Enforce exact E/Q collection membership and explicit E coverage. |
| Blind 3: recovered prerequisite backfills invalid history | medium | Current complete shortcut skips prior evidence timing. Check historical prerequisites for started claims even after recovery. |
| Blind 4: live queue can authorize work retrospectively | medium | Queue has no durable decision chronology. Record append-only readiness decisions before downstream work. |
| Blind 5: historical queue becomes stale after regression | medium | Root reproduced both failure branches with/without old queue. Separate historical readiness from current queue. |
| Blind 6: resolved reconciliation must be deleted | medium | Root reproduced rejection after passing reassessment while retaining valid prior decision. Preserve audit rows. |
| Blind 7: malformed queue/reconciliation entry errors | low | CLI catches AttributeError, so the claimed CLI escape is false; direct validation still benefits from a normal ValueError. Add object guards and negatives. |
| Blind 8: mixed date/timestamp rejection | medium | 36 hours can span the specified two dates. Implement documented calendar comparison when either value is date-only. |
| Blind 9: basic ISO date bypass | medium | Length detection treats basic dates as timestamps. Enforce canonical representation. |
| Blind 10: future reconciliation supports present snapshot | medium | No upper bound on decision time. Reject decisions after snapshot update time. |
| Edge 1: basic ISO date bypass | medium | Same demonstrated date-format defect; grouped with Blind 9. |
| Edge 2: mixed-precision delay | medium | Same demonstrated calendar comparison defect; grouped with Blind 8. |
| Edge 3: readiness history after failure | medium | Same reproduced stale-queue defect; grouped with Blind 5. |
| Verification 1: ownership fixture has unrelated E22 rejection | medium | Reviewer disabled ownership guard and all 66 tests passed. Add isolated gate fixtures plus mutation verification. |
| Verification 2: E22 condition untested independently | medium | Reviewer removed dedicated check and all fixtures passed. Add practiced-only E22 completion rejection. |
| Verification 3: one-day date-only floor unprotected | medium | Reviewer weakened delay helper and suite remained green. Add canonical/mixed boundary fixtures and ready queue checks. |
| Edge follow-up: earliest gate masks later work after prerequisite failure | medium | Reproduced old J3 execution/explanation plus new J3 debug after J2 failure. Fixed by checking each claimed observation separately; dedicated rejection fixture passes and reviewer confirmed resolution. |

All retained findings above were resolved in this maintenance change. No new finding was deferred. Existing vendor runtime replacement/renderer limitations remain outside this refinement change, as recorded in repository maintenance guidance. Verification establishes bounded checkpoint/tutor behavior only.

## Verification

- `python tools/validate_workspace.py` -- native state and owned documents pass.
- `python tools/validate_workspace.py --self-test` -- existing and added semantic fixtures pass.
- `git diff --check` -- no whitespace defects.
- Independent frozen-diff review and tutor simulations -- concrete failures resolved or explicitly reported; never treated as learner evidence.
