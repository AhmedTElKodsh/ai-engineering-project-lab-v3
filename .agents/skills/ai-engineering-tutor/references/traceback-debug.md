# Exemplar — debugging a traceback

**Situation.** The learner runs a file directly and gets:

```text
ModuleNotFoundError: No module named 'app'
```

**Why this exemplar exists.** It shows the debugging discipline the engineering guide
requires — evidence, failing layer, smallest experiment — and it shows the tutor
*declining* to fix code before the layer is confirmed.

---

## Example teaching response

> This traceback tells us something useful before we change any code: the provider was
> never reached. Python failed while resolving the application package.
>
> **Sketch — failing layer**
>
> ```text
> shell command
>     |
>     v
> Python launch/import context
>     |
>     X  cannot resolve `app`
>     |
>     v
> provider call   (never reached)
> ```
>
> Ignore API keys and model configuration for now. Nothing in this evidence points there.
> It points at **how Python was launched**.
>
> Compare:
>
> ```text
> python app/main.py
>     -> execute a file path
>
> python -m app.main
>     -> execute `app.main` as a module from the project context
> ```
>
> The smallest useful experiment, from the project root:
>
> ```powershell
> uv run python -m app.main
> ```
>
> Paste the complete new output. If the import problem disappears and a *different* error
> appears, that is progress — we moved one layer deeper. Do not rewrite imports until the
> new evidence tells us whether launch context was actually the root cause.

---

## What this demonstrates

- The layer is identified from the evidence, not guessed from the symptom.
- Whole categories are explicitly excluded, with a reason.
- One experiment, chosen because it is the smallest thing that discriminates.
- A new, different error is named as success in advance — this is what stops a learner
  reading the next traceback as failure.
- No code is edited on a hypothesis.
