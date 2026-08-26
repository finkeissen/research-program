research-program/RUN_DEFINITION.md
# Run Definition

## Purpose

This document defines what a "run" is
within the epistemic architecture (Layers 0–5).

It establishes the structural meaning of a run.

It does not define execution engines.
It defines epistemic status.

---

# 1. Definition

A run is:

> A formally bounded falsification attempt
> under explicitly declared structural conditions.

A run is not:

- mere execution
- logging
- simulation
- demonstration
- performance measurement

A run is an epistemic event.

---

# 2. Structural Characteristics

Every run must:

- declare its problem binding
- declare scope
- declare affected artifacts
- declare termination conditions
- preserve traceability
- preserve version binding
- preserve authority boundaries

A run without explicit binding is inadmissible.

---

# 3. Epistemic Function

Every run tests one or more of the following:

- a hypothesis
- a prediction
- a governance rule
- an admissibility constraint
- a structural invariant

Every run is therefore a falsification attempt.

If no falsification condition exists,
the run is ill-defined.

---

# 4. Test vs Run Distinction

A technical test verifies implementation behavior.

A run tests structural admissibility
or falsifies an epistemic claim.

Technical tests belong to enforcement layers.
Runs belong to the epistemic history.

---

# 5. Historical Status

Runs are:

- immutable
- audit-relevant
- historically persistent
- representable in the Matrix

A run cannot be edited after completion.
Corrections require a new run.

---

# 6. STOP Interaction

If a run triggers STOP:

- STOP must be recorded
- cause must be localized
- no silent repair permitted
- no implicit override permitted

STOP is a structural outcome,
not a failure of execution.

---

# 7. Authority Boundary

A run does not produce authority.

A run may:

- falsify
- survive
- expose conflict
- expose structural limits

Interpretation of results belongs to Layer 6.

---

# 8. Invariance Requirement

If runs begin to:

- legitimize artifacts,
- upgrade survival into truth,
- implicitly prioritize outcomes,

the architecture has failed.

Runs must remain diagnostic only.

