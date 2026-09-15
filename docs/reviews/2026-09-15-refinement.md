# Planning and learner-coach review

Date: 2026-09-15. Repository baseline: ce3d5b767280bb8a376753b04598f377202ecb06. Inputs: uploaded project-planning.zip (33 files), standalone SKILL.md and DELIVERY_VALIDATION.md; existing native guides/tutor/validator; the two explicitly requested public teaching toolkits. This is maintainer work, not learner evidence.

## Findings in the supplied materials

**High: conflicting route/state.** The uploaded M0-M7/T001-T030 plan and learning/progress.json create a second progression system. T001 begins with a FastAPI health service; T002 adds configuration/quality/CI. Installing that unchanged would displace the existing J0/Q0/0.3 provider lesson and inherited Groq/onboarding context. The adapted route retains native J/E/Q identifiers and evidence, not the upload's initial tracker.

**High: incomplete skill bundle in these attachments.** The standalone commerce-ai-coach entrypoint references scripts/coach.py, references, assets/project-template, helper tests and behavioral cases that are not in the supplied ZIP or standalone attachments. The validation report may describe another completed delivery, but its 22 helper tests cannot be reproduced from these files. Do not install missing commands as if available. Adapt useful behavior into the existing complete ai-engineering-tutor bundle instead.

**Medium: scope beyond the initial learning route.** The uploaded architecture, roughly twenty logical entities, durable graph, OIDC, queue, classical classifier and deployment are useful later designs. Their presence must not turn every early mini-tool into an enterprise project. The adapted PRD preserves all 14 FR and 7 NFR identifiers with explicit local versus selected-extension scope. Proposed metrics and case counts remain targets, not results or arbitrary early gates.

**Strengths retained.** Product copilot versus learning coach separation; assistance versus mastery; explicit requests for scoped solutions; source provenance and schema truth distinction; server-owned identity; immutable manager approval; execution-time revalidation; idempotency and unknown-write reconciliation; evaluation leakage awareness; version verification; resource/privacy boundaries.

## Input checks reproduced

The archive contains 33 planning files and no complete coach directory. JSON/JSONL parses. The backlog has 30 unique tasks, all depends_on references resolve and the graph is acyclic; task requirements cover all 21 PRD IDs. These are record checks, not application tests or learning results. Source helper code and its reported 22 tests were not provided and were not rerun.

## Adoption rather than silent replacement

| Supplied component | Disposition |
|---|---|
| README, brief, PRD | Adapt into root entrypoint and project/PRD.md, preserving FR/NFR traceability and declaring narrower initial scope |
| Architecture/data/API/tool design | Preserve core source/identity/approval semantics in project/CONTRACTS.md; defer full database/endpoint catalog |
| RAG/evaluation/testing | Introduce with actual mechanisms; local tests and execution inspection early; larger infrastructure conditional |
| Security/operations | Preserve first-boundary safety; operational guarantees require selected Q6/Q11 evidence |
| Roadmap, foundation plan and backlog | Use project/RELEASES.md inside J0-J5; do not install M/T state or a setup-first course |
| Portfolio/demo | Preserve interview prompts and truthful results; one product, no arbitrary failure-story or corpus quota |
| Sources/risks/traceability | Record current corrections and decision scope; no blanket runtime verification claim |
| Uploaded AGENTS/Copilot/coach setup | Route to one canonical existing tutor, not an incomplete second coach |
| Learner profile/progress/logs/templates | Do not overwrite native evidence, provider choice or onboarding |
| Development evaluation seeds | Design examples only; never relabel as held-out or observed output |
| Delivery report | Treat as supplied assertions with missing-test limitations, separate from this revision's evidence |

Source task mapping remains descriptive, not a new tracker: T001 -> J5; T002 -> J0/J1 with CI deferred; T003 -> incremental fixtures; T004-T007 -> J0/J1 evaluation/intake; T008 -> J4 SQL with larger persistence selected; T009-T011 -> J3 with lifecycle depth selected; T012 -> Q5; T013-T015 -> J4; T016 -> Q6; T017-T018 -> local J4 approval/write with stronger persistence later; T019 -> selected external reconciliation; T020 -> J4 inspection/J5 UI; T021-T022 -> growing evaluations/local traces, hosted traces conditional; T023 -> optional classifier experiment; T024 -> measured comparison; T025-T028 -> current scope checks plus selected auth/queue/deployment/concurrency; T029-T030 -> J5 evidence/handoff accumulated during learning. These mappings do not award completion.

## Public toolkit comparison

### Manware's AI Learning Toolkit

Inspected the copilot tree 3eb77d0ec8b4835b31e5e848559153daf5f4af59, Copilot instructions (blob ac0f4b0caf5b1bdab1190d00173b84710c28d6ba) and learn prompt (b591316a3d80a52c73e25fa5fb56df1fad113aeb). [Source repository](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit).

Useful ideas: distinguish learning from shipping, smallest useful intervention, verification and independent application. Adopt as inspiration with original wording. Do not force attempt-before-feedback before first instruction/direct questions, import parallel learning logs, or bulk-install its workflows. No license file was found in the inspected tree and repository license metadata was null; direct redistribution is not assumed authorized.

### Matt Pocock's teach skill

Inspected [teach](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md), blob c679eeccd48ca720c8196e5d9a9e58223abf213b, and MIT LICENSE f1dd2c09108dde1a5f56097cee8461b3ea834499. Useful ideas: mission-linked short lessons, tangible wins, primary resources, retrieval/spacing and explicit learning records.

Adopt inspiration only. Do not install mandatory HTML lessons/reference components, a new MISSION file or a parallel learning-record hierarchy. Existing product/evidence authorities already serve those purposes. No upstream skill text or installer is bundled. Static reading does not establish teaching effectiveness.

### Local decision

Keep ai-engineering-tutor canonical with an identical existing Claude mirror and Copilot routing. Preserve requested worked examples, direct explanations, evidence-based resumption, safe execution and independent variations. All referenced skill resources are included. Twelve host scenarios are supplied as unexecuted specifications; no activation or coaching pass rate is claimed.

## Technical corrections and preserved material

[Groq compatibility](https://console.groq.com/docs/openai) documents n=1, not the earlier n=2 teaching experiment. The [API reference](https://console.groq.com/docs/api-reference) and [models](https://console.groq.com/docs/models) inspected do not substantiate the earlier embedding default: mark it unverified, not conclusively nonexistent. [Python str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) uses code-point indices, distinct from bytes and graphemes; new Arabic fixtures exercise the original-string round trip.

Preserve native state, append-only evidence, progress schema, validator, frozen sources, historical medical fixtures and vendor skills. No learner app, paid call, real commerce operation, cloud deployment or visibility change is performed. Repository visibility was observed public; do not publish private transcripts or raw business tickets. The upload is reviewed input, not a competing installed authority.
