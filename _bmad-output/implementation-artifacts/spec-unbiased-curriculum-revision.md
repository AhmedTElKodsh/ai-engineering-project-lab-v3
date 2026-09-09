---
title: 'Loosen curriculum routing and strengthen learning evidence'
type: 'refactor'
created: '2026-09-08'
status: 'in-progress'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: '7d527c20198c426d501cd237858e1bc2dcd5f7f2'
context: ['{project-root}/AGENTS.md', '{project-root}/docs/TEACHING_GUIDE.md']
---

<frozen-after-approval reason="User requested implementation after the unbiased curriculum review">

## Intent

**Problem:** The curriculum's default sequence is enforced as a universal prerequisite chain, narrow failures can supersede unrelated evidence at stage level, and detailed progress administration is more precise than the rubrics used to judge understanding. Framework rewrites and AI-only comparisons can also become completion ceremony rather than evidence of sound engineering judgment.

**Approach:** Keep J0-J5 as the recommended narrative while permitting dependency-safe branches, scope evidence freshness by capability overlap, make one readiness event own its delayed-practice contract, and improve assessment validity with conceptual anchors, meaningful transfer differences, simple baselines, earlier unseen cases, adaptive lesson sizing, and lightweight usability evidence.

## Boundaries & Constraints

**Always:** Preserve the append-only evidence log, initial J0/Q0/0.3 state, learner ownership rules, synthetic-data limits, current valid evidence, honest assistance records, and deterministic safety boundaries. Keep the combined policy-and-order workflow dependent on both retrieval and tools even when the initial SQL/tool slice can branch earlier.

**Never:** Award learner progress from this maintenance work, edit either learner application, call a provider, weaken J5 independent delivery, require a framework without a demonstrated learning or role need, or convert the route into an unstructured menu.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Scoped reassessment | Passing J3 retrieval explanation followed by failed E13 framework explanation | Retrieval evidence remains current; E13 and dependent work reopen | Require correction only for overlapping capability tags |
| SQL branch | J2 ready; J3 incomplete | Learner may begin direct SQL and scoped read-tool work | Combined policy/order behavior still waits for J3 |
| Delayed readiness | Non-transfer gates pass and transfer is pending | One readiness event records eligibility, task and trigger | Reject missing, premature or stale readiness evidence |
| Framework decision | Native mechanism works and no framework need is demonstrated | A justified trace/no-adoption comparison can satisfy abstraction literacy | Record the tradeoff; do not require a duplicate implementation |

</frozen-after-approval>

## Code Map

- `tools/validate_workspace.py` -- evidence freshness, route prerequisites, readiness, provider-state shape, and 92 embedded fixtures; extend rather than replace the validator.
- `docs/PROGRESS_PROTOCOL.md` -- normative evidence and checkpoint contract; simplify duplicate readiness bookkeeping and define capability-scoped freshness.
- `docs/CURRICULUM.md` -- J0-J5 route, stage dependencies, framework comparisons, baselines, unseen cases, timeout awareness and usability work.
- `docs/ASSESSMENT_CARDS.md` -- learner-understanding rubrics, meaningful transfer variation, conditional framework evidence and usability acceptance.
- `docs/TEACHING_GUIDE.md` -- adaptive learner action size and optional first-exposure presentation components.
- `docs/ENGINEERING_GUIDE.md` -- non-AI baselines, request budgets, conditional abstraction comparisons and early blinded evaluation.
- `docs/PORTFOLIO.md` -- small observed usability task and explicit applied-LLM specialization boundary.
- `.agents/skills/ai-engineering-tutor/SKILL.md`, `AGENTS.md`, `README.md` -- align routing summaries with the revised policy without loading later material during J0.
- `progress/current.json`, `progress/skills.json`, `progress/evidence.jsonl`, `curriculum/**` -- preserve bytes and all learner status.

## Tasks & Acceptance

**Execution:**
- [ ] `tools/validate_workspace.py` -- add dependency-aware entry/completion rules, overlap-scoped freshness, single-event readiness and exact provider version keys with focused positive/negative fixtures.
- [ ] `docs/PROGRESS_PROTOCOL.md` and routing summaries -- describe the implemented state model once and remove conflicting duplicated policy.
- [ ] `docs/CURRICULUM.md`, `docs/ASSESSMENT_CARDS.md`, `docs/TEACHING_GUIDE.md` -- revise sequencing and assessment without increasing first-lesson load.
- [ ] `docs/ENGINEERING_GUIDE.md`, `docs/PORTFOLIO.md`, tutor skill and README -- align engineering judgment, usability and specialization expectations.
- [ ] Verification artifacts -- record current commands and limits without creating learner evidence.

**Acceptance Criteria:**
- Given a later failure tagged only to a different capability, when a prior gate reference is validated, then the unrelated passing evidence remains current.
- Given J2 readiness and incomplete J3, when J4 SQL/tool work begins, then the state is valid; J4 completion still requires J3 retrieval readiness.
- Given transfer is pending, when readiness is recorded, then the append-only readiness event alone carries a valid eligible time, next task and trigger.
- Given a native implementation has no demonstrated framework need, when abstraction literacy is assessed, then a justified comparison or no-adoption decision can qualify.
- Given the unchanged initial checkpoint, when native validation runs, then all learner skills remain unawarded and both native checks pass.

## Implementation Notes

- The user explicitly approved implementation after rejecting an authority-bound review. Treat prior documents as changeable design inputs.
- The earlier first-prompt finding is retracted as a launch blocker; improve the assessment with a changed trace or prediction instead.
- Corrected the baseline metadata before review after the initially entered full SHA failed to resolve; the canonical `git rev-parse HEAD` value is recorded above.

## Spec Change Log

## Review Triage Log

## Design Notes

Route entry and route completion have distinct dependencies. J4 entry requires J2 so direct SQL and scoped read tools can proceed; J4 completion requires J3 because the finished retail workflow combines order facts with retrieved policy. Evidence freshness is superseded only by a later event sharing the same milestone, kind and at least one capability tag; untagged evidence remains milestone-wide.

## Verification

**Commands:**
- `python tools/validate_workspace.py` -- expected: native state and owned documents pass.
- `python tools/validate_workspace.py --self-test` -- expected: all existing and new semantic fixtures pass.
- `python -m py_compile tools/validate_workspace.py` -- expected: no syntax error.
- `git diff --check` -- expected: no whitespace errors.
- preservation comparison for `progress`, `curriculum`, and vendor skills -- expected: no unintended changes.
