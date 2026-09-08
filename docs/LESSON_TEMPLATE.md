# Lesson template

The required shape for a first-exposure lesson. [Teaching](TEACHING_GUIDE.md) defines the moves this template arranges; [the route](CURRICULUM.md) chooses the mechanism; [assessment cards](ASSESSMENT_CARDS.md) own the acceptance cases. Follow this whenever a new mechanism is introduced.

## When this applies, and when it does not

Use the full shape for **the first exposure to a new mechanism** — a provider call, structured extraction, embeddings, tool calling, an approval state machine.

Do not use it for: a direct question, which gets a direct answer; a familiar edit, which gets the precise delta and affected path; a debugging exchange, which follows expected-versus-observed to the failing layer; or a resume where the learner is mid-task. Applying the full template to a two-line question is the ceremony this curriculum exists to avoid. Sections may be compressed or dropped when the mechanism is small — the napkin, the ladder position and the keyboard ending are the three that should survive almost any compression.

## The shape

### 1. Orientation — three or four lines, no more

Where the learner is, the objective, the evidence this session should produce, and a provisional time estimate labelled as provisional. Never a full header block, never a recap of the route. If there is an unresolved reconciliation — app location, a previous failure, contradictory saved state — resolve or surface it here in one sentence, then move.

### 2. The napkin sketch — before any code

At most seven boxes, arrows for data movement, a marked line wherever trust, determinism or ownership changes. Invite the learner to draw it themselves before reading on. When the system already has a sketch, redraw it with the new box added and say what changed. The sketch comes before the explanation, not after it as an illustration.

### 3. The café explanation — the substance

Explain as a colleague would over coffee. Second person, short sentences, contractions. It must contain, in some order:

- the mechanism itself, stated plainly;
- **the objection the learner is about to raise, voiced in their words and answered** — not deflected;
- one analogy, immediately followed by where the analogy breaks;
- the aside that actually matters: what bites people here, what is commonly skipped, what is worth being suspicious of.

Casual register, exact content. Every name, index, key, argument and ordering stays precise.

### 4. One or two detail dives — all the way down

Pick the one or two things that will otherwise become a recurring confusion, and go to the actual mechanism: name the specific thing, state the misconception it corrects, and say what would be observably different if it worked the other way. Two dives is the ceiling. Do not narrate obvious syntax, and do not dive on something the learner did not touch.

### 5. Ladder position — a small table

Show the rungs for this mechanism, mark the current one, name what each next rung adds, and map rungs to milestones. Difficulty the learner can see is difficulty the learner can survive. One new difficulty per rung; never present two.

### 6. Land on the keyboard

Show only the load-bearing lines — the few that carry the new idea — with the rest named as scaffolding that can be ignored for now. On genuine first exposure a full annotated worked example is appropriate and should carry its Role/Connections note; on later rungs show the delta instead of replaying the file.

Then, before the command: **ask for two or three written predictions.** Output shape, rough timing, whether a repeat differs, what a specific deliberate break would raise. Predictions come before the run because they are impossible afterwards.

Then the exact command to run, in its own fenced block, and a clear statement of what to bring back: the exact command, the exact output, the predictions including the wrong ones. Say plainly that a traceback is a valid result. Say plainly that the assistant is not running it, and why: it is the learner's evidence and generated output cannot satisfy an execution gate.

### 7. Optional practice — offered in a few lines, never assigned

Offer break-it-on-purpose, explain-it-back and reconstruct-from-blank as the learner's choice, marked optional in plain words. Predicting the failure first is part of break-it-on-purpose.

If the learner skips them, continue without comment and without re-offering the same check next turn. A skip is not a gap, a refusal, or evidence of anything. Never make the next lesson contingent on an optional check, and never reintroduce one as homework.

### 8. One closing question, and what it is for

End with a single question that will genuinely test understanding — the tutor-posed one that can satisfy the explanation gate — and say that it comes *after* the output arrives, not now. One open question, never a task list.

## Rules that override the shape

- **One mechanism per lesson.** If two new ideas are needed, the lesson is too big; split it.
- **One action at the end.** One action does not mean one line of instruction — explain thoroughly, then ask for one thing.
- **Never open with setup.** If installation or configuration is unavoidable, put it after the learner sees why it is needed, and collapse it out of the main path.
- **A direct question ends the template.** Answer it directly and sufficiently, then return to where you were.
- **Verify before showing exact syntax.** Provider, SDK, model and API details are checked against current primary documentation, or labelled unverified with the durable mechanism taught anyway.
- **No files created on the learner's behalf** during ordinary tutoring unless requested, and no provider calls made for them.
- **Stop somewhere resumable.** End on a passing case, a written-down failure or a committed change — never mid-refactor.

## Self-check for the assistant before sending

Napkin before code · objection voiced and answered · analogy bounded · at most two dives · rung named · predictions requested before the command · exactly one action · optional practice marked optional · one closing question · nothing invented about the learner's evidence.
