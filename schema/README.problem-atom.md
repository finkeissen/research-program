# Problem Atom — Admissibility Specification

## Purpose

This document defines the **minimal admissibility conditions**
for representing anything as a *problem* within this repository bundle.

It does not explain, justify, interpret, or evaluate problems.
It specifies only **what must be present** for a problem to exist at all.

---

## Scope

This specification applies uniformly to:

- all domains,
- all disciplines,
- all problem groups,
- all abstraction levels,
- all instances in the Matrix.

There are **no domain-specific variants** of this schema.

---

## Core Rule

A problem exists **if and only if**
it satisfies **all** admissibility conditions defined below.

If any condition is not met, the problem is **inadmissible**  
and processing **MUST STOP**.

---

## Admissibility Conditions

### 1. Atomicity

- A problem represents **exactly one** problem.
- It MUST NOT bundle multiple problems.
- It MUST NOT function as a container or category.
- Structural complexity may arise **only through relations** to other problems.

---

### 2. Symptom Requirement

- A problem MUST reference **at least one symptom**.
- A symptom is an observed or reported deviation or state.
- Symptoms MUST be represented as **references to other problem atoms**.
- Free-text-only symptoms are inadmissible.

---

### 3. Cause Requirement

- A problem MUST reference **at least one cause**.
- Causes represent hypothesized or observed conditions
  that may give rise to the symptom.
- Causes MUST be represented as **references to other problem atoms**.
- Missing causes are inadmissible.

---

### 4. Consequence Requirement

- A problem MUST reference **at least one consequence**.
- Consequences represent effects that may occur
  if the problem remains unbound.
- Consequences MUST be represented as **references to other problem atoms**.
- Missing consequences are inadmissible.

---

### 5. Relational Closure

- All symptoms, causes, and consequences MUST resolve
  to existing problem atoms.
- If a referenced problem does not exist,
  it MUST be created.
- Implicit or external references are inadmissible.

---

### 6. Epistemic Status

- Each cause MUST have an explicit epistemic status.
- Permissible statuses include:
  - observed
  - assumed
  - disputed
  - unresolved
- Causes without explicit status are inadmissible.

---

### 7. Temporal Admissibility

- The schema MUST allow causal ordering
  (cause → symptom → consequence).
- Underaction or non-action MUST be representable as a cause.
- No explicit timeline is required,
  but temporal direction MUST NOT be denied.

---

### 8. Responsibility Visibility

- A problem MUST allow explicit expression of responsibility
  or explicit non-assignability of responsibility.
- Hidden, implicit, or assumed responsibility is inadmissible.

---

### 9. Freedom / Binding Tension

- A problem MUST allow expression of:
  - zones requiring judgment (freedom),
  - zones requiring standards or constraints (binding).
- No decision, recommendation, or prioritization
  may be expressed at this level.

---

## Prohibitions

A problem atom MUST NOT contain:

- solutions or remedies,
- actions or tasks,
- optimization goals,
- priorities or rankings,
- scores or probabilities,
- utility or value functions,
- moral or psychological judgments,
- narratives or persuasive framing.

Presence of any prohibited element
renders the problem atom inadmissible.

---

## STOP Condition

If any admissibility condition is violated:

- the problem MUST NOT be instantiated,
- no approximation or substitution is allowed,
- no downstream processing may continue.

STOP is the correct and final outcome.

---

## Non-Goals

This specification does not:

- resolve problems,
- validate claims,
- rank alternatives,
- assign authority,
- produce decisions,
- guarantee completeness or correctness.

It defines **existence conditions only**.

---

## Binding Nature

This specification is **binding** for all downstream systems,
including MMS and the Matrix.

No component may override, relax, or reinterpret
these admissibility conditions.

