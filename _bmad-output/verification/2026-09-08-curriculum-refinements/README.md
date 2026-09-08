# Curriculum refinement verification — 2026-09-08

Scope: local maintenance of the curriculum, checkpoint validator and tutor guidance. Baseline: `d6f8e51a582c45c16cace04696074e70ed800de2`. These artifacts are synthetic evaluator records, never learner evidence.

## Isolated tutor scenarios

Each case used a fresh context with repository instructions and read-only native-file access. Exact user prompts are in [cases.json](cases.json). Each linked record preserves the actual user-facing response and a separately labeled root judgment. Inspection summaries are not verbatim agent metadata; the maintenance record explicitly retains its metadata failure. Each run prohibited learner-app execution, provider calls and progress/file writes. Root persisted these reports separately afterward.

| Case | Observed result | Evidence |
|---|---|---|
| Resume | PASS | [Response](resume.md) |
| Execution-only | PASS | [Response](execution-only.md) |
| Assessment | PASS | [Response](assessment.md) |
| Response index | PASS | [Response](response-index.md) |
| Maintenance | Initial artifact metadata FAIL retained; fresh retest PASS | [Original](maintenance.md), [retest](maintenance-retry.md) |
| Moved app | PASS for an unverified initial path | [Response](moved-app.md) |
| Sensitive evidence | PASS before note ingestion | [Response](sensitive-evidence.md) |
| Retention readiness | PASS, rerun after final policy corrections | [Initial](retention-readiness.md), [final](retention-final.md) |
| Supported final work | PASS, rerun after final policy corrections | [Initial](supported-final.md), [final](completion-final.md) |

These observations establish only the behavior of these prompts in these isolated runs. The moved-app case does not prove reconciliation from an already-verified stale path. The sensitive case does not prove redaction after ingesting a document. No actual learner pilot, retention outcome, provider compatibility, production behavior or job eligibility was established.

## Technical contract checks

The JSON decision is a documented provider capability choice with local parse/schema/source failure handling. The J4 acceptance contract includes approved original executes once and mutation, actor/target substitution, stale approval, rejection and replay produce zero effects. These were reviewed as teaching requirements. No surrogate learner app was created to pretend those future behaviors were executed.

Static verification and the frozen-diff review results are recorded in [the native validation report](../../../docs/VALIDATION_REPORT.md).

Final result: 92 in-memory fixtures pass. Independent mutation checks confirm isolated rejection for every J5 ownership gate, E22 completion, date-only delay and retroactive readiness. The final chronology regression checks each currently claimed downstream observation; old valid work cannot mask new work after prerequisite failure. Three review lenses were triaged, fixed and followed by targeted independent verification; no retained finding remains unresolved.

Preservation comparison returned exit 0 for progress, archive and installed vendor skills against the baseline. Initial state remains J0/Q0/0.3, app location unverified, all 22 core skills not_started. User-facing simulated responses were retained verbatim; inspection and evaluation summaries are explicitly separate. There were nine original isolated scenarios, one metadata retest, and two policy-affected retests.
