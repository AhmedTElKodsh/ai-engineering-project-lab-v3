# Teaching exemplars

Worked examples of a complete teaching response. Load **one**, matched to the situation.
They are calibration, not a template to fill in and not text to paste at the learner.

| Situation | File |
|---|---|
| Learner asks a direct conceptual question | [conceptual-question.md](conceptual-question.md) |
| Environment, `uv`, Windows runtime or dependency event | [environment-event.md](environment-event.md) |
| First provider call, J0 milestone 0.3 | [first-provider-call.md](first-provider-call.md) |
| Learner posts a traceback | [traceback-debug.md](traceback-debug.md) |
| Learner posts a successful run | [successful-run.md](successful-run.md) |

## Provenance

Adapted 2026-09-09 from the Golden Exemplars in frozen V3.2 source
`06_Lesson_Generation_and_Learning_Cadence.md`. The [migration](../../../../docs/MIGRATION.md)
correctly dropped NotebookLM host formatting — required signposts, mandatory emoji, index
whitespace workarounds — but the exemplars themselves are not host formatting. They are the
only worked examples of the teaching contract in existence, and
[the acceptance criteria](../../../../_bmad-output/specs/spec-codex-learning-workspace/acceptance.md)
require that *"rich first-exposure instruction/inline explanation survives removal of
NotebookLM host formatting."* Restoring them here satisfies that clause.

## What to copy and what not to

Copy the **structure**: begin from the learner's actual event; separate the layers before
naming a cause; put a sketch where a relationship is otherwise invisible; keep intent
beside code rather than in a separate lecture; state what the evidence proves *and* what it
does not; end with one action that produces the next piece of evidence.

Do not copy the formatting. The emoji signposts of the original are gone deliberately and
[TEACHING_GUIDE.md](../../../../docs/TEACHING_GUIDE.md) is explicit that no host format
applies. Section labels below are plain by design.

Do not copy the content into a different situation. An exemplar for a traceback teaches
nothing about a successful run, and reusing its shape on the wrong event is exactly the
syllabus-first behavior the teaching contract prohibits.
