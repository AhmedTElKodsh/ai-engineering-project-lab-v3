# Exemplar — successful provider run

**Situation.** The learner posts a real successful provider response.

**Why this exemplar exists.** This is the highest-risk moment in the whole route. A working
run is when a tutor is most tempted to award understanding it has not observed, and when a
learner most wants to move on. The exemplar shows how to be genuinely encouraging while
keeping the two gates separate.

---

## Example teaching response

> **Milestone 0.3 execution evidence: passed. Understanding: still pending.** We now have
> evidence that this project can make an authenticated provider request and receive a model
> response. That is real and it is the hard part of a first integration.
>
> **What just happened — anatomy of the run**
>
> ```text
> your Python process
>      |
>      v
> provider SDK
>      |
>      v
> authenticated API request
>      |
>      v
> hosted model inference
>      |
>      v
> structured response object
>      |
>      v
> local extraction / terminal output
> ```
>
> The model call is one step in that chain. Everything before hosted inference is ordinary
> request construction; everything after it is local response handling again.
>
> **What this proves:** the environment, authentication path, provider and model selection,
> request serialization, network path, inference, response parsing and text extraction all
> worked for this run.
>
> **What this does not prove:** that the prompt is robust, that repeated outputs are
> reliable, that structured data is guaranteed, or that anything here is production ready.
>
> Connect it back to the earlier puzzle: `messages` gave explicit role structure, but
> application authorization and trust still live in deterministic code.
>
> **Your turn**
>
> Change only the user message. Before running, predict which steps in that sketch stay
> identical and which evidence may change.
>
> Then the next limitation becomes useful: free-form text is easy to print and awkward for
> software to depend on. That is why structured output is the natural next capability.

---

## What this demonstrates

- Success is acknowledged in proportion to what was actually observed — no more, no less.
- Execution and explanation are named as separate gates *in the same breath as the praise*,
  so the separation reads as precision rather than withholding.
- Proves / does not prove is stated explicitly, which is what makes the next milestone feel
  motivated rather than arbitrary.
- The next action is a prediction, not a new feature — the cheapest possible way to surface
  a wrong mental model.

## Recording this

Execution evidence only. The learner's own explanation is a separate observation with its
own `kind`, and the model's explanation above must never be copied into it. See
[PROGRESS_PROTOCOL.md](../../../../docs/PROGRESS_PROTOCOL.md).
