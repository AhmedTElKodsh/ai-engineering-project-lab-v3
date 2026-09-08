---
title: 'Codex learner-owned curriculum workspace'
type: 'feature'
created: '2026-09-08'
status: 'ready-for-publication'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: 'UNBORN'
review_base_commit: 'd58c4f5bf615b7d60e2c9f90412dc063777c22fc'
context: []
---

<frozen-after-approval reason="User requested configuration, planning, tutoring skill and private publication after the proposed Codex approach">

## Intent

**Problem:** V3.2 is a NotebookLM source pack. This repository has installed BMAD skills and no first commit, but lacks a Codex tutoring entry point, authoritative portable learning state and native planning documents.

**Approach:** Configure this repository as the learner's project-first AI engineering workspace with a small teaching contract, native guides, an automatically discoverable tutoring skill, basic BMAD spec companions and durable evidence. Preserve existing artifacts. The root agent handles GitHub publication after local validation and review.

## Boundaries & Constraints

**Always:** Learner ownership during lessons; clear Learn/Assess/Build together modes; explicit maintainer work executes normally. Current Q0 / 0.3 Groq call remains pending with no fabricated achievements. J0-J5 develops medical extraction/review and retail triage/RAG/SQL/tools then a junior application checkpoint. Egypt plus eligible remote roles. Explain first exposures thoroughly but focus each exercise on one mechanism. Keep code/source fidelity, gradual hints, direct answers, spaced retrieval, delayed transfer and independent explanation/debug evidence. Basic checks, secrets and authorization follow the active boundary; deep testing/deployment/LLMOps remain later.

**Never:** Implement the learner's apps in this setup; run a provider call; ask for keys or patient data; award mastery from generated code/tests; silently restart onboarding; edit original Downloads or the V3.2 pack; publish a public repository; invent clinical validity, job eligibility or a timeline. Ordinary lesson requests do not invoke BMAD Build automatically. Existing vendor skills stay intact.

</frozen-after-approval>

## Code Map

- `curriculum/V3.2_Medical_and_Retail_Junior_Path/NotebookLM_Live_Source_Pack/` — seven source guides; preserve archive bytes and reuse content through deliberate native adaptation.
- `curriculum/.../Maintainer_Only/` — prior validation and pilot; preserve, do not treat PASS as native behavior proof.
- `.agents/skills/` — installed BMAD skills; add custom tutor alongside them; don't edit vendor definitions.
- `_bmad/config.toml`, `_bmad/scripts/` — setup materialized from installed BMAD 6.13.0-next skills. Default output `_bmad-output`.
- `.agents/skills/bmad-spec/SKILL.md`, `assets/spec-template.md` — basic five-field spec plus canonical append-only memlog; follow for the requested native planning spec.
- `C:/Users/Asd/.codex/skills/.system/skill-creator/SKILL.md` — skill authoring/validation; use for the tutor.

## Tasks & Acceptance

**Execution:**
- [x] `AGENTS.md`, `AGENT.md`, `README.md` — concise Codex default instructions; singular file only a pointer; practical start/resume and maintainer commands.
- [x] `docs/CURRICULUM.md`, `docs/TEACHING_GUIDE.md`, `docs/ENGINEERING_GUIDE.md`, `docs/PORTFOLIO.md` — native active route, rich first-exposure teaching behavior, mechanism-first technical standards and truthful job evidence. Reuse V3.2, no two active contradictory policies. Source-grounding and technical exactness survive removal of NotebookLM host rules.
- [x] `progress/current.json`, `progress/skills.json`, `progress/evidence.jsonl`, `docs/PROGRESS_PROTOCOL.md` — unambiguous current state and skills; append actual learner evidence only; explicit initialization event, no run/understanding proof. Latest user evidence wins. Reconcile state and evidence safely; never silently advance on successful execution alone. Learner code location starts null/unverified; curriculum root is not assumed to contain app/main.py.
- [x] `docs/PROVIDER_REFERENCE.md` — retained dated Groq baseline semantics/code and unknown installed versions. No new verification claim.
- [x] `.agents/skills/ai-engineering-tutor/SKILL.md` and useful references/UI metadata — precise lesson/resume/debug/assessment triggers and exclusions; reference authoritative guides; read needed content incrementally; normal automatic selection.
- [x] `_bmad-output/specs/spec-codex-learning-workspace/{.memlog.md,SPEC.md,architecture.md,acceptance.md}` — derive kernel from memlog using actual BMAD helper. Include stable capability intent/success pairs, constraints/non-goals and preservation mapping. Do not invent an entire enterprise PRD or stories.yaml requiring user interview.
- [x] `docs/PILOT.md`, `tools/validate_workspace.py` — behavioral scenario protocol plus standard-library validation of JSON relationships, evidence references, pending gates, local links and owned document structure. Tool is read-only and never executes learner apps. Include meaningful negative fixtures if an evidence/gating validator is implemented. Explain static vs agent simulation vs actual learner proof.
- [x] `docs/MIGRATION.md` — map every live V3.2 source to native authority and distinguish frozen archive from current state; documents and app are distinct.

**Acceptance Criteria:**
- Given a fresh lesson thread, when instructions and saved state are read, then it resumes Q0 / 0.3 without pretending an app exists or installing everything again.
- Given success output without an explanation, when evaluating advancement, then execution is recorded separately and the milestone remains pending understanding.
- Given an explicit maintain/configure/publish request, when routing it, then student assessment is not imposed on that work.
- Given a new clone, when running the standard-library validator, then it validates native paths/state without the author's Downloads path, secrets or provider access.
- Given the private repository publication, when the root agent verifies it, then private visibility and the published tree/commit correspond to the reviewed files.

## Implementation Notes

- User's explicit request authorizes this previously proposed setup and publication. Existing untracked content belongs to the initial project and will be preserved. No existing git commits/remotes; baseline is UNBORN, not a fabricated SHA.
- Repo name assumption: ai-engineering-project-lab-v3 in the authenticated personal account; check availability before create.
- Root handles ignores, git/auth, privacy, commit/push and publication evidence. Implementation agent owns the local document/skill/validation tasks above and may not stage, commit, push, invoke paid providers or modify this build record's frozen intent.
- Original V3.2 artifacts, installed BMAD source skills and their lockfile were preserved in local baseline commit d58c4f5bf615b7d60e2c9f90412dc063777c22fc. The repository was initially unborn; review compares authored setup against this exact preserved-source baseline. No remote created yet.

## Spec Change Log

## Review Triage Log

- Iteration 1: three independent reviewers examined the frozen authored diff. Eleven validator/verification findings were accepted and patched. Duplicate delayed-transfer findings were consolidated. Two inherited BMAD runtime/test findings were confirmed, documented, and deferred because the frozen boundary preserves vendor skills. Full verdicts and evidence are in `docs/VALIDATION_REPORT.md`.

## Verification

- `python tools/validate_workspace.py` — expected coherent native state, references and constraints; read-only.
- Skill Creator `quick_validate.py` — expected valid tutor skill metadata.
- Independent bounded tutor simulations — evaluate responses to resume, success-only, assessment and maintainer prompts without provider calls or student state writes.
- Root publication verification — private visibility, local/remote commit and clean worktree.
- Local result: native validation passed 45 fixtures; Skill Creator validation, Python compilation, diff hygiene, known-secret pattern scan, and four bounded tutor simulations passed. The real learner/provider boundary remains untested.
