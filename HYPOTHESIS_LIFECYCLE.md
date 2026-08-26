research-program/HYPOTHESIS_LIFECYCLE.md
# Hypothesis Lifecycle

## Purpose

This document defines the structural lifecycle
of hypotheses (Layer 4).

It governs status transitions,
storage organization,
and historical persistence.

It does not define truth.
It defines structural state.

---

# 1. Directory Structure

Hypotheses must be organized as:

hypotheses/
  active/
  inactive/
  falsified/

This structure supports scaling
without altering identity or history.

Directory placement reflects status,
not legitimacy.

---

# 2. Identity

Each hypothesis must have:

- immutable identifier (H###)
- version marker
- explicit problem binding
- falsification criteria
- declared assumptions

Identifier must never change.

If core meaning changes substantially,
a new H### must be created.

---

# 3. Status Definitions

## active

- Currently under consideration
- Not falsified
- Not superseded
- May be tested by runs

Active does not imply plausibility.
It only implies structural admissibility.

---

## inactive

- No longer actively tested
- Temporarily suspended
- Replaced by more specific hypotheses
- Deprioritized for testing

Inactive does not imply falsification.

---

## falsified

- At least one run satisfied falsification criteria
- Failure condition documented
- Version and run reference recorded

Falsified hypotheses remain historically accessible.

They are never deleted.

---

# 4. Status Transitions

Permitted transitions:

active → falsified  
active → inactive  
inactive → active  

Not permitted:

falsified → active  
falsified → inactive  

Reinstatement after falsification
requires creation of new identifier.

---

# 5. Versioning Interaction

Version increment does not change status.

If falsification criteria change,
version must increment.

If falsification criteria are weakened,
justification must be documented.

No silent weakening permitted.

---

# 6. Run Binding

Every run that references a hypothesis must bind to:

- explicit identifier
- explicit version

If version changes during a run,
the run remains bound to original version.

No implicit upgrade permitted.

---

# 7. Matrix Representation

Hypothesis status changes must be representable
in the Matrix as structured events.

No status change may occur silently.

---

# 8. Deletion Prohibition

Hypotheses must never be deleted.

Historical artifacts are structurally persistent.

Archival is permitted.
Erasure is not.

---

# 9. Non-Authority Statement

Active does not mean likely.
Falsified does not mean useless.
Inactive does not mean irrelevant.

Lifecycle state does not imply truth.

Authority remains external.

