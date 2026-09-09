# Repository maintenance and publication

This repository contains a private learning workspace, reusable curriculum, and installed BMAD tooling. Maintainer setup is separate from student achievement. The original V3.2 NotebookLM pack remains a frozen reference; native Codex guidance and progress files own new lessons.

## Version control

Use ordinary Git commits for meaningful work. The preserved-source baseline is `d58c4f5bf615b7d60e2c9f90412dc063777c22fc`; it contains the pre-existing curriculum, installed BMAD skills and their lockfile. New implementation branches normally use `codex/` unless the user requests another name. No branch or PR ceremony is required for each learner exercise.

The user explicitly requested initial private publication on 2026-09-08. This authorizes creation and upload of the configured project to the authenticated personal account. It does not authorize changing visibility to public, publishing future patient/customer data, or activating external integrations.

## What is included

- Project guidance, curriculum, planning documents and honest learner progress.
- Installed `.agents/skills/bmad*` source copies and `skills-lock.json` for reproducibility.
- The custom tutor skill, setup runtime under `_bmad`, and maintainer verification tools.
- The original local V3.2 pack and its ZIP artifacts. Its recorded machine path is historical provenance, not a dependency for native workspace validation.

Existing `.claude/skills` Windows junctions remain on the original machine but are ignored: they point at `.agents/skills` and are not portable repository content. Generated `_bmad/render` snapshots, Python caches, user TOML overrides, local credentials and `.local` working files are also ignored. The actual source files under `.agents` remain tracked.

## Maintenance checks

Run native workspace validation before recording a setup change. Run the tutor skill's metadata validator when its metadata changes. Assess substantive tutoring changes with the bounded scenarios in the pilot guide; static checks alone cannot establish learning effectiveness.

Before a requested upload, inspect the selected files and Git diff, check for credentials and private raw data, and confirm repository visibility. After upload, compare the local commit with the remote branch. Do not treat successful local commits as successful publication.

Use current official provider documentation when teaching exact APIs. Package/catalog availability is separate from syntax and actual execution. The initial setup does not install the learner's application dependencies or run its provider calls.

## BMAD operation

The project runtime was materialized using the installed BMAD setup command, not a parallel hand-written installer:

```powershell
uv run --no-cache .agents/skills/bmad/scripts/setup.py --project-root . --skill .agents/skills/bmad
```

BMAD planning and implementation skills support maintainer work. Normal teaching should use the tutor skill and native teaching contract. Do not modify vendor skill files to impose student behavior globally; keep project-specific guidance in the repository entry point and custom tutor skill.

## Bundled BMAD limitations

Independent review found two inherited vendor maintenance issues; vendor files are preserved. Replacing an existing runtime on Windows can fail with WinError 183 because `replace_dir` renames into an already-created backup directory. The materialized renderer test suite expects source-repository assets absent from `_bmad`, so it cannot collect here. Initial setup and skill rendering succeeded; runtime replacement and the vendor test suite are not certified. Use the native validator for this curriculum. Repairing vendor maintenance code is deferred to a separate scoped change.

## Host skill mirror

`.agents/skills/ai-engineering-tutor/` is the source of truth for the native tutor.
`.claude/skills/ai-engineering-tutor/` mirrors it so Claude Code registers the skill as
well as the Codex convention; both sit at the same relative depth, so document links
resolve identically from either. After editing the skill, run:

```powershell
python tools/sync_tutor_skill.py
```

`python tools/validate_workspace.py` fails if the two copies drift, so the mirror is a
checked invariant rather than a second file to remember. Vendored BMAD skills under
`.claude/skills/` remain local host conveniences and stay untracked.
