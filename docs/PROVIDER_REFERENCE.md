# Provider reference: documented syntax, not runtime proof

Reviewed 2026-09-15. Groq remains the recorded generation provider. Installed versions, account access, chosen model and successful execution must be observed in the learner's environment. Do not reset provider/onboarding from the uploaded template.

## Primary sources

[Compatibility](https://console.groq.com/docs/openai), [API reference](https://console.groq.com/docs/api-reference), [models](https://console.groq.com/docs/models), [quickstart](https://console.groq.com/docs/quickstart) and [Python SDK](https://github.com/groq/groq-python). Recheck version-sensitive behavior before implementation. [Python str documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) defines code-point semantics.

The documented Groq endpoint supports supplied n=1, not n=2. A choices list is a response-shape fact, not a promise of multiple supported completions. Empty/truncated/refused/invalid responses require explicit handling at the relevant lesson.

## Minimal first-call reference

Adapt to the actual existing learner file. This code was not executed against a provider by this delivery. The local environment must contain an authorized key and currently supported selected model. Timeout and disabled retries make one attempt visible; these settings are examples to inspect, not measured service objectives.

```python
import os
from groq import Groq

model_id = os.environ["GROQ_MODEL"]
client = Groq(api_key=os.environ["GROQ_API_KEY"], timeout=20.0, max_retries=0)
messages = [
    {"role": "system", "content": "Draft a support reply using only the supplied policy. Do not claim order lookup or completed actions."},
    {"role": "user", "content": "Message: An item in order 1042 arrived damaged. Policy: Ask which item was damaged before preparing a replacement."},
]
response = client.chat.completions.create(model=model_id, messages=messages, n=1)
if not response.choices:
    raise RuntimeError("The provider returned no choices")
content = response.choices[0].message.content
if not content:
    raise RuntimeError("The provider returned no reply text")
print(content)
```

Never print key values. If the project uses python-dotenv, load its local configuration before constructing the client; do not add a second system. GROQ_MODEL is a proposed configuration name, not proof it exists. Inspect the current setup before changes. Usage may be unavailable; unknown cost is not zero.

## Structured outputs and embeddings

At 0.7 verify selected-model support for the chosen JSON response mode. JSON object mode does not enforce schema, and neither schema nor JSON proves source truth. Use local malformed fixtures before spending a request on validation practice.

No Groq embeddings endpoint is established here. [DR-001](DECISIONS.md) is unverified after the official-reference check. At J3 select one documented local or hosted embedding route, record model/revision/dimensions/preprocessing/language scope and authorize any live verification. Generation and embedding providers need not match. This choice is not a first-call prerequisite.
