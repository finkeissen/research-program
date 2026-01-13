# CHANGELOG.md  
## Research Program — Transition from v0.4 to v0.5

**Status:** Draft / Pre-Release  
**Scope:** Epistemic architecture (research-program only)  
**Authority:** None  

---

## Purpose of This Changelog

This changelog documents **method-level and architectural changes**
between:

- **v0.4 — Guardrails (closed, binding)**  
and
- **v0.5 — Stresstest (current, experimental)**

It does **not** document:
- implementation details
- domain content completeness
- product readiness
- downstream systems (MMS, Matrix)

v0.5 is **not a release in the conventional sense**.  
It is an **evaluation and stress-testing regime**.

---

## Version Status Overview

- **v0.1 – v0.3:** closed (historical, architectural groundwork)
- **v0.4:** closed (guardrails, binding baseline)
- **v0.5:** current (stress-test phase, iterative, unstable)

v0.4 remains the **epistemic baseline**.  
v0.5 may change, reset, or fail without invalidating v0.4.

---

## Summary of Changes (v0.4 → v0.5)

### Added

#### Stress-Test Framing
- Introduction of **domain pressure tests**:
  - domains are used to stress epistemic limits,
  - not to validate or extend the program.
- Success criteria include:
  - explicit conflict,
  - STOP,
  - documented failure modes.

#### Physics as a Pressure Domain
- Physics is introduced deliberately as a **worst-case domain** due to:
  - hard empirical constraints,
  - constants and invariants,
  - non-derivability,
  - interpretive plurality.
- Physics is used to test whether the program resists:
  - authority creep,
  - empirical overreach,
  - ontological hardening.

#### Input Stratification
Clear separation of:

- **Facts / Inputs**
  - empirical constraints,
  - always scoped and uncertainty-tagged,
  - never authoritative.

- **Claims / Interpretations**
  - optional, replaceable lenses,
  - explicitly marked as contingent.

- **Drivers / Interfaces**
  - exported artifacts for other systems,
  - include STOP logic and scope declarations.

#### Explicit STOP Triggers for Empirics
- STOP conditions defined for:
  - misuse of empirical inputs,
  - conversion of inputs into ontological or epistemic authority.

---

### Changed

#### Handling of G2 (No External Empirical Grounding)

- **v0.4:**  
  - strict prohibition of empirical grounding.

- **v0.5:**  
  - replaced by a **controlled allowance**:
    - empirical statements may appear **only as tagged inputs**,
    - must declare scope and uncertainty,
    - must never function as proof, validation, or metaphysical commitment.

This change does **not** weaken v0.4.  
It tests whether v0.4 survives contact with empirical pressure.

---

### Clarified

#### Meaning of “Current”
- “Current” does **not** mean stable, recommended, or complete.
- It means:
  - actively tested,
  - expected to change,
  - allowed to fail.

#### Meaning of “Closed”
- “Closed” does **not** mean obsolete.
- v0.4 remains:
  - valid,
  - binding,
  - the reference point for coherence.

---

## Compatibility Notes

- v0.5 may introduce constructs that:
  - cannot be represented in v0.4
  - without violating guardrails.
- Such constructs must **not** be backported.
- Any empirically constrained content belongs in v0.5 or later only.

---

## Known Risks / Failure Modes (Tracked)

- **Authority creep**  
  Empirical inputs treated as metaphysical proof.

- **Scope collapse**  
  Local constraints generalized without justification.

- **Interpretation lock-in**  
  One physics interpretation hardens into doctrine.

- **Interface leakage**  
  Domain assumptions contaminate program-level primitives.

These are **expected risks**, not bugs.

---

## Planned Next Steps (Non-Binding)

- Establish a minimal **physics domain package**:
  - `facts/` — tagged empirical inputs
  - `claims/` — optional interpretive lenses
  - `drivers/` — export artifacts with STOP logic

- Run first pressure-test cases:
  - light speed
  - locality
  - Bell-type constraints

- Define **pass / fail criteria** for stress-tests:
  - including legitimate failure and STOP outcomes.

---

## Final Note

This changelog does **not** announce progress.

It documents **exposure to risk**.

v0.5 exists to test whether the research program
can remain epistemically disciplined
when confronted with domains that usually force authority.

Failure is an acceptable outcome.

