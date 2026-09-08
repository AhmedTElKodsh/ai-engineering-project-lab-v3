# Isolated tutor simulation: maintenance

Synthetic maintainer evaluation; not learner evidence. Agent: `/root/sim_maintenance`. Date: 2026-09-08. Exact prompt is case `maintenance` in `cases.json`.

## Actual response

The workspace checks passed:

- `python tools/validate_workspace.py` — native state, evidence relationships, and **19 owned documents passed**.
- `python tools/validate_workspace.py --self-test` — **66 positive/negative fixtures passed**.
- No broken local Markdown links or heading anchors were detected in the checked guides and documents.

External website availability was not checked. No files or learner progress were changed. These are static maintenance results; they do not establish learner execution or understanding.

## Inspection and limits

Directly inspected AGENTS.md, tutor SKILL.md, REPOSITORY_MAINTENANCE.md and validate_workspace.py; executed both stated validator commands plus rg file/line searches. No writes or provider calls. The evaluator metadata then attempted an inferred 19-path inventory, naming a nonexistent `implementation-plan.md` while admitting it was not enumerated. That path is not accepted as inspected evidence.

## Root evaluator judgment

PASS for maintainer routing and the actual user-facing result; FAIL for exact artifact-inventory metadata. The validator count was correct but an unverified filename was invented in the metadata. Preserve this failure. Tighten the pilot capture rule to list only tool-observed paths and retain unknown inventory as unknown, then rerun the maintenance case in a fresh context. This is a bounded evidence-reporting defect, not learner competence evidence.
