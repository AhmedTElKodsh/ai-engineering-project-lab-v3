# Portfolio and Junior Application Evidence

**Native adaptation:** 2026-09-08, from frozen V3.2 source 05. Status claims must follow [current evidence](../progress/evidence.jsonl) and [the progress protocol](PROGRESS_PROTOCOL.md).

## Initial package

Recommend two featured projects: the Medical Document Review Assistant and Retail Support and Order Assistant. They demonstrate different applied work and share transferable AI mechanisms. These are planned artifacts, not finished projects; neither is currently marked complete. Two is a curriculum recommendation, not a universal minimum demanded by employers.

| Project | Status | What the initial showcase should prove | Honest scope label |
|---|---|---|---|
| Medical Document Review Assistant | Planned; learner implementation not observed | Typed source-grounded extraction, missingness/negation, review workflow, measured field errors | Synthetic document-processing prototype; not clinically validated |
| Retail Support and Order Assistant | Planned; learner implementation not observed | Cited policy RAG, scoped order lookup, bounded tool/state flow and simulated approval | Synthetic support workflow; actions simulated |

## Capture as you go, not at the end

The portfolio is a byproduct of the route, not its final phase. Each stage in [the route](CURRICULUM.md) ends with a capture step; this file is where those captures accumulate. Assembling a portfolio from memory after J5 is the slowest path to an application, and the numbers it needs are gone by then.

| After | Capture, while it is fresh | Why this one is persuasive |
|---|---|---|
| J1 | Recording of a successful extraction, a correctly flagged missing fact and one honest failure; the field counts and denominator; the first measured CV bullet | Source-grounded extraction with visible provenance is a specific, uncommon thing to be able to show |
| J2 | The retail schema beside the medical one, and a short note on what transferred and what the domain changed | Demonstrates generalization rather than one memorized pipeline |
| J3 | A cited answer, an abstention on an unsupported question, and one retrieval miss traced to its layer | A system that refuses to answer reads as engineering judgment; one that always answers reads as a demo |
| J4 | Normal lookup, blocked wrong-customer lookup, rejected approval producing zero effects | The refusals are the demo. Happy paths are assumed |
| J5 | Reproducible run commands, README, evaluation report with limits, contribution disclosure | This is assembly if the earlier captures exist, authorship if they do not |

Keep captures honest as they are made: label synthetic data, simulated actions, mocked outputs and prerecorded runs at capture time, not retroactively. A recording made during the stage is also the most reliable record of what the learner actually built themselves.

## When to start applying

Applications are not gated on route completion, and waiting for the whole route is a common, costly mistake.

- **After J1:** the CV, profile and repository carry one honest measured bullet. This is enough to start conversations and to find out what local and eligible-remote listings actually ask for.
- **From J3 onward:** apply to roles whose must-have list is already covered by demonstrated work. Which requirements those are is an open question this curriculum does not answer — collect the must-have lists from actual eligible listings and compare them against the route yourself. Do not take a coverage claim from any secondary source, including this document.
- **Throughout:** record uncovered requirements as `role_gaps` entries and convert repeated ones into short targeted branches. A requirement appearing in one listing is noise; the same requirement in five is a branch worth taking.

None of this changes eligibility. Degree, experience minimums, language requirements, location and work authorization are separate constraints that portfolio evidence does not remove, and "remote" alone does not mean applicants in Egypt are eligible. Verify before applying, and do not describe planned work as completed.

## Artifact maturity is separate from visibility

- **A — Learning build:** small runnable slice, a few expected-vs-observed cases, explanation and a known failure. It can already be shown as learning work.
- **B — Demonstrable engineered project:** reproducible interface, focused boundary checks, honest held-out evaluation, independent modification/debugging and a readable README. This is the target for the initial featured portfolio.
- **C — Operational system:** deployment, access controls, monitoring, load/recovery, cost and rollback evidence for the actual environment. This is later work. Portfolio visibility does not imply C.

Do not label a repository production ready because it has Docker, many tests or a polished UI. Do not wait for maturity C to apply to suitable junior positions.

## Evidence bundle for each featured project

1. Problem, intended user, input/output example and concise scope.
2. Data origin, synthetic-generation method or license, and what was manually reviewed.
3. Small architecture/dataflow diagram: deterministic code, model call, retrieval/data boundary and human decision point.
4. Reproducible setup with dependency lock, example environment variable names only, exact local run/demo commands, and a fake-data or fixture mode when provider access is unavailable. Clearly label prerecorded or mocked outputs.
5. Evaluation report: development/held-out split, expected-outcome rubric, sample size, model/config/date, counts and denominators, critical failures, language breakdown and limits. Include actual latency/cost only if measured.
6. Focused deterministic checks plus AI evaluation kept conceptually separate. Show at least one failed case and the change it motivated.
7. Brief design decisions, one credible alternative rejected for a stated reason, known limitations and a realistic next step.
8. Learner contribution and AI assistance disclosure, plus one independent change/debugging record. Preserve references to real commits/output where available.

Useful demo: show one successful case, one missing/ambiguous case and one controlled failure with an honest explanation. A short recording or local reproduction is sufficient for this curriculum; a hosted app may be a useful vacancy-specific extension. Never require reviewers to supply patient/customer data or send their secrets to an unknown service.

## Suggested measurements, never fabricated results

| Product | Core measurements | Failure evidence that matters |
|---|---|---|
| Medical | Field precision/recall or defined exact-match rubric; unsupported-fact count; source-span validity; review flag behavior | Missing vs negated facts, chronology, uncertain source text and valid-schema hallucinations |
| Retail | Classification correctness; retrieval Recall@k; citation/answer support; abstention; tool/workflow success | Wrong-customer lookup, missing order, wrong policy version, rejected action, repeated request and tool error |

Record the evaluation dataset size and ambiguity handling. Small synthetic evaluations show bounded engineering behavior, not clinical efficacy or proven commercial savings. If claiming a reduction in review time, measure it with an explicit baseline and comparable tasks; otherwise describe it as an intended benefit.

## Vacancy matching for Egypt and remote roles

This section owns how a vacancy is recorded and matched; the timing of a first application is above. Maintain a small list of current vacancies and revisit it as projects mature. Capture: employer/title/link/date, Egypt/on-site/hybrid/remote eligibility, experience/degree, English/Arabic requirements, must-have skills, preferred tools, evidence links and unresolved gaps. “Remote” alone does not mean applicants in Egypt are eligible. Listings may expire; verify before applying.

Use the route to prepare a strong applied core, then add short branches for repeated requirements in eligible roles. If target roles consistently require Docker/Azure or deeper ML, schedule a focused extension with actual practice; do not pretend this initial route covers it. Some junior titles still demand prior experience or a degree, and a portfolio does not erase those constraints.

Application checkpoint: can the learner reproduce the demo, explain every major boundary, make an unfamiliar change, debug a controlled failure, discuss measured limitations and point to their own contribution? If yes and the vacancy's requirements fit, apply while continuing selected later study. Never claim employment readiness solely from document validation.

Curriculum completion is a separate claim: J5 ownership gates (explanation, modification, debug and transfer) require actual learner evidence with assistance `none` or `docs`; execution may be supported. J5 readiness requires E01–E22 at least practiced; completion also requires E22 independently applied or stronger. A `ready` milestone with delayed transfer queued permits useful progress but does not certify retention or full route completion. Disclose assistance and pending transfer honestly when showing work; supported artifacts remain usable learning evidence.

## Resume bullets — fill only after measurement

- Built a synthetic medical document review prototype using [actual stack] to extract [defined fields] with source evidence; evaluated on [N] held-out cases and reported [measured results and important limitations].
- Developed a retail support assistant combining cited policy retrieval with scoped SQL order tools and human-approved simulated returns; demonstrated [actual workflow cases] and measured [actual quality/latency results].

Replace brackets with observed facts before use. State prototype/synthetic scope when relevant. Do not claim clinical validation, live refunds, real revenue gains, production scale or business adoption without evidence.

## Later portfolio expansion

Expand an existing product when a measured limitation or target role calls for it. An optional third independent project can demonstrate a missing capability such as SQL analytics or open-model adaptation. Do not require four to six repositories or every Q5-Q12 framework before the first application. Prefer a small number of explainable, evaluated projects over copied demos.
