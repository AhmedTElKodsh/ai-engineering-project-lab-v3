# Learning workspace

This repository contains curriculum, tutoring instructions, and portable learning evidence. The learner's application checkout is separate until verified in [current state](progress/current.json).

For a lesson, resume, explanation, debugging help, or assessment, use [ai-engineering-tutor](.agents/skills/ai-engineering-tutor/SKILL.md). Read current state before suggesting setup. Resume J0 / Q0 / 0.3 initially; onboarding is already complete as inherited context, while execution and understanding remain pending. Newer actual learner evidence overrides an older saved snapshot.

Honor the requested mode: **Learn** explains and returns one meaningful learner action; **Assess** gathers independent evidence without revealing the answer; **Build together** permits explicitly requested code help and records assistance. Direct questions receive direct answers. Ordinary lessons do not invoke BMAD Build automatically. Explicit maintenance, configuration, review, and publication requests execute as maintainer work without student assessments.

The native authorities are [teaching](docs/TEACHING_GUIDE.md), [route](docs/CURRICULUM.md), [engineering](docs/ENGINEERING_GUIDE.md), [evidence protocol](docs/PROGRESS_PROTOCOL.md), and [portfolio](docs/PORTFOLIO.md). Latest user direction controls scope. Saved state records facts; it does not override teaching policy. The V3.2 pack is a frozen archive, not a second active instruction set; see [migration](docs/MIGRATION.md).

Never fabricate learner evidence or award mastery from generated code/tests. Persist actual evidence before changing derived state, validate it, and report failed writes. Do not edit learner app files during ordinary tutoring unless requested. Provider calls and external actions require task-specific authorization; this workspace setup authorizes no provider calls. Use synthetic notes/orders, never request keys or patient data, and enforce authorization in application code when tools exist.

Preserve archived curriculum and installed vendor skills. Native maintenance check: `python tools/validate_workspace.py`; negative fixtures: `python tools/validate_workspace.py --self-test`. Both are standard-library, read-only checks and never execute learner apps. Static success proves no learner skill, provider behavior, or production readiness.
