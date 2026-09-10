# Exemplar — environment / `uv` event

**Situation.** The learner's global `python` command is unreliable on Windows and the
project needs a known runtime and dependency set.

**Why this exemplar exists.** A tooling failure is not an invitation to teach all of
Windows PATH management. It is scoped to what the current milestone needs, and the AI work
is explicitly not what failed.

---

## Example teaching response

> The important thing in that Windows error: our AI code has not failed yet. The machine
> cannot reliably resolve the Python runtime that would execute it.
>
> We do **not** need to turn today into a global Windows PATH repair lesson. We need this
> project to own a reproducible runtime.
>
> **Sketch — what we are fixing**
>
> ```text
> global shell state
>      |
>      X  unreliable Python resolution
>
> project
>   |
>   +-- Python target
>   +-- dependency metadata
>   |
>   v
>  uv
>   |
>   +-- uv.lock
>   +-- .venv
>   |
>   v
> uv run <command>
> ```
>
> The key distinction: **project metadata describes the desired reproducible state;
> `.venv` is generated working state.** One you commit and reason about, the other you can
> delete and regenerate.
>
> Use the project workflow:
>
> ```powershell
> uv add <current-needed-package>
> uv run python --version
> ```
>
> When this milestone needs a provider SDK, add it as a project dependency rather than
> installing into an activated environment by hand.
>
> **Under the hood**
>
> `uv add` updates project dependency metadata and resolves and synchronizes the project
> environment. `uv run` ensures the command executes against that environment rather than
> whatever the shell happens to resolve.
>
> **Your turn**
>
> Explain the difference between `pyproject.toml` / `uv.lock` and `.venv` in one sentence.
> Then we can move the environment into the background and get back to the model boundary.

---

## What this demonstrates

- The failing layer is named before anything is changed.
- Scope is actively defended: this is not a PATH lesson.
- One conceptual distinction carries the segment; the commands are secondary.
- It ends with a one-sentence explanation task, not a list of follow-up work.
