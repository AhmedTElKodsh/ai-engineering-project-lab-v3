# AI Engineering Project Lab V3

A learner-owned Codex workspace for building a Medical Document Review Assistant and a Retail Support and Order Assistant. This repository currently contains the curriculum and learning state; neither learner application has been observed here.

Open this folder as the project and ask **“Resume my lesson”** or **“Use $ai-engineering-tutor to resume.”** The initial saved position is **J0 / Q0 / 0.3 — first Groq SDK call**, with execution and understanding pending. The tutor first reconciles your latest output and the application location. It should not repeat onboarding or install the full tool stack.

A fresh lesson thread may be needed for the skill picker to refresh after installation. [AGENTS.md](AGENTS.md) also points directly to the project skill file, which the agent can read even before picker discovery refreshes.

Useful requests:

- “Learn: explain this response object and help me continue.”
- “Assess: test my understanding of the current mechanism.”
- “Build together: help me write this specific function.”
- “Save a checkpoint from today's actual evidence.”
- “Maintain this workspace: validate the guides and state.”

Learner questions are answered directly. Assessment answers are withheld until you attempt them or request help. Explicit maintainer work runs normally and does not become a student exercise.

Start with [the route](docs/CURRICULUM.md), [teaching guide](docs/TEACHING_GUIDE.md), and [current state](progress/current.json). [Progress protocol](docs/PROGRESS_PROTOCOL.md) explains evidence and resumption. [Provider reference](docs/PROVIDER_REFERENCE.md) retains a dated baseline, not a current runtime claim. [Portfolio](docs/PORTFOLIO.md) distinguishes planned work from demonstrated results. [Migration](docs/MIGRATION.md) maps all seven frozen sources to native authorities.

From this repository's root, with Python installed:

```powershell
python tools/validate_workspace.py
python tools/validate_workspace.py --self-test
```

These commands use only the standard library, need no secrets/network/provider, and never launch the learner's app. The [pilot](docs/PILOT.md) distinguishes static checks, tutor simulations, and real learner outcomes. Maintainers can request BMAD explicitly; [the planning contract](_bmad-output/specs/spec-codex-learning-workspace/SPEC.md) and its companions describe this setup. Do not treat generated planning artifacts as completed student projects.

The V3.2 source pack and prior QA remain under [curriculum](curriculum/V3.2_Medical_and_Retail_Junior_Path/README_FIRST.md) as a frozen archive. Native guides own current teaching. Keep publication private unless the user later explicitly changes that scope; GitHub publication does not activate providers or establish learning progress.
