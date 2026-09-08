# Workspace architecture

The workspace is a set of versioned documents and standard-library validation tools, not a deployed application. Native guidance owns teaching; snapshots and an append-only log own observed learner state. The actual learner code location is explicitly unverified until reconciled.

| Responsibility | Owner |
|---|---|
| Default routing | `AGENTS.md`; singular `AGENT.md` is a pointer |
| Repeatable lesson interaction | `.agents/skills/ai-engineering-tutor/SKILL.md` |
| Product sequence and scope | `docs/CURRICULUM.md` |
| Teaching and engineering depth | `docs/TEACHING_GUIDE.md`, `docs/ENGINEERING_GUIDE.md` |
| Active resume action | `progress/current.json` |
| Competence and review queues | `progress/skills.json` |
| Actual observed history | `progress/evidence.jsonl` under `docs/PROGRESS_PROTOCOL.md` |
| Portfolio and applications | `docs/PORTFOLIO.md` |
| Historical source edition | `curriculum/V3.2_Medical_and_Retail_Junior_Path` |
| Maintainer decisions and acceptance | This spec folder and `_bmad-output/implementation-artifacts` |

The tutor loads current state and teaching guidance, then only the active route/technical sections. Ordinary exercise help does not dispatch BMAD Build. Explicit maintenance follows the requested maintainer scope. Repository rules are a teaching contract, not an infallible enforcement mechanism; actual responses need pilot evidence.

Checkpoint order is new real evidence first, then skill/current snapshots, then readback and validation. Matching `last_event_id` detects incomplete snapshot updates. A correction invalidates evidence without erasing history. The validator rejects invalid references, evidence-kind mismatches, unsatisfied prerequisites and unsupported promotion, but cannot authenticate pasted output or judge a learner explanation.

App launch commands apply only in a verified learner checkout, using task-appropriate authorization. No provider secret is needed for workspace validation. V3.2's original release checks remain frozen; their all-Not-started assumptions must not govern later native progress.

Publication uses a private GitHub repository and Git version history. Existing local junctions, credentials, caches and rendered machine-specific snapshots are excluded. A clone needs no local Downloads source to validate native guides; the inherited provider snapshot remains dated, not newly verified.
