# Domain Boundaries — Legal Law

This document defines **where the Legal Law domain stops**.

Boundaries are not “edge cases”.
They are part of the contract that prevents
silent norm propagation and category errors.

---

## Non-Goals

This domain does not attempt to:

- determine moral rightness or ethical justification
- provide political legitimacy or policy desirability
- recommend actions or strategies
- assign responsibility or blame
- predict enforcement outcomes
- optimize for compliance, efficiency, or social welfare
- replace qualified legal professionals
- guarantee legal correctness

---

## Invalid Inferences

The following inference patterns are invalid within this domain:

- **Legal validity ⇒ moral legitimacy**
- **Legal permission ⇒ recommendation**
- **Legal prohibition ⇒ impossibility**
- **Legal classification ⇒ responsibility attribution**
- **A single source ⇒ complete legal status**
- **A general statement about law ⇒ jurisdiction-independent truth**
- **Silence in sources ⇒ permission** (unless explicitly supported)

---

## Known Category Errors

Common category errors include:

- confusing legal “ought” with moral “ought”
- treating court decisions as universal truths rather than jurisdiction-bound artifacts
- treating enforcement likelihood as legal validity
- importing economic efficiency notions as legal criteria
- importing psychological intent models as legal standards without explicit translation
- assuming procedural correctness implies substantive legality (or vice versa)

---

## Undecidability and STOP

This domain must return STOP (or “underdetermined”) when:

- jurisdiction is missing, ambiguous, or contested
- temporal applicability cannot be established
- the relevant fact pattern is incomplete, disputed, or undefined
- sources are missing, inaccessible, or insufficiently identifiable
- norms conflict without an explicit, domain-bounded resolution rule
- interpretation requires assumptions not declared in the artifact
- the output would imply advice, enforcement, or responsibility

STOP is not a failure.
STOP is a valid domain output.

---

## Scope Leakage Prevention

Legal outputs must not silently influence other domains.

Any cross-domain use requires:

- explicit translation artifacts
- explicit loss/distortion statements
- explicit boundary re-checks

No legal constraint is globally binding by default.

