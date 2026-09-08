# Isolated tutor simulation: maintenance retest

Synthetic maintainer evaluation; not learner evidence. Agent: `/root/sim_maintenance_retry`. Date: 2026-09-08. Same exact `maintenance` prompt from cases.json; fresh context additionally read the corrected pilot capture rule.

## Actual response

Both maintenance checks passed:

- `python tools/validate_workspace.py` — passed native state, evidence relationships, and 19 owned documents.
- `python tools/validate_workspace.py --self-test` — passed all 66 in-memory positive/negative fixtures.

The validator checks local Markdown link targets and heading anchors in its native document scope; it found no broken guide links. External HTTP/HTTPS links are skipped and were not checked.

No files or learner progress were changed. These are static workspace results; they do not establish learner understanding, provider compatibility, or teaching effectiveness.

## Inspection and limits

Directly inspected AGENTS.md, tutor SKILL.md, PILOT.md and validate_workspace.py (search matches and two slices). Executed both stated Python commands, Get-Content and rg; all returned exit 0 with no truncation. Metadata explicitly declined to infer the file inventory from the count. No writes, learner app execution or provider calls.

## Root evaluator judgment

PASS for user-facing maintenance and exact metadata boundary. The original inventory defect remains recorded in maintenance.md. The root independently traced the nineteenth local item to an existing ignored `.memlog.md` under the spec folder; it was not a missing implementation-plan file. Counts describe this local tree and may differ in a clean clone without ignored metadata. This single retest does not demonstrate repeated-run reliability.
