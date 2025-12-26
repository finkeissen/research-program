# Transition: Mathematical → Computational

## Transition Type
Boundary Transition (Formal → Executable)

---

## Transition Statement

This transition defines the point at which
purely formal mathematical structures
are restricted to those that are
effectively representable and executable.

Any derivation that crosses from mathematics
into computation without satisfying the required constraints
is illegitimate.

---

## Purpose of the Transition

The purpose of this transition is to distinguish:

- formal definability
from
- formal executability

This transition prevents the conflation of
existence in a formal system
with the ability to carry out a procedure.

---

## Trigger Conditions

The transition is triggered when at least one of the following is required:

- execution of a procedure
- algorithmic generation of results
- automation of reasoning
- operational decision-making

At this point, mathematical reasoning alone is insufficient.

---

## Mandatory Constraints

To cross this transition, all of the following constraints must be satisfied:

- **Finiteness**  
  All representations, descriptions, and executions
  must be finite.

- **Discreteness**  
  All operations must proceed in discrete, well-defined steps.

- **Decidability**  
  The problem must admit a determinate outcome
  under the specified rules.

Failure to satisfy any constraint blocks the transition.

---

## Illegitimate Transitions

The following are explicitly forbidden:

- assuming computability from formal existence
- relying on non-constructive proofs
- invoking infinite precision or infinite time
- treating undecidable problems as solvable

Such transitions must result in STOP.

---

## Relation to STOP

If the transition cannot be completed due to
undecidability, non-termination, or unbounded resources,
the correct outcome is:

→ **STOP**

No approximation or optimization
can bypass this requirement.

---

## Epistemic Consequences

- Formal truth does not imply operational availability.
- Some mathematically meaningful questions
  cannot be answered computationally.
- Automation has principled limits.

Any system that ignores this transition
produces results without epistemic authority.

---

## Notes

This document treats the transition from
mathematical to computational reasoning
as a hard boundary of legitimacy,
not as a technical inconvenience.

