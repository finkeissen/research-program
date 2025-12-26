# Failure
## Kernel Panic, STOP, and Epistemic Breakdown

This text provides orientation on failure.
It explains why stopping is sometimes the only correct action.

It does not define error handling.
It clarifies legitimacy.

---

## Kernel Panic: Correct Failure

In operating systems, a kernel panic occurs
when the system detects a condition
from which safe continuation is impossible.

A kernel panic:
- is not a crash
- is not a bug by default
- is a protective halt

Continuing execution would cause:
- corruption
- undefined behavior
- loss of integrity

Stopping preserves correctness.

---

## Epistemic Failure: When Derivation Breaks

In epistemic systems, failure occurs when:
- constraints conflict irreducibly
- required information is missing
- further derivation would be arbitrary

At this point, continuation would:
- introduce assumptions
- hide uncertainty
- simulate knowledge

This is epistemic corruption.

---

## STOP as a First-Class Outcome

STOP is not an error message.
STOP is a valid result.

STOP indicates:
- that the system has reached its limit
- that no further justified derivation exists
- that responsibility returns to the human layer

STOP protects the system
from producing illegitimate output.

---

## Fail-Closed vs. Fail-Open

Fail-open systems:
- continue under uncertainty
- guess or optimize
- conceal limits

Fail-closed systems:
- halt when constraints are violated
- expose limits explicitly
- preserve integrity

The MMS is intentionally fail-closed.

---

## Why Failure Must Be Visible

Hidden failure produces:
- false confidence
- unjustified decisions
- misplaced responsibility

Explicit failure:
- maintains traceability
- preserves accountability
- enables revision at the correct layer

STOP is therefore a signal,
not a defect.

---

## Responsibility After STOP

When STOP occurs:
- the MMS does not decide
- the structure does not change
- evidence is not invented

Responsibility shifts to:
- i

