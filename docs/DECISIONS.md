# Decision records

Costly or cross-component choices get a short record in the format [ENGINEERING_GUIDE.md](ENGINEERING_GUIDE.md)
already specifies: context, decision, alternatives, evidence, consequences, review trigger.
A record states what was decided and on what evidence; it is not a claim that the decision
was executed or measured.

## DR-001 — J3 embedding route

**Status:** provisional default, decided 2026-09-09, **revised 2026-09-22** (the original
evidence was wrong; see below). Reopen at J3 entry.

### Context

[CURRICULUM.md](CURRICULUM.md) J3 says *"Use one embedding route and NumPy similarity"*
and never names it. [PROVIDER_REFERENCE.md](PROVIDER_REFERENCE.md) covers chat completions
and JSON Object Mode only. Meanwhile E09 in [skills.json](../progress/skills.json) requires
Arabic and English results reported separately, and J3 asks for cross-language retrieval
evaluation if used.

So the first genuinely cross-component choice on the route had no owner: which embedding
model, from which provider, at what setup cost, with what Arabic behavior.

### Decision

Default to **local embeddings through `fastembed`** (ONNX runtime, no PyTorch) with
`BAAI/bge-small-en-v1.5` for the first working J3 slice, English only. Treat Arabic
retrieval as an explicitly open risk to be decided with evidence, not now.

### Correction (2026-09-22)

The 2026-09-09 version chose "Groq's embeddings endpoint". **Groq does not list any
embedding model.** Its official models page lists chat, speech, TTS and guard models only;
the claim that it serves `nomic-embed-text-v1_5` came from a third-party API catalogue,
not from Groq. A learner following the old default would have hit a missing model on
their first J3 call and had no way to tell it from their own bug.

### Alternatives considered

| Option | Cost | Arabic | Why not the default |
|---|---|---|---|
| `fastembed` + `BAAI/bge-small-en-v1.5` | One dependency, ~67 MB download, no key, no rate limit | Weak — English-only model | **Chosen** for the first slice |
| `fastembed` + `paraphrase-multilingual-MiniLM-L12-v2` | Same dependency, ~220 MB download | Designed for it | The measured comparison, not the starting point: one model name away once the English baseline exists |
| `sentence-transformers` | Pulls PyTorch (large install) | Depends on model | Heavy install before the mechanism is understood |
| Hosted embeddings (a second provider) | New key, billing or free-quota limits, new client | Varies | Two provider boundaries while learning the first one |
| Groq embeddings endpoint | — | — | Not available (see Correction) |

### Evidence

Checked 2026-09-22, no provider or model call made:

- Groq's [models page](https://console.groq.com/docs/models) lists production models
  `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `openai/gpt-oss-120b`,
  `openai/gpt-oss-20b` and two Whisper models, plus preview chat/TTS/guard models. No
  embedding model.
- `fastembed`'s [supported models](https://qdrant.github.io/fastembed/examples/Supported_Models/)
  include `BAAI/bge-small-en-v1.5` (384 dimensions, 0.067 GB) and the multilingual
  `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384 dimensions, 0.22 GB)
  and `intfloat/multilingual-e5-large` (1024 dimensions, 2.24 GB).
- Same dimension (384) for the English default and the small multilingual model, so the
  comparison changes one string and nothing downstream.

Sources: [Groq supported models](https://console.groq.com/docs/models),
[fastembed supported models](https://qdrant.github.io/fastembed/examples/Supported_Models/),
[Arabic–English RAG embedding comparison](https://hosn.om/blog/bilingual-rag-embeddings-arabic-english.html).

Install behaviour on the learner's machine and actual retrieval quality on this corpus are
unverified. This is a documentation check, exactly as scoped in
[PROVIDER_REFERENCE.md](PROVIDER_REFERENCE.md).

### Consequences

The English J3 slice costs one new dependency and a small download, but no key, no quota
and no second provider boundary. That is the smallest honest cost now that no hosted
zero-setup route exists, and it keeps the route's rule about one mechanism at a time:
the learner meets embeddings, not a new provider.

**Arabic retrieval on this route is expected to underperform, and that is a tooling
property, not a learner failure.** This is the consequence that matters. Without this
record, a learner whose Arabic Recall@k comes back poor has no way to tell a bad chunking
decision from a bad embedding model, and the available conclusion — *"I don't understand
embeddings"* — is both wrong and the likeliest to end the project.

State this before the Arabic evaluation runs, not after it disappoints.

### Review trigger

Reopen when **either** condition holds:

1. Labeled Arabic questions exist and measured Arabic Recall@k is materially below the
   English figure on the same content. `note_001` / `note_007` in
   [fixtures](../fixtures/medical/CASES.md) are the same pattern for extraction and show
   how the comparison is built: same facts, two languages, scored separately.
2. A target vacancy requires demonstrated Arabic retrieval quality.

On either trigger, evaluate a multilingual model (start with
`paraphrase-multilingual-MiniLM-L12-v2`) against this baseline on the same labeled
set and keep whichever is justified. Do not switch models on intuition; the point of the
baseline is to make the switch measurable.
