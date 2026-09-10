# Exemplar — first provider call (J0 milestone 0.3)

**Situation.** The learner is at Q0 / 0.3 with Groq selected and a working project runtime.

**Why this exemplar exists.** This is the current active milestone. It shows the shape of a
first-exposure segment: one new mechanism, the boundary made visible, intent beside code,
and a trace before any evidence is claimed.

**The code lives in [PROVIDER_REFERENCE.md](../../../../docs/PROVIDER_REFERENCE.md), not
here.** Read the exact syntax there and verify it against current official documentation
before presenting it as executable. This file owns the teaching wrapper around it; keeping
one copy of the code means the two cannot drift.

---

## Example teaching response

> We now have the capability we were missing: a project-owned Python runtime. The next
> boundary is the one this milestone actually cares about — **local application → provider
> API → model inference → parsed response → local code**.
>
> This connects directly to the earlier prompt-injection puzzle. There, labels and user
> text were flattened into one Python string. Here the request carries explicit `system`
> and `user` message roles. That gives the provider explicit role semantics — and it is
> still **not** a hard security boundary.
>
> **Sketch — what actually lives where**
>
> ```text
> LOCAL PYTHON PROCESS
>    |
>    +-- your main module
>    |     | build messages
>    |
>    +-- Groq SDK/client
>          |
>          | authenticated HTTPS request
>          v
>       GROQ API / HOSTED MODEL
>          |
>          | probabilistic inference + HTTP response
>          v
>    +-- SDK parses response into Python objects
>    |
>    +-- your module reads first choice -> message -> content
> ```
>
> The boundary that matters is the network call. The SDK itself is ordinary library code
> running inside your local Python process — nothing about importing it is remote.
>
> Your module has three responsibilities today: configure the client, send one structured
> request, extract one returned message. The intent stays beside the code so the file reads
> top to bottom without jumping to a separate lecture.
>
> *[Present the annotated code from PROVIDER_REFERENCE.md here, verified against current
> official documentation.]*
>
> **The lines carrying the new idea**
>
> Three, and the rest can be ignored for now:
>
> ```python
> response = client.chat.completions.create(...)   # crosses the boundary, waits
> first_choice = response.choices[0]               # choices is a list; [0] is not decoration
> response_content = first_choice.message.content  # the text, finally
> ```
>
> The compact form is `response.choices[0].message.content`. We are writing it in three
> steps first because each hop is a real object with a real reason to exist. The index
> operation is essential and never optional — the API returns a *list* of choices because
> it can return more than one.
>
> **Trace before you run**
>
> Load configuration → create client → serialize model and messages → authenticated request
> → wait → hosted inference → HTTP response → SDK parses to Python objects → select
> `choices[0]` → read `.message.content` → print.
>
> Expected: one short paragraph of text on your terminal. Python execution never moved into
> the model; it waited.
>
> **Your turn**
>
> Run it and paste the complete actual output.

---

## What this demonstrates

- One new mechanism, connected to a limitation the learner already felt.
- The sketch carries the local/remote split that prose alone hides.
- Attention is steered to three lines out of thirty.
- A dense idiom is decomposed *before* being compressed.
- It ends waiting for evidence, not asserting success.
