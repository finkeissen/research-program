# Compile Phases (Normative Semantics)

## Phase 1 — Parsing

- Artifact format must be valid.
- Identifiers must conform to required patterns.
- Schema validation must pass.

Failure → FAIL

---

## Phase 2 — Static Semantics

- Integration contract must hold.
- Problem binding must exist.
- Scope must be declared.
- Termination conditions must exist.

Violation → STOP

---

## Phase 3 — Dependency Resolution

- All references must be explicit.
- All referenced artifacts must exist.
- Version binding must be explicit.

Unresolved reference → STOP

---

## Phase 4 — Execution Eligibility

- No authority transfer.
- No implicit role collision.
- No undeclared mutation.

Violation → STOP

---

## Phase 5 — Registration Eligibility

- Outputs must be declared.
- Provenance must be reconstructable.
- Version binding must be preserved.

Violation → FAIL
