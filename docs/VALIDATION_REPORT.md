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

## Teaching-material pass — 2026-09-09

A multi-perspective review of the curriculum, AI-guiding files and skills found that prior
review cycles had been engineering lenses only. Twelve triaged findings above all concern
ledger integrity; none tested whether the material teaches. Two defects followed from that.

**Acceptance clause not met.** [acceptance.md](../_bmad-output/specs/spec-codex-learning-workspace/acceptance.md)
requires that *"rich first-exposure instruction/inline explanation survives removal of
NotebookLM host formatting."* It did not. The five Golden Exemplars in frozen source 06 —
roughly 3,700 words of worked teaching responses — were dropped as host packaging, leaving
[TEACHING_GUIDE.md](TEACHING_GUIDE.md) with no worked example and no code fence. Restored,
adapted, as per-situation references under the tutor skill; host formatting stays dropped.

**Required fixtures did not exist.** [CURRICULUM.md](CURRICULUM.md) J1 and
[ENGINEERING_GUIDE.md](ENGINEERING_GUIDE.md) both mandate synthetic cases for absent facts,
negation, uncertainty, chronology, malformed output and instruction-like text. None existed
as files, so each session regenerated them, which made J5's "freeze expected outcomes before
running" structurally unsatisfiable. Seven notes and eight hand-written payloads are now
frozen in [fixtures](../fixtures/README.md). Expected values are deliberately absent: they
are learner work.

**J3 embedding route had no owner.** The curriculum said "use one embedding route" and never
named it while E09 requires separate Arabic reporting. Recorded as [DR-001](DECISIONS.md)
with its Arabic consequence stated in advance, so a poor Arabic result is attributable to
the model rather than to the learner.

Changes are additive; no governing rule was rewritten and no progress file was touched.
Four pointer edits wire the new material into `CURRICULUM.md`, `ENGINEERING_GUIDE.md` and
the tutor skill. On that branch `python tools/validate_workspace.py` and `--self-test` PASSed
at 20 owned documents and 92 fixtures; the counts after merge are recorded in the merge
section below, not here.

Not established by this pass: that the restored exemplars improve tutoring, that the
fixtures cover the failure modes a real learner hits, that DR-001's default is the right
one, or any learner progress whatsoever. Static structure only.

**Known gap at the time of this pass — since resolved.** CAP-5 requires the project skill to
be discoverable. When this pass was written it was not: `.claude/skills/` was gitignored
wholesale, so `ai-engineering-tutor` was absent from a fresh clone's skill picker and
[AGENTS.md](../AGENTS.md) worked around it by naming the skill path directly. Resolved
separately on `main`: [.gitignore](../.gitignore) now un-ignores
`.claude/skills/ai-engineering-tutor/`, [tools/sync_tutor_skill.py](../tools/sync_tutor_skill.py)
mirrors the `.agents` source into it, and the validator fails on drift between the two.

## Curriculum pacing and delivery pass — 2026-09-09

Scope: teaching sequence, portfolio timing and deferral boundaries. No learner evidence, gate, milestone ID, capability ID or validator rule was changed; `progress/current.json` and `progress/evidence.jsonl` are untouched.

- `python tools/validate_workspace.py` and `--self-test`: PASS, 92 in-memory fixtures. The owned-document count moved from 19 to 20 when `docs/LESSON_TEMPLATE.md` was added in the pedagogy pass below; fixtures are unchanged.
- Route changes: J0's 0.3–0.9 identifiers are regrouped into three presented blocks; each stage now ends with a capture step; J5 is split into three passes; framework work in J3/J4 is a bounded comparison rather than a rebuild of working code.
- A consolidated deferral table names each deferred area with the observation that reopens it, and the boundary-check versus test-engineering distinction is stated explicitly in the route and engineering guide.
- Portfolio gains a per-stage capture table and explicit application timing; the readiness-machinery paragraph duplicated in the route map and assessment cards is replaced by a pointer to its single definition in the progress protocol.
- `progress/skills.json` free-text `capability`, `stage` and `evidence_target` fields were revised for E13, E17 and E20. All IDs, statuses and evidence references are unchanged.
- Not established by this pass: any learner execution, understanding, teaching effectiveness, pacing accuracy, portfolio quality or job readiness. No tutor simulation was rerun; the pilot scenarios in [pilot](PILOT.md) remain at their prior recorded state.

## Teaching pedagogy pass — 2026-09-09

Scope: how lessons are delivered. No learner evidence, milestone, gate, capability ID or validator rule changed.

- Added a **Teaching moves** section to [teaching](TEACHING_GUIDE.md) defining six binding moves: napkin sketch before code, cafe-register explanation with the learner's objection voiced and any analogy bounded, detail dives taken to the actual mechanism, a named complexity ladder with one new difficulty per rung, every explanation ending on the keyboard, and practice tasks.
- Practice is split: predict-then-run belongs inside the action; break-it-on-purpose, explain-it-back and reconstruct-from-blank are **offered and freely skippable**, with an explicit instruction to continue without comment, penalty or re-offering. Optional self-checks are informal and never satisfy or block an evidence gate.
- Added [lesson template](LESSON_TEMPLATE.md) as the required shape for first-exposure lessons, including the cases where it must not be applied. Owned documents: 20.
- Mirrored the operative rules into [the tutor skill](../.agents/skills/ai-engineering-tutor/SKILL.md) and [AGENTS.md](../AGENTS.md).
- Added five [pilot](PILOT.md) scenarios covering the new behaviors — template application on first exposure, skipping optional checks, a direct question mid-lesson, stage-end capture prompting, and deferral-trigger questions — plus judging criteria that fail a move performed as an empty heading. These are written, **not yet run**: no tutor simulation has been executed against the new template, so the pilot's recorded results remain at their prior state.
- [Migration](MIGRATION.md) records that the named teaching moves and the first-exposure lesson shape are a native addition, not archive content; the frozen source prescribed the intent, not this structure.
- Not established by this pass: teaching effectiveness, learner understanding, retention or engagement.

## Interaction template set — 2026-09-09

Scope: tutoring exchange shapes. No learner evidence, milestone, gate, capability ID or validator rule changed.

- [Lesson and interaction templates](LESSON_TEMPLATE.md) expands from one first-exposure shape to six, with a routing table keyed on the learner's most recent event: first exposure, next rung, debugging, assess, build together and resume. The four exchange types the original template excluded now have defined shapes rather than being left to improvisation.
- Adds the stage-end capture contract — demo, README paragraph, numbers with denominators, one bracket-free CV bullet — which the route required at every stage without defining anywhere, and napkin sketch conventions so a sketch grows across stages instead of being redrawn from scratch.
- Three further [pilot](PILOT.md) scenarios cover the debugging, build-together and next-rung shapes. As with the previous pass, these are written and **not yet run**.
- Mirrored into [the tutor skill](../.agents/skills/ai-engineering-tutor/SKILL.md), [teaching](TEACHING_GUIDE.md) and [AGENTS.md](../AGENTS.md). Owned documents remain 20.
- Not established by this pass: teaching effectiveness, learner understanding, retention or engagement.

## Adversarial review of this session's own changes — 2026-09-09

An unbiased review pass over the three preceding entries, recorded because the findings are against this session's own work.

- **Specification volume.** This session added 399 lines and removed 31 across 13 files, after opening with a criticism of documentation bloat. `docs/TEACHING_GUIDE.md` grew from 10,469 to roughly 20,000 bytes and `docs/LESSON_TEMPLATE.md` was created at 13,000. The critique of inherited ceremony was applied to inherited documents and not to the new ones. This pass reduced the tutor skill by about 1,850 bytes by removing restatement, and trimmed duplicated override rules from the template, but the net direction of the session remains strongly additive.
- **Unsupported claims, now removed.** Five assertions were written in a confident register without evidence: two superlatives about interview relevance, an invented capture-duration comparison, a session-length estimate for J0 blocks after criticising the inherited five-hour assumption, and a coverage claim about junior posting requirements. The last was the most serious: it reached [portfolio](PORTFOLIO.md), where a learner would use it to decide when to apply, and it originated from secondary content-marketing pages rather than any labour-market source. It is replaced with an instruction to collect actual listing requirements and an explicit warning not to trust a coverage claim from this document.
- **Triplication.** The six teaching moves were stated in full in three places after this same session compressed a paragraph duplicated across five files. [Teaching](TEACHING_GUIDE.md) now owns the moves and their rationale, [lesson and interaction templates](LESSON_TEMPLATE.md) owns the shapes, and the tutor skill points at both instead of restating them.
- **Missing shape.** No template covered a learner with no runnable project — the actual pending situation throughout the session. Added as Shape 0, cold start.
- **Verification gap, unresolved.** Eleven pilot scenarios are now written and **none has been run**. Static validation checks links, JSON structure and fence balance; it cannot determine whether any teaching instruction is followed. The behavioral specification has roughly doubled while behavioral verification remains at zero. This is the largest outstanding risk in the workspace and is not addressed by this pass.
- Not established by this pass: teaching effectiveness, learner understanding, retention, engagement or job-market accuracy.

## First executed teaching pilot — 2026-09-09

The verification gap recorded in the previous entry is now partially closed. Six of the eleven [pilot](PILOT.md) scenarios were run in fresh independent read-only contexts.

- **Five clean passes, one finding.** Skipping optional checks, a direct question mid-lesson, a pasted traceback, a request to have code written, and a stage declared finished all behaved as specified. The debugging case is the strongest result: it named configuration as the failing layer and explicitly ruled out authentication, which is the exact conflation [engineering](ENGINEERING_GUIDE.md) warns against, and it did so without being told that was the test.
- **The finding:** a request for a later-stage mechanism produced a complete lesson for it. Placement was disclosed and a return offered, but after the fact, spending a session that produced no evidence for the active increment. No shape covered this. An off-route rule was added to [lesson and interaction templates](LESSON_TEMPLATE.md): disclose placement, answer the conceptual question, put the choice explicitly to the learner before delivering a later-stage lesson, and state that a detour advances no milestone.
- **Added a worked fragment** to the same document — a condensed real transcript annotated with the move each part performs — on the evidence that the shapes were followed accurately from prose alone, so a fragment supplements rather than replaces them. The proposal to replace the specifications with an exemplar outright is not supported by this run.
- **Routing held.** All six reached the tutor skill through [AGENTS.md](../AGENTS.md) unprompted, read six to twelve files each, and none wrote a file, called a provider or asserted learner evidence.
- **Limits.** Six single runs, one judge, scenarios authored by the same session that wrote the documents under test. This establishes neither repeated-run reliability nor any learning outcome, and five scenarios remain unrun. Teaching effectiveness, learner understanding, retention and job-market accuracy remain unestablished.
