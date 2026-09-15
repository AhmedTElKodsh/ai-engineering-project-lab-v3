# SupportOps contracts: introduced at the relevant stage

These are adapted design decisions, not implemented services. The early tool does not require every type/table here. Start with simple functions and teach each boundary when its behavior appears.

## Intake and source truth: J1/J2

A small intake record has `case_id`, `order_reference: str | None`, `damage_reported: bool | None`, `requested_resolution`, `missing_information`, `claims`, and `review_flags`. A claim records field/value, source ID/type, quote and source range. Unknown is not false; a customer-stated order reference is not a verified order record. Resolve internal line identifiers through application data, not free-text invention.

Span coordinates are start-inclusive/end-exclusive Unicode code-point indices in the original, unnormalized Python string. `source[start:end] == quote` checks position, not semantic support. Byte positions and grapheme positions are different. Read UTF-8 and use consistent line endings before assigning positions. Preserve original text or explicitly map transformed coordinates back. Arabic combining marks remain part of the source string.

A human correction retains original value, corrected value, source and reason. Required/null/extra-field/strictness choices must be explicit and tested. JSON parsing, schema validity, quote resolution and source support are four different responsibilities.

J2 can use supplied customer and carrier statements with separate source IDs. Preserve disagreement instead of resolving it by vocabulary. A carrier statement that a parcel was delivered is evidence of the carrier's report, not conclusive proof of physical receipt. No carrier API is a prerequisite at this stage.

## Knowledge and operational records: J3/J4

Policy evidence carries document/section/chunk IDs, version, effective interval and locator. Similarity does not select authoritative policy. Filter eligible versions and access scope before model exposure. Retrieved snippets are untrusted evidence, not instructions. Record embedding model/revision/preprocessing identity when introduced.

Current order/stock/status comes from a narrow operational tool, not an old embedding. Preserve observation time and version. A timeout is not not-found. Trusted context supplies employee identity and allowed scope; a model-supplied customer ID or role cannot grant it. The employee is not necessarily the customer. Two synthetic scopes are enough to test denial before a full login/tenant platform exists.

## Fictional damaged-item policy: J4 action slice

The following are explicit sandbox choices adapted from the uploaded brief, not legal or commercial policy.

| Rule | Contract |
|---|---|
| BR01 | The report requests a damaged-item replacement; other intents do not authorize this write |
| BR02 | One identifiable small-appliance order line, quantity one, with known delivery time; otherwise clarify/escalate |
| BR03 | Case-created local calendar date minus delivery local calendar date in Africa/Cairo is 0-7 inclusive; missing/negative age needs review |
| BR04 | Accept the customer's damage statement for this simulation without calling it independently verified |
| BR05 | At least one available unit; no active/completed replacement for the scoped order line |
| BR06 | Use active policy at proposal creation; a policy change before execution invalidates the proposal |
| BR07 | Proposal expires after 15 minutes; a different authorized same-scope manager approves; recheck permission at execution |
| BR08 | Replies remain drafts; no email, shipping, refund or actual fulfillment integration |

Use a fixed clock in tests. Store UTC instants and compare intended local dates for BR03. The active-at-proposal rule is deliberate; switching to purchase-date policies requires a recorded decision, not silent retrieval behavior.

## Narrow tools and exact action approval

`get_order(reference)` injects trusted scope and uses a parameterized query. `check_inventory(sku)` returns scoped timestamped facts. `search_policies(question)` injects scope/version eligibility and bounds results. `prepare_replacement(line, reason)` resolves trusted records and creates only a pending proposal after deterministic checks. Execution is not a free-form model tool: the application validates authorized approval before the simulated effect.

State starts as proposed -> awaiting_approval -> approved or rejected -> succeeded or failed, with explicit stale/expired/superseded rejection reasons. Text saying approved is not an approval event.

Bind immutable proposal identity/version or digest to exact normalized arguments, target, scope, proposer, order/policy versions and expiry. Approval separately records its binding, manager and decision. An edit creates a new proposal. Immediately before the effect recheck permission, binding, expiry, freshness, eligibility, stock and duplicate state. Consume approval under the controlled execution boundary and retain the result.

Same idempotency key and same normalized payload returns its known result; changed payload conflicts. Also prevent a second replacement for the same scoped line under a different key. Local sequential correctness is not concurrency or distributed exactly-once evidence. If an external write is selected later, persist intent and reconcile unknown outcomes instead of blind retry or invented success. Durable queues, coordination and recovery belong to selected Q6/Q11 work.

## Later storage and interfaces

Use files and then SQLite as needed. Later entities include cases/messages, policy versions/chunks, orders/lines/stock, proposals/approvals/results and audit records. Add keys, uniqueness and migrations with actual persistence. PostgreSQL/pgvector is a candidate for demonstrated persistence/filter/update needs, not a J0 prerequisite.

J5 wraps existing functions with the smallest useful validated API/interface. Real authentication must precede public protected access. Resource denial must not disclose foreign data. The upload's full endpoint catalog, OIDC and worker architecture remain later reference designs, not requirements to close intake or search.
