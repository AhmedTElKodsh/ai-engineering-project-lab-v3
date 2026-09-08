# Portable progress protocol

This document owns evidence/status rules adapted from V3.2 sources 02 and 03. [Current state](../progress/current.json) owns the active action; [skills](../progress/skills.json) owns competence; [evidence](../progress/evidence.jsonl) is append-only factual history. [Teaching](TEACHING_GUIDE.md) owns modes. Curriculum edits, generated code and static checks never create learner achievements.

## Resume and reconcile

Prefer newest actual learner evidence in the turn, then conversation, saved checkpoint, and saved state. Start with the latest event and unresolved action. Initial onboarding is inherited as complete and calibration sufficient; this is a continuity decision, not proof of installed packages or competence. The only initial evidence event is maintainer initialization. All E01–E22 skills and Q5–Q12 later modules start `not_started`; Q0 / 0.3 is `in_progress`, with both execution and explanation gates pending.

The learner code location starts null/unverified. This curriculum checkout does not imply a learner app. Before launch guidance, inspect the actual app metadata or obtain its location from the learner. A verified location requires a `location` learner observation with an explicit `observed_path` exactly matching that path after Windows path normalization; portability does not require that app to exist in every curriculum clone. A moved/unavailable path becomes unverified after reconciliation. Installed versions start null until actual environment evidence exists.

## Evidence record

`schema_version` is 1 in both JSON snapshots. Each JSONL line is one object with a globally unique `id` and ISO `at` date or timestamp in nondecreasing chronological order. No blanks, duplicate IDs or invalid JSON are accepted. The first event is `initialization`, actor `maintainer`, with a source and summary; it cannot satisfy gates or skills.

Actual learner observations use these fields:

| Field | Meaning |
|---|---|
| `id`, `at` | Stable reference and observed date/time |
| `kind` | `execution`, `explanation`, `modification`, `debug`, `transfer`, `engagement`, `operational`, or `location` |
| `actor` | `learner` for learner evidence; never relabel a simulation |
| `milestone` | One declared milestone ID |
| `skill_ids` | Zero or more existing E IDs or later Q IDs supported by this observation |
| `outcome` | `pass`, `fail`, or `observed`; pass is a reasoned decision against the stated expected behavior |
| `assistance` | `none`, `docs`, `hint`, `scaffold`, `worked_example`, or `ai_implemented` |
| `expected` | What was being checked, including relevant acceptance case/context |
| `observation` | Safe verbatim learner output/explanation or an exact source pointer; no invented paraphrase-as-quote |
| `source` | A nonempty traceable `conversation:<nonempty-id>` / `turn:<nonempty-id>` reference or local artifact path; local file pointers use repository-relative paths |
| `redactions` | Array describing removed sensitive fields, empty when none; never include removed values |

An `ai_implemented` outcome can describe the learner running assistant-written code; it cannot prove independent implementation. A provider success needs enough observed command/output/context to distinguish it from a mock or printed fixture. A single sentence “it worked” is a reported claim until its meaning is reconciled. A local validator cannot authenticate a pasted output or judge the correctness of prose: the tutor must inspect actual evidence and acceptance scope.

Never request or persist API keys, patient data, or sensitive customer data. Redact sensitive values before appending; record what was redacted and preserve the safe remainder or a safe source reference. If the full evidence cannot be retained safely, use a minimal safe description and mark that limitation. Do not write raw sensitive content as a temporary evidence artifact.

Corrections append `kind: correction`, `actor: maintainer`, `supersedes` naming one earlier learner observation, and a nonempty `reason`. Corrections invalidate that observation without deleting history; append replacement learner evidence only when real evidence supports it. An initialization or prior correction cannot be superseded. For a given milestone/kind, the newest non-invalidated learner event is current; newer failed evidence defeats an older pass. Skill references use the newest event for that skill/milestone/kind, so an unrelated skill observation does not erase demonstrated work. Explain contradictions and update affected gates/statuses visibly.

## Gates and competence

Milestone IDs 0.3–0.9 retain Q0 continuity within J0. J1–J5 have stage-level evidence gates; actual acceptance cases come from [curriculum](CURRICULUM.md). Every gate has `status` (`pending` or `satisfied`) and `evidence_ids`. A satisfied gate requires the latest active passing event of the matching kind and milestone. A pending gate can retain failed/observed evidence or await tutor review of a pass. Milestone `complete` requires all its gates satisfied. A later active milestone cannot bypass an incomplete prerequisite. If reassessment reopens an earlier prerequisite, return the active milestone to that prerequisite; retain downstream work with its own valid evidence and evidence that prerequisites previously passed before that work. Historical completion does not authorize advancing past the reopened prerequisite. Passing evidence permits a reasoned update, never automatic advancement by execution alone. Completing 0.3 does not complete J0 or grant E03 independence.

Q0 / 0.3 requires separate `execution` and `explanation` events. Do not copy the model's generated boundary explanation into the learner explanation field. Later gates add learner modification, debugging and delayed transfer as specified in the route. Explanation, modification, debugging and transfer gates reject `ai_implemented` evidence. Transfer gates in 0.9, J2 and J5 require transfer on a later calendar date than passing modification practice; supported work is distinct from independent skill promotion. One event may support multiple genuinely demonstrated skill IDs, but not multiple evidence kinds by relabeling output.

Skill status meanings:

- `not_started`: no qualifying competence decision. Mere curriculum exposure is not a promotion.
- `introduced`: engaged learner explanation or engagement evidence.
- `practiced`: supported execution, modification, debugging, or transfer evidence.
- `applied_independently`: explanation, modification, debug and delayed transfer with assistance `none` or `docs`.
- `production_understanding`: independent evidence plus actual scoped `operational` evidence; architecture intent alone is insufficient.

For automated independence checks, transfer must occur on a later calendar date than the supporting modification practice. Same-day practice can be recorded but does not yet satisfy that delayed-transfer check. Current native quest labels are `Q0` within J0 and otherwise the stage label (`J1`–`J5`). Selected later Q5–Q12 milestones can be added with execution, explanation and debug gates after the initial route is complete; deeper acceptance still comes from the selected module.

Statuses can stay conservative while evidence accumulates. Required evidence references must be active, passing, tagged for that skill and latest for that skill/milestone/kind. Downgrade or return to pending when contrary current evidence invalidates a claim; retain the reason in a correction/checkpoint narrative. Explanation questions alone are not failures. These statuses express demonstrated scope, not universal mastery of a whole technology.

The three review queues (`blockers`, `delayed_practice`, `role_gaps`) hold objects with `evidence_ids`, `observation`, `next_task`, and `trigger`. Add them only after a real observation. Trigger delayed practice by a later session/date, adjusted to actual schedule. Queue entries do not create calendar automations.

## Safe checkpoint writes

Inspect existing files and new evidence before writing. Validate candidate objects in memory using `validate_state` from the standard-library validator before persisting them. Append each new actual event once, then update skill/current snapshots to reference it. Use temporary sibling files and atomic replacement for JSON snapshots when practical; never overwrite the log. Read back all three files and run `python tools/validate_workspace.py`. Do not claim success until readback and validation succeed.

The snapshots are not a database transaction. `last_event_id` and `updated_at` are required in both snapshots. Each snapshot must reference the last JSONL event and cover its timestamp, so an interrupted append/update is detectable. If files disagree, stop advancement and reconcile from the intact log plus newest actual learner evidence. Do not delete an inconvenient event, reset progress, or silently synthesize completion. Report failed writes/validation and preserve the exact pending action in the response if persistence remains unavailable. Serialize concurrent writers by coordinating one checkpoint writer; re-read before each update and do not overwrite another writer's newer state.

At a pause preserve milestone/mode, last learner event, conceptual thread, assistance, expected/observed evidence, blocker, pending action and next retrieval target. `active_minutes_observed` stays null unless actual time was supplied; estimate time in lesson prose separately. `last_learner_event` references the latest learner observation, excluding corrections/init. `updated_at` must cover the latest event date. `stage`, `quest`, and active `milestone` must agree. A finished route can retain J5 as the active completed checkpoint.

## Validation boundary

The read-only validator checks schema, paths, references, evidence kinds, current-event precedence, skill/gate prerequisites, ordering and owned document links. `--self-test` runs synthetic positive and negative fixtures only in memory. It cannot establish clinical validity, actual execution, a correct explanation, effective teaching, or job readiness. Tutor simulations belong in [pilot](PILOT.md), never in the learner log.
