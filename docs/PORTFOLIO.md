# Portfolio and Junior Application Evidence

**Native adaptation:** 2026-09-08, from frozen V3.2 source 05. Status claims must follow [current evidence](../progress/evidence.jsonl) and [the progress protocol](PROGRESS_PROTOCOL.md).

## Initial package

Recommend two featured projects: the Medical Document Review Assistant and Retail Support and Order Assistant. They demonstrate different applied work and share transferable AI mechanisms. These are planned artifacts, not finished projects; neither is currently marked complete. Two is a curriculum recommendation, not a universal minimum demanded by employers.

| Project | Status | What the initial showcase should prove | Honest scope label |
|---|---|---|---|
| Medical Document Review Assistant | Planned; learner implementation not observed | Typed source-grounded extraction, missingness/negation, review workflow, measured field errors | Synthetic document-processing prototype; not clinically validated |
| Retail Support and Order Assistant | Planned; learner implementation not observed | Cited policy RAG, scoped order lookup, bounded tool/state flow and simulated approval | Synthetic support workflow; actions simulated |

## Artifact maturity is separate from visibility

- **A — Learning build:** small runnable slice, a few expected-vs-observed cases, explanation and a known failure. It can already be shown as learning work.
- **B — Demonstrable engineered project:** reproducible interface, focused boundary checks, honest held-out evaluation, independent modification/debugging and a readable README. This is the target for the initial featured portfolio.
- **C — Operational system:** deployment, access controls, monitoring, load/recovery, cost and rollback evidence for the actual environment. This is later work. Portfolio visibility does not imply C.

Do not label a repository production ready because it has Docker, many tests or a polished UI. Do not wait for maturity C to apply to suitable junior positions.

This route specializes in applied AI/LLM application engineering: provider boundaries, structured outputs, retrieval, scoped tools, evaluation and delivery. It does not by itself establish general data-science, ML-research, model-training, data-engineering, frontend-specialist, security-specialist or platform/SRE competence. Match each application to demonstrated evidence and add a targeted branch when a role depends on one of those areas.

## Evidence bundle for each featured project

1. Problem, intended user, input/output example and concise scope.
2. Data origin, synthetic-generation method or license, and what was manually reviewed.
3. Small architecture/dataflow diagram: deterministic code, model call, retrieval/data boundary and human decision point.
4. Reproducible setup with dependency lock, example environment variable names only, exact local run/demo commands, and a fake-data or fixture mode when provider access is unavailable. Clearly label prerecorded or mocked outputs.
5. Evaluation report: development/held-out split, expected-outcome rubric, sample size, model/config/date, counts and denominators, critical failures, language breakdown and limits. Include actual latency/cost only if measured.
6. Focused deterministic checks plus AI evaluation kept conceptually separate. Show at least one failed case and the change it motivated.
7. Brief design decisions, one credible alternative rejected for a stated reason, known limitations and a realistic next step.
8. Learner contribution and AI assistance disclosure, plus one independent change/debugging record. Preserve references to real commits/output where available.
9. A small observed usability note when practical: one person other than the builder attempts a normal task from the README/interface; record the task, hesitation or failure, and one resulting correction or explicit deferral. Do not coach the participant to manufacture success or present this as a formal usability study.

**A recorded demo is a required artifact, not an alternative to one.** Deployment is deferred to later work for good reasons, but the consequence has to be handled rather than inherited: a reviewer spending four minutes on a candidate does not clone a repository, install a package manager, supply their own provider key and run anything. Record two to three minutes showing one successful case, one missing or ambiguous case, and one controlled failure with an honest explanation. Label prerecorded or mocked output plainly. A hosted app remains an optional vacancy-specific extension; the recording is what actually gets watched. Never require reviewers to supply patient/customer data or send their secrets to an unknown service.

## Suggested measurements, never fabricated results

| Product | Core measurements | Failure evidence that matters |
|---|---|---|
| Medical | Field precision/recall or defined exact-match rubric; unsupported-fact count; source-span validity; review flag behavior | Missing vs negated facts, chronology, uncertain source text and valid-schema hallucinations |
| Retail | Classification correctness; retrieval Recall@k; citation/answer support; abstention; tool/workflow success | Wrong-customer lookup, missing order, wrong policy version, rejected action, repeated request and tool error |

Record the evaluation dataset size and ambiguity handling. Small synthetic evaluations show bounded engineering behavior, not clinical efficacy or proven commercial savings. If claiming a reduction in review time, measure it with an explicit baseline and comparable tasks; otherwise describe it as an intended benefit.

## Publication: which repositories go public

The curriculum workspace stays private. It holds learning state and evidence about a person, and nothing about it is portfolio material. The two product repositories have to be public, or the portfolio does not exist — a reviewer cannot evaluate what they cannot open.

Before making a product repository public, in this order:

1. Confirm no secret was ever committed, not merely that one is ignored now. `git check-ignore   .env` proves the current rule matches; it says nothing about history. Search the history   explicitly, and if a key was ever committed, rotate it — removing the file does not unpublish it.
2. Confirm every document, note, policy and order in the repository is synthetic, and that the   README says so in its first paragraph.
3. Keep the evaluation report in. Its limitations section is evidence of judgement, and removing   it to look stronger makes the portfolio weaker to exactly the readers worth impressing.
4. Keep the assistance disclosure in. Supported work honestly labelled reads as professional;   discovering it was undisclosed does not.

## Vacancy matching for Egypt and remote roles

Maintain a small list of current vacancies and revisit it as projects mature. Capture: employer/title/link/date, Egypt/on-site/hybrid/remote eligibility, experience/degree, English/Arabic requirements, must-have skills, preferred tools, evidence links and unresolved gaps. “Remote” alone does not mean applicants in Egypt are eligible. Listings may expire; verify before applying.

Use the route to prepare a strong applied core, then add short branches for repeated requirements in eligible roles. If target roles consistently require Docker/Azure or deeper ML, schedule a focused extension with actual practice; do not pretend this initial route covers it. Some junior titles still demand prior experience or a degree, and a portfolio does not erase those constraints.

Application checkpoint: can the learner reproduce the demo, explain every major boundary, make an unfamiliar change, debug a controlled failure, discuss measured limitations, show one small usability observation when available, and point to their own contribution? If yes and the vacancy's requirements fit the applied-LLM evidence actually demonstrated, apply while continuing selected later study. Never claim employment readiness solely from document validation.

Curriculum completion is a separate claim: J5 ownership gates (explanation, modification, debug and transfer) require actual learner evidence with assistance `none` or `docs`; execution may be supported. J5 readiness requires E01–E22 at least practiced; completion also requires E22 independently applied or stronger. A `ready` milestone with delayed transfer queued permits useful progress but does not certify retention or full route completion. Disclose assistance and pending transfer honestly when showing work; supported artifacts remain usable learning evidence.

## Resume bullets — fill only after measurement

- Built a synthetic medical document review prototype using [actual stack] to extract [defined fields] with source evidence; evaluated on [N] held-out cases and reported [measured results and important limitations].
- Developed a retail support assistant combining cited policy retrieval with scoped SQL order tools and human-approved simulated returns; demonstrated [actual workflow cases] and measured [actual quality/latency results].

Replace brackets with observed facts before use. State prototype/synthetic scope when relevant. Do not claim clinical validation, live refunds, real revenue gains, production scale or business adoption without evidence.

## What this package does not evidence

This route is solo by construction. Two synthetic-data prototypes, one author, no review history, no issue thread, no collaboration artifact. "Can this person work with other people" is a real screen and nothing here answers it — which is worth stating plainly, in the same spirit as every other limit named in this document, rather than letting the package look complete along an axis it never measured.

The cheapest honest evidence, if a target role weights it: one real issue thread, or one accepted contribution to something you did not write. Neither belongs on the critical path to a first application, and neither should delay one.

## Later portfolio expansion

Expand an existing product when a measured limitation or target role calls for it. An optional third independent project can demonstrate a missing capability such as SQL analytics or open-model adaptation. Do not require four to six repositories or every Q5-Q12 framework before the first application. Prefer a small number of explainable, evaluated projects over copied demos.
