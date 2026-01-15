# OPERATIONS.md
## Operational Contracts for Matrix Worksteps

---

## Purpose

This document defines the **operational contracts** governing all worksteps
that lead to the creation, transformation, and revision of Matrix artifacts.

Its purpose is to ensure that matrix-related processes are:

- formally correct by construction
- reproducible and auditable
- robust against accidental error
- explicit about semantic uncertainty

This document does **not** define truth, correctness of content,
or epistemic authority.
It defines **conditions under which operations are admissible**.

---

## Scope

These operational contracts apply to all processes that transform
domain-specific knowledge-claims into Matrix artifacts, including:

- manual preprocessing
- semi-automated workflows
- fully automated MMS runs
- validation, build, and reporting steps

They apply across all domains and use cases.

---

## Pipeline Stages (Canonical)

Matrix-related work proceeds through the following stages:

1. **raw-materials**  
   Unstructured or weakly structured domain-specific knowledge-claims.

2. **pre-matrix**  
   Normalization, structuring, and schema alignment.
   No aggregation, resolution, or evaluation.

3. **matrix**  
   Explicit representation of epistemic elements, relations, conflicts,
   provenance, and temporal bindings.

4. **productive**  
   Derived views, exports, and representations based on a given Matrix state.

Each stage has **strict input and output expectations**.
No stage may silently compensate for violations in a previous stage.

---

## Operational Invariants (Hard Rules)

The following invariants **MUST hold** for any admissible Matrix run.

### Structural Invariants

1. All artifacts MUST be schema-valid.
2. All identifiers MUST be globally unique within a run.
3. All references MUST resolve (no dangling references).
4. No artifact MAY overwrite a previous version; revisions MUST be explicit.
5. Ordering of elements MUST be deterministic.

### Provenance Invariants

6. Every epistemic element MUST carry provenance metadata
   or an explicit `unknown` marker.
7. Provenance MUST be preserved across all transformations.
8. Loss of provenance information is a **FATAL error**.

### Epistemic Invariants

9. Conflicts MUST be represented explicitly, never resolved implicitly.
10. Absence of information MUST NOT be interpreted as negation.
11. No operation MAY introduce truth validation, ranking, or authority.

### Process Invariants

12. Identical inputs under identical conditions MUST produce identical outputs.
13. All operations MUST be reproducible from recorded parameters.
14. STOP conditions MUST be enforced when specified.

---

## Error Taxonomy

Operational issues are classified as follows:

### FATAL
- Schema violations
- Broken references
- Missing identifiers
- Provenance loss
- Non-deterministic behavior

→ The run MUST abort.

### INVALID
- Contract violations that do not break parsing
- Inadmissible transformations
- Unauthorized inference steps

→ The run MUST abort or be quarantined.

### WARN
- Ambiguous mappings
- Weak or minimal provenance
- High conflict density
- Incomplete normalization

→ The run MAY proceed, but warnings MUST be recorded.

### INFO
- Statistical summaries
- Novelty indicators
- Drift or change metrics

→ Informational only.

Errors MUST be reported explicitly.
Silent failure is not admissible.

---

## Operational Interfaces (Target State)

All implementations are expected to converge toward the following
conceptual operations:

- **validate**  
  Structural and contractual validation.

- **build**  
  Deterministic construction of a Matrix from admissible inputs.

- **report**  
  Generation of warnings, conflict summaries, and audit information.

These names define an **interface**, not an implementation.

---

## Non-Goals (Explicit)

This operational framework does **not**:

- determine truth or correctness
- resolve epistemic conflicts
- rank sources or claims
- generate recommendations or decisions
- collapse epistemic, operative, or instantiational layers

Any system performing such actions violates this contract.

---

## Relationship to Other Layers

- The **research-program** defines admissibility and STOP conditions.
- **MMS** implements these operational contracts.
- The **Matrix** reflects the contingent outcome of a compliant run.

No layer may assume responsibilities assigned to another.

---

## Final Note

If these operational rules appear restrictive,
they are operating as intended.

Their purpose is not to accelerate conclusions,
but to protect the conditions under which
epistemic work remains legitimate, revisable, and auditable.

