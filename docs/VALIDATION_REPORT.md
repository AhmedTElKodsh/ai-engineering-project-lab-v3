# Native workspace validation report

Date: 2026-09-08. Scope: Codex learner workspace configuration and its authored evidence validator. This report does not award learner progress.

## Local verification

- `python tools/validate_workspace.py --self-test`: PASS for native state, evidence relationships, 17 owned documents, and 45 synthetic positive/negative fixtures.
- Skill Creator `quick_validate.py`: PASS for `ai-engineering-tutor` metadata and structure.
- `python -m py_compile tools/validate_workspace.py` and `git diff --check`: PASS.
- Publication scan: 317 candidate files, zero findings for its defined GitHub/provider/AWS/private-key patterns. This is a bounded known-pattern check.
- Four isolated agent simulations passed lesson resume, success-only gating, assessment, and maintainer routing. They made no writes or provider calls and are not a real learner pilot.

## Independent review triage

| Finding | Verdict and resolution |
|---|---|
| Evidence freshness ignored skill scope | Patched. Skills use latest evidence per skill, milestone, and kind; milestone gates retain milestone-level precedence. |
| Assistant-written explanations could satisfy understanding | Patched. Explanation, modification, debug, and transfer gates reject `ai_implemented` evidence. |
| Delayed milestone transfer was not enforced | Patched. Transfer-bearing milestones require a later calendar date than passing modification practice. |
| Skills snapshot could be saved partially | Patched. Both snapshots carry and validate the evidence log revision and timestamp. |
| Resume context fields could disappear | Patched. Required onboarding, provider, conceptual, assistance, blocker, retrieval, and expected-evidence fields are type checked. |
| Location used free-form substring matching | Patched. Location evidence has an explicit `observed_path` compared after Windows path normalization. |
| Empty conversation or turn references passed | Patched. Trace references require a nonempty identifier. |
| Reassessment erased downstream history | Patched. The active checkpoint returns to the reopened prerequisite while downstream evidence is retained only with earlier prerequisite history. |
| Broken Markdown anchors passed | Patched. Owned Markdown file and same-file anchors are validated. |
| Malformed spec front matter crashed | Patched. Front matter has a guarded parse and negative fixture. |
| Source artifact checks were bypassed by self-tests | Patched. All state fixtures run with the repository root; explicit valid, missing, absolute, and escaping references are exercised. |
| BMAD Windows runtime replacement can fail with WinError 183 | Confirmed inherited vendor issue; deferred and documented in repository maintenance guidance. Initial setup succeeded. |
| Materialized BMAD renderer tests expect absent source assets | Confirmed inherited vendor test-suite mismatch; deferred and documented. Native workspace validation remains independent. |

## Evidence boundary

Static checks establish repository consistency and the intended teaching gates. They do not establish an actual Groq call, installed provider versions, learner understanding, teaching effectiveness, clinical validity, production readiness, or job readiness. The saved learner state therefore remains at J0 / Q0 / 0.3 with execution and explanation pending.

## Publication

The workspace was published to the authenticated user's `ai-engineering-project-lab-v3` repository with private visibility. The final `main` reference was compared with the clean local checkout after this report and completion status were committed.

## Curriculum readiness refinements — 2026-09-08

This subsequent maintenance pass implements the nine approved technical/pedagogical review refinements. It is local work; the earlier publication statement above does not mean these changes were uploaded.

- Native validator and self-test: PASS, 19 local documents and 66 in-memory fixtures at the implementation checkpoint. The local count includes an existing ignored spec memlog; it is not a portable inventory guarantee.
- New fixtures cover readiness queues, midnight versus elapsed delay, invalidated prerequisite history, cross-stage reassessment/reconciliation, independent J5 ownership, capability coverage and supported execution.
- [Nine isolated tutor scenarios](../_bmad-output/verification/2026-09-08-curriculum-refinements/README.md) exercised original routing cases plus retention-readiness and unsupported final completion. All user-facing behaviors passed. One metadata-inventory failure was retained, the capture rule corrected, and a fresh maintenance retest passed.
- JSON mode and immutable approval binding are now explicit teaching/acceptance contracts. No learner implementation or provider behavior was exercised to validate these future contracts.
- Learner progress remains actual-evidence-only. No actual learner pilot, provider execution, clinical validity, production readiness or job eligibility is established by these refinements.

Final frozen-diff review and completion checks are recorded in the [refinement implementation record](../_bmad-output/implementation-artifacts/spec-curriculum-readiness-refinements.md).

Final verification after review corrections: **PASS, 92 fixtures and 19 local documents**. Three independent review lenses identified additional history, date, partition and test-isolation defects; the retained findings were fixed. Follow-up reviews verified mutation sensitivity and per-observation prerequisite chronology. The two tutor cases affected by durable readiness/final-route semantics were rerun in fresh contexts and passed. Progress, archive and vendor preservation comparison against the baseline returned exit 0. No new findings were deferred; no provider calls or remote operations occurred.

## Unbiased curriculum revision — 2026-09-08

- `python tools/validate_workspace.py`: **PASS**, native state, evidence relationships and 19 owned documents.
- `python tools/validate_workspace.py --self-test`: **PASS**, 102 in-memory positive/negative fixtures, including capability-overlap freshness, dependency-safe J4 entry, J3-gated J4 completion, single-event readiness, exact provider-version keys and the conditional framework contract.
- `python -m py_compile tools/validate_workspace.py` and `git diff --check`: **PASS**.
- `progress/`, `curriculum/`, `_bmad/` tracked sources and installed BMAD skill directories other than the intentionally revised project tutor remained unchanged from local `HEAD` `7d527c20198c426d501cd237858e1bc2dcd5f7f2`.

These are read-only/static maintenance results. They do not award learner evidence, execute either learner application, call a provider, validate teaching effectiveness, or establish job, clinical or production readiness. The implementation spec records baseline `7d527c26160c381740739bde323a61691082fc53`, which is unavailable in this checkout; no historical comparison to that object was possible.
