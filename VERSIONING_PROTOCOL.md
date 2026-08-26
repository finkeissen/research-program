VERSIONING_PROTOCOL.md
# Versioning Protocol

## Purpose

This document defines structural versioning rules
across all architectural layers (0–5).

It does not introduce epistemic authority.
It defines artifact mutation boundaries.

Versioning must preserve:

- traceability
- responsibility localization
- non-transfer principle
- STOP integrity
- structural invariance under scale


---

# 1. Identity vs Version

Identity is immutable.

Version is mutable.

Identity examples:

- H001
- P001
- RUN-2026-02-001
- CLM-2026-001

Identity must never change.

If identity changes, a new artifact must be created.

Version changes must not alter identity.


---

# 2. Layer-Specific Version Rules

## Layer 0 — legacy

Artifacts may evolve.
No admissibility guarantees.
No structural versioning constraints required.

---

## Layer 1 — research-program

Normative documents may be versioned.

Constraints:

- Changes require explicit revision marker.
- Invariants must remain stable unless formally replaced.
- If invariants change, all lower layers require re-evaluation.
- Revision must be documented.

Layer 1 changes may invalidate prior runs.

---

## Layer 2 — MMS

Schemas and integration contracts may be versioned.

Constraints:

- Schema changes must not silently invalidate prior artifacts.
- Backward compatibility must be declared.
- Breaking changes require explicit major version increment.
- Gateway enforcement logic must reflect declared schema version.

---

## Layer 3 — Matrix

Claims:

- claim_id is immutable.
- status may change.
- content edits require version increment.
- silent edits are forbidden.

Permitted status changes:

- active → superseded
- active → invalidated
- active → retracted

Original content must remain auditable.

---

## Layer 4 — hypotheses

Rules:

- hypothesis ID (H###) immutable.
- statement edits require version increment.
- falsification criteria edits require version increment.
- scope edits require version increment.
- assumptions edits require version increment.

Falsification does not delete.
It updates status.

If core meaning changes substantially,
a new hypothesis ID must be created.

---

## Layer 5 — predictions

Rules:

- prediction ID (P###) immutable.
- operationalization edits require version increment.
- evaluation criteria edits require version increment.
- scope changes require version increment.

Evaluation outcomes do not change prediction identity.

---

# 3. Run Versioning

Runs are immutable.

A run cannot be edited after completion.

If correction is required:

- a new run must be created
- previous run remains as historical artifact

Reports may only append corrections
with explicit correction section.

Silent rewriting is forbidden.

---

# 4. Traceability Preservation

Versioning must preserve trace chain:

H → P → RUN → Outputs

If a hypothesis version changes:

- predictions referencing it must declare version bound
- new predictions may reference new version
- old predictions remain historically valid

No implicit upgrade permitted.

---

# 5. STOP Interaction

If a Layer 1 invariant changes:

- all lower layer artifacts must be reviewed
- affected runs may be marked structurally outdated
- no automatic upgrade

STOP triggered by version conflict must halt execution.

---

# 6. Non-Transfer Safeguard

Versioning must not:

- introduce authority
- erase historical responsibility
- collapse conflict history
- rewrite falsification events
- retroactively justify outcomes

Versioning is structural.
It does not legitimize.

---

# 7. Breaking Changes

Breaking changes occur when:

- identifier format changes
- admissibility rules change
- STOP semantics change
- integration contract changes
- schema removes required field

Breaking changes require:

- explicit major version increment
- compatibility declaration
- audit log entry

---

# 8. Audit Requirements

Every version increment must record:

- timestamp
- author (actor)
- reason
- affected layer
- compatibility note

Version logs must be append-only.

---

# 9. Structural Invariance Requirement

If versioning becomes necessary
to maintain scale stability
by introducing hidden rules,
the architecture has failed.

Versioning must preserve invariants.

---

# 10. Authority Boundary

Versioning does not create authority.

Interpretation of version consequences
belongs exclusively to Layer 6.

All artifacts remain non-authoritative.


