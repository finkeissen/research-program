# Pipeline Model (Normative)

## Purpose

This document defines the normative structure
of the compile pipeline across Layers 0–5.

It specifies phases and admissibility logic.
It does not define implementation.

The compiler must not introduce new norms.
It must only enforce existing ones.

---

# Entry Principle

Every compile process begins with a run-manifest.

The run-manifest is the only admissible entry point.

If no explicit run-manifest exists,
no compile process may begin.

---

# Normative Phases

1. Parsing
2. Static Semantics
3. Dependency Resolution
4. Execution Eligibility
5. Registration Eligibility

Each phase may either:

- PASS
- FAIL
- STOP

STOP is structural refusal, not error.
