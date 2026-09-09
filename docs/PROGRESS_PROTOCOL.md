# Portable progress protocol

This document owns evidence/status rules adapted from V3.2 sources 02 and 03. [Current state](../progress/current.json) owns the active action; [skills](../progress/skills.json) owns competence; [evidence](../progress/evidence.jsonl) is append-only factual history. [Teaching](TEACHING_GUIDE.md) owns modes. Curriculum edits, generated code and static checks never create learner achievements.

## Read only the part you need

This document is a reference, not a briefing. An ordinary lesson needs none of it.

| Doing this | Read |
|---|---|
| Resuming, reconciling saved state against newer evidence | *Resume and reconcile* |
| Recording an observation | *Evidence record* |
| Deciding whether a gate or skill status may change | *Gates and competence* |
| Writing a checkpoint to disk | *Safe checkpoint writes* |
| Advancing on readiness, or reopening a corrected claim | *Readiness, final ownership and reassessment*, then *Durable readiness and downstream history* |

Nothing here is teaching policy; [the teaching guide](TEACHING_GUIDE.md) owns that. The
prohibitions in this document exist to keep a record honest, not to shape a lesson: if a
rule here appears to be telling you how to teach, you are reading the wrong document.

## Resume and reconcile

Prefer newest actual learner evidence in the turn, then conversation, saved checkpoint, and saved state. Start with the latest event and unresolved action. Initial onboarding is inherited as complete and calibration sufficient; this is a continuity decision, not proof of installed packages or competence. The only initial evidence event is maintainer initialization. All E01–E22 skills and Q5–Q12 later modules start `not_started`; Q0 / 0.3 is `in_progress`, with both execution and explanation gates pending.

The learner code location starts null/unverified. This curriculum checkout does not imply a learner app. Before launch guidance, inspect the actual app metadata or obtain its location from the learner. A verified location requires a `location` learner observation with an explicit `observed_path` exactly matching that path after Windows path normalization; portability does not require that app to exist in every curriculum clone. A moved/unavailable path becomes unverified after reconciliation. `provider.installed_versions` has exactly four keys—`python`, `uv`, `groq`, and `python-dotenv`—whose values start null until actual environment evidence exists; add a schema revision before changing that shape.

## Evidence record

`schema_version` is 1 in both JSON snapshots. Each JSONL line is one object with a globally unique `id` and canonical `at`: `YYYY-MM-DD` or a full ISO timestamp with seconds (optional fraction and zone; a missing zone means UTC) in nondecreasing chronological order. No blanks, duplicate IDs or invalid JSON are accepted. The first event is `initialization`, actor `maintainer`, with a source and summary; it cannot satisfy gates or skills.

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

Corrections append `kind: correction`, `actor: maintainer`, `supersedes` naming one earlier learner observation, and a nonempty `reason`. Corrections invalidate that observation without deleting history; append replacement learner evidence only when real evidence supports it. An initialization or prior correction cannot be superseded. Evidence freshness is scoped by milestone, kind and capability overlap: a later event supersedes an earlier event only when both share the milestone and kind and their `skill_ids` overlap. An event with no capability tags is milestone-wide and therefore overlaps every event of that milestone/kind. A failed E13 framework explanation can reopen E13 and dependent abstraction work without erasing a still-current E09 retrieval explanation. Explain contradictions and update only the overlapping gates/statuses visibly.

## Gates and competence

Milestone IDs 0.3–0.9 retain Q0 continuity within J0. J1, J3 and J4 each carry a `modification` gate, because each stage's route text asks the learner to change something they did not copy; that evidence belongs on the milestone, not only on a skill row. Inherited setup milestones `0.1` and `0.2` carry no gates and never appear in the milestone list, but they are valid evidence milestones: a genuine diagnostic or setup failure is recorded against them rather than relabeled under `0.3`. J1–J5 have stage-level evidence gates; actual acceptance cases come from [curriculum](CURRICULUM.md). Every gate has `status` (`pending` or `satisfied`) and `evidence_ids`. A satisfied gate requires current active passing evidence of the matching kind and milestone under the overlap rule above. A pending gate can retain failed/observed evidence or await tutor review of a pass. Milestone `complete` requires all its gates satisfied.

Route entry and completion are separate dependency decisions. The recommended narrative is J0 -> J1 -> J2 -> J3 -> J4 -> J5, and the J0 increments through J3 retain their preceding readiness dependency. J4 may become active after J2 is `ready` or `complete`, allowing direct parameterized SQL and scoped read-tool work while J3 is incomplete. J4 cannot become `ready`/`complete` until J3 is also `ready` or `complete`, because the finished support workflow combines retrieved policy with order facts. J5 requires J4 completion, and therefore inherits both branches. If reassessment reopens an earlier prerequisite, return the active milestone to the affected prerequisite unless another dependency-safe branch remains useful; retain downstream work with its own valid evidence and evidence that its actual entry prerequisites previously passed before that work. Historical completion does not authorize a new dependent step past a reopened prerequisite. Passing evidence permits a reasoned update, never automatic advancement by execution alone. Completing 0.3 does not complete J0 or grant E03 independence.

Q0 / 0.3 requires separate `execution` and `explanation` events. Do not copy the model's generated boundary explanation into the learner explanation field. Later gates add learner modification, debugging and delayed transfer as specified in the route. Explanation, modification, debugging and transfer gates reject `ai_implemented` evidence. Transfer gates in 0.9, J2 and J5 require transfer at least 24 hours after passing modification practice (two calendar days when either observation has only a date); supported work is distinct from independent skill promotion. One event may support multiple genuinely demonstrated skill IDs, but not multiple evidence kinds by relabeling output.

Skill status meanings:

- `not_started`: no qualifying competence decision. Mere curriculum exposure is not a promotion.
- `introduced`: engaged learner explanation or engagement evidence.
- `practiced`: supported execution, modification, debugging, or transfer evidence.
- `applied_independently`: explanation, modification, debug and delayed transfer with assistance `none` or `docs`.
- `production_understanding`: independent evidence plus actual scoped `operational` evidence; architecture intent alone is insufficient.

The validator's elapsed-time check is a rejection floor, not the teaching interval: 24 hours is the point below which a delayed-transfer record is refused, while the interval to actually teach to remains 2-7 days. Do not schedule to the floor. For automated independence checks, transfer must occur at least 24 hours after supporting modification practice; if either observation has only a date, compare their UTC-normalized calendar dates and require a two-day difference, rather than 48 elapsed hours. Basic ISO dates and partial timestamps are rejected. Do not invent timestamps for historical evidence. A different date just minutes after practice does not establish delayed retention. Same-day practice can be recorded but does not yet satisfy that delayed-transfer check. Current native quest labels are `Q0` within J0 and otherwise the stage label (`J1`–`J5`). Selected later Q5–Q12 milestones can be added with execution, explanation and debug gates after the initial route is complete; deeper acceptance still comes from the selected module.

Statuses can stay conservative while evidence accumulates. Required evidence references must be active, passing, tagged for that skill and latest for that skill/milestone/kind. Evidence supporting an `applied_independently` or `production_understanding` claim should carry a durable `source` -- a repository-relative artifact path rather than a conversation reference alone -- so the strongest claims remain checkable after the conversation is gone. Downgrade or return to pending when contrary current evidence invalidates a claim; retain the reason in a correction/checkpoint narrative. Explanation questions alone are not failures. These statuses express demonstrated scope, not universal mastery of a whole technology.

The three review queues (`blockers`, `delayed_practice`, `role_gaps`) hold objects with `evidence_ids`, `observation`, `next_task`, and `trigger`. Add them only after a real observation. They can organize ordinary review work, but a `delayed_practice` queue entry is not a second readiness contract and cannot authorize advancement. Queue entries do not create calendar automations.

## Safe checkpoint writes

Inspect existing files and new evidence before writing. Validate candidate objects in memory using `validate_state` from the standard-library validator before persisting them. Append each new actual event once, then update skill/current snapshots to reference it. Use temporary sibling files and atomic replacement for JSON snapshots when practical; never overwrite the log. Read back all three files and run `python tools/validate_workspace.py`. Do not claim success until readback and validation succeed.

The snapshots are not a database transaction. `last_event_id` and `updated_at` are required in both snapshots. Each snapshot must reference the last JSONL event and cover its timestamp, so an interrupted append/update is detectable. If files disagree, stop advancement and reconcile from the intact log plus newest actual learner evidence. Do not delete an inconvenient event, reset progress, or silently synthesize completion. Report failed writes/validation and preserve the exact pending action in the response if persistence remains unavailable. Serialize concurrent writers by coordinating one checkpoint writer; re-read before each update and do not overwrite another writer's newer state.

At a pause preserve milestone/mode, last learner event, conceptual thread, assistance, expected/observed evidence, blocker, pending action and next retrieval target. `active_minutes_observed` stays null unless actual time was supplied; estimate time in lesson prose separately. `last_learner_event` references the latest learner observation, excluding corrections/init. `updated_at` must cover the latest event date. `stage`, `quest`, and active `milestone` must agree. A finished route can retain J5 as the active completed checkpoint.

## Validation boundary

The read-only validator is a consistency and discipline harness, not a fraud check. It verifies schema, paths, references, evidence kinds, current-event precedence, skill/gate prerequisites, ordering and owned document links -- the shape of the record. It cannot distinguish an invented observation from a true one; that judgement is the tutor's and the learner's alone, and no count of passing fixtures changes it. `--self-test` runs synthetic positive and negative fixtures only in memory. It cannot establish clinical validity, actual execution, a correct explanation, effective teaching, or job readiness. Tutor simulations belong in [pilot](PILOT.md), never in the learner log.


## Readiness, final ownership and reassessment

A milestone with transfer may be `ready`: every non-transfer gate is satisfied and transfer remains pending. Before advancing, append one maintainer `kind: readiness` event. That single event owns the delayed-practice contract: `id`, `at`, `actor: maintainer`, `milestone`, traceable `source`, the exact then-current passing non-transfer `evidence_ids`, `eligible_after`, `next_task`, and `trigger`. It must be appended before dependent work, and `eligible_after` must meet the transfer delay from the referenced modification. Missing, premature or stale readiness evidence is rejected. The event is teaching administration, not learner competence; it does not change `last_learner_event` or satisfy transfer. No duplicate queue record is required. Complete transfer only after actual qualifying evidence. The usual teaching interval remains 2–7 days; 24 hours is a machine-checkable minimum, not proof of retention by itself.

J5 explanation, modification, debug and transfer require assistance `none` or `docs`. Supported execution remains valid. J5 readiness and completion require every E01–E22 capability to be at least `practiced` with qualifying evidence; completion also requires E22 independent or production-understanding evidence. This means capability coverage plus independent delivery, not universal independent mastery of every skill. Multiple capability tags require genuinely demonstrated acceptance scope for each tag.

For prerequisite history, use the latest valid evidence before downstream work began; append order resolves equal timestamps. A genuine subsequent failure does not erase earlier valid work. A correction invalidates its target even in historical checks: reopen affected downstream claims to `pending`, retaining artifacts and valid gate observations. Historical readiness requires the durable decision described below; a mutable live queue cannot retroactively justify past work. Return the active milestone to the prerequisite requiring reassessment.

A later active failure tagged to a skill in any milestone requires explicit handling before retaining independence. Downgrade conservatively, obtain a later independent passing reassessment for the failed kind, or record a skill-row `reconciliations` array. Each decision contains `failure_id`, `decision: retain`, `reason`, `scope`, `source`, and `at` at or after the failure. The failure must concern this skill; resolved or corrected failures may retain their historical decision, but only an active failure and its matching decision can support a present retain claim. Decision time cannot exceed the containing skills snapshot time; the source is traceable and the reason explains why it lies outside the explicitly retained scope. Reconciliation never turns stale or failed gate evidence into a pass. The tutor judges the rationale; the validator checks references and structure. Questions requesting explanation are not failure observations.


## Durable readiness and downstream history

Current `ready` status requires a readiness event matching its current non-transfer proof. Historical readiness uses the same event appended before the dependent gate evidence being claimed. Its proof must remain uncorrected and valid at that boundary; a subsequent non-overlapping failure does not stale it, and a subsequent genuine regression does not erase the valid historical decision. Corrections invalidate referenced proof even if the prerequisite has recovered today. Current completion cannot backfill an earlier missing prerequisite. Check each claimed dependent gate against the entry dependencies that applied to that branch and the event order, not an unrelated earliest observation. Reopen affected claims while keeping artifacts; after new valid prerequisite proof and fresh dependent reassessment, claims can recover.

J5 `complete` additionally requires every initial-route milestone complete: readiness supports useful advancement, but outstanding earlier retention prevents final route certification. Reconciliation records remain auditable after later reassessment and are structurally validated at every skill status; keep their real failure reference, reason, scope, source, decision and bounded timestamp.
