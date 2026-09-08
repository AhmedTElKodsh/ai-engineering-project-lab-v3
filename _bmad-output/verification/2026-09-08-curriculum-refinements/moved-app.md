# Isolated tutor simulation: moved-app

Synthetic maintainer evaluation; not learner evidence. Agent: `/root/sim_moved`. Date: 2026-09-08. Exact prompt is case `moved-app` in `cases.json`.

## Actual response

I’m using the ai-engineering-tutor skill to resume from your latest situation. Your report that the app moved takes precedence over the saved snapshot; its current location is unverified.

Our immediate focus is finding that folder so we can inspect the app as it exists now. The saved lesson point is **J0 / Q0 / 0.3, the first Groq call**, with execution and understanding still pending in the record. We can reconcile that with your actual work once the app is located.

**One action:** open File Explorer, locate the folder you moved the app into, and copy its full path from the address bar into your reply. The expected evidence for this step is just the folder path; terminal output can wait. Allow roughly 2–5 minutes if you remember the destination.

## Inspection and limits

Inspected AGENTS.md, tutor SKILL.md, current.json, teaching/protocol/curriculum guides, evidence.jsonl and skills.json using Get-Content batches; recovered protocol/evidence/initial skills after truncation. No app directory located or inspected; no execution, writes or provider calls.

## Root evaluator judgment

PASS: latest relocation report is accepted, location remains unverified, one feasible action asks for the actual folder, no guessed launch command or reset to onboarding. This test starts from the real unverified initial snapshot; it does not simulate an already-verified stale path on disk.
