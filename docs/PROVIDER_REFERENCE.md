# Dated provider reference

The first-call baseline is the inherited Groq snapshot reported checked on **2026-09-06** in frozen V3.2 source 03. Its initial adaptation did not reverify runtime. The separate JSON decision below was checked against official documentation on **2026-09-08** without a provider call. Installed versions, account access and actual learner execution remain unknown. Do not label this a currently verified working setup.

## Known choices and unknown runtime

| Component | Inherited reference | Current local evidence |
|---|---|---|
| Workflow | uv; Python target 3.12 | Installed app interpreter/uv versions unknown |
| Provider / SDK | Groq / groq | Installed SDK version unknown |
| Environment loader | python-dotenv | Installed version unknown |
| Key variable | GROQ_API_KEY | No secret value requested or observed |
| Model baseline | llama-3.3-70b-versatile | Reported checked 2026-09-06; availability not reverified |
| Call shape | client.chat.completions.create(...) | Dated reference, non-streaming |
| Response | choices list -> first choice -> message -> content | Required zero-index semantics retained |

Sources named by the archived first-call snapshot: Groq Quickstart, API Reference, Text Generation guide and the model page. The JSON decision below has its own verification scope. At lesson time verify current official documentation and reconcile the actual project versions before presenting executable guidance. If verification is unavailable, teach the durable mechanism and explicitly retain the unverified label.

## Baseline teaching code

This is reference code, not an app created in this repository. The learner code location starts null/unverified in [current state](../progress/current.json). Inspect the actual app directory before using the inherited `app/main.py` shape. Preserve an existing attempt rather than silently replacing it.

```python
"""
Role:
This module is the smallest provider-boundary experiment in Quest 0. It owns
client creation, one structured chat request, and local extraction of the first
returned message.

Connections:
.env -> Groq client -> chat request -> Groq-hosted model -> SDK response object
"""

from dotenv import load_dotenv
from groq import Groq

# Intent / pseudocode
# 1. Load local secret configuration into the process environment.
# 2. Create the provider client.
# 3. Send one system message and one user message.
# 4. Receive the SDK's parsed response object.
# 5. Select the first returned choice and print its message content.

load_dotenv()

client = Groq()
MODEL = "llama-3.3-70b-versatile"

# Provider boundary: the Groq SDK runs inside this local Python process.
# This synchronous call sends an authenticated network request and waits while
# the remote provider performs model inference.
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a concise learning assistant.",
        },
        {
            "role": "user",
            "content": (
                "Explain the boundary between deterministic application logic "
                "and probabilistic model behavior in one short sentence."
            ),
        },
    ],
)

# Response anatomy: expose each semantic hop before using the compact idiom.
# `choices` is a list, so `[0]` selects the first returned choice.
first_choice = response.choices[0]
assistant_message = first_choice.message
response_content = assistant_message.content

print("\n--- Model Response ---")
print(response_content)
```

`response.choices[0]` selects the first choice; the next two lines expose message and content. The compact equivalent is `response.choices[0].message.content`. V3.2 used spaces inside `[ 0 ]` for NotebookLM rendering; both forms have the same Python meaning. Codex does not require that host workaround. The index operation itself is essential.

The local SDK serializes model/messages into a request; the synchronous call waits across a network/provider boundary; hosted inference produces a response; the SDK parses it into Python objects; local Python extracts and prints text. Python execution does not move into the model. Structured system/user roles are not a hard security boundary.

## JSON experiment decision — documentation checked 2026-09-08

For J0 0.7/J1, retain `llama-3.3-70b-versatile` as the baseline and explicitly request **JSON Object Mode** using `response_format={"type": "json_object"}` in `client.chat.completions.create(...)`. The model page lists JSON Object Mode. This is a documentation capability check, not account availability or runtime proof. [Groq model documentation](https://console.groq.com/docs/model/llama-3.3-70b-versatile).

Include an explicit instruction to return a JSON object and describe the expected fields/null behavior in the messages. JSON Object Mode targets valid JSON syntax; it does not enforce the application schema. The checked Structured Outputs model list does not include this baseline for `json_schema`; do not assume `strict: true` support. Recheck the selected model before choosing a different mode. [Groq structured-output documentation](https://console.groq.com/docs/structured-outputs).

After inspecting `response.choices[0].message.content`, reject absent or incomplete content rather than replacing it with an empty success object. Parse locally with `json.loads`, validate the parsed value against the chosen schema, then check source truth separately. In Pydantic v2, `Model.model_validate(...)` validates a parsed object and `Model.model_validate_json(...)` combines JSON parsing and model validation; configure strictness, required/null fields and extra-field policy deliberately. Neither verifies that a fact occurs in a note. [Pydantic model validation documentation](https://docs.pydantic.dev/latest/concepts/models/).

Use a tiny synthetic note and a local hand-written malformed/type-invalid payload to expose distinct parse, schema and source-fidelity failures. No provider request is needed to exercise those local checks. Preserve valid failure evidence; do not retry blindly or silently coerce an unsupported fact. This note is a teaching decision, not learner evidence, package installation or permission to call the provider.

## Conditional commands and evidence

Only in a confirmed learner app root, if these dependencies are not already declared, the inherited command is `uv add groq python-dotenv`. Only if the package/module exists, the inherited run command is `uv run python -m app.main`. These commands have not been executed for the learner by this setup. A provider call needs explicit authorization if the agent is to run it; the learner may run their own authorized experiment. Never request the API key value or patient data.

Expected evidence is the actual command and output showing the model response/extraction. Observed evidence remains pending. A successful run alone supports execution, not the learner's boundary explanation, quality, reliability, structured output guarantees, or production readiness. See [progress protocol](PROGRESS_PROTOCOL.md).
