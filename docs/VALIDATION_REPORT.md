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
