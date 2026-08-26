research-program/ACTOR_MODEL.md
# Actor Model

## Purpose

This document defines the structural actor model
for operations within Layers 0–5.

It defines admissible roles, their boundaries,
and the constraints that prevent authority transfer.

It does not define permissions as power.
It defines responsibility localization.

The actor model must ensure:

- no role becomes epistemically authoritative
- no execution role becomes normative
- no coordination role becomes interpretive
- no volume-based dominance under scale


---

# 1. Core Principle

Actors are operational entities.
They are not epistemic authorities.

No actor may:

- convert representation into endorsement
- convert survival into truth
- convert volume into relevance
- convert enforcement into normativity
- convert coordination into decision

Authority remains external (Layer 6).

---

# 2. Admissible Actor Roles

The following roles are admissible within Layers 0–5.

## 2.1 author

Creates or edits artifacts in:

- hypotheses/
- predictions/
- documentation (non-normative)

Constraints:

- must preserve identifiers
- must increment versions when meaning changes
- must maintain explicit problem binding
- cannot assert truth or authority inside artifacts

## 2.2 reviewer

Produces review artifacts:

- RUN_REVIEW.md
- STOP.md
- admissibility notes

Constraints:

- reviews are diagnostic, not authoritative
- must cite applicable rules
- may record PASS/FAIL/STOP only as structural outcomes
- cannot upgrade artifacts into authority

## 2.3 gateway

Enforcement role.

Responsibilities:

- schema validation
- contract enforcement (e.g., read-only)
- admissibility checks
- STOP triggering on violation

Constraints:

- cannot define rules
- cannot interpret results
- cannot resolve conflicts
- cannot prioritize artifacts

Gateway is enforcement only.

## 2.4 curator

Curates public showcase artifacts (e.g., `3.commit/`).

Responsibilities:

- selects representative artifacts
- preserves traceability
- ensures provenance exists for published exports

Constraints:

- curation does not imply endorsement
- selection does not imply truth
- curation must not remove conflict history
- cannot rewrite runs to fit narratives

## 2.5 archivist

Maintains legacy material:

- `0.legacy/`

Constraints:

- no admissibility guarantee
- cannot move artifacts upward without re-entry at Layer 1
- archival does not imply acceptance

## 2.6 observer

Reads artifacts and produces external interpretation.

Observer is structurally outside Layers 0–5.

Inside the system, observer may only be represented as:

"Actor X interpreted Y under context C at time T."

Observer outputs belong to Layer 6 authority.

---

# 3. Role Collisions

One human may occupy multiple roles,
but role boundaries must remain explicit.

If role collision occurs during a run:

- the run must declare actor role(s)
- outputs must record role context
- any ambiguity triggers FAIL or STOP

Implicit role switching is inadmissible.

---

# 4. Actor Claims and Authority

Actors may introduce claims.

Claims must be recorded as:

- contingent
- bounded
- attributable
- problem-bound

Actor attribution is mandatory for accountability.

Attribution does not create authority.

---

# 5. Concurrency Interaction

Under concurrency:

- actors do not gain priority by speed
- actors do not gain legitimacy by repetition
- actors do not gain authority by output volume

Any dominance mechanism constitutes:

- hidden prioritization
- implicit authority transfer

Such mechanisms are inadmissible.

---

# 6. STOP Interaction

If an actor attempts to:

- treat explanation as norm
- treat representation as endorsement
- bypass contracts
- rewrite admissibility rules

STOP must trigger.

STOP is structural refusal, not punishment.

---

# 7. Audit Requirements

For any run:

- actor role must be declared
- actor identity (if any) may be recorded
- role context must be reconstructable

If actor role cannot be reconstructed:

- run is inadmissible

---

# 8. Non-Authority Statement

No role inside Layers 0–5 can produce authority.

Roles can produce:

- artifacts
- constraints
- diagnostics
- representations

Interpretation, decision, and responsibility
remain external inputs and outputs (Layer 6).


