# MMS INTERFACE
## Enforcement Without Structural Authority

---

## Status

This document defines the **interface between the Research Program (RP)**
and the **Meta-Management System (MMS)**.

It assigns **enforcement responsibilities**
while explicitly denying
any structural or epistemic authority to MMS.

---

## Role of MMS

MMS is a **pure enforcement and administration layer**.

Its sole function is to:

- validate inputs against structures defined in the RP,
- refuse inadmissible instantiations,
- emit STOP records,
- forward admissible instantiations to the Matrix,
- record provenance and audit data.

MMS does not interpret content
and does not reason about meaning.

---

## Structural Authority (Explicitly Denied)

MMS MUST NOT:

- define new entity types,
- modify RP-defined structures,
- extend schemas,
- infer admissibility beyond explicit rules,
- introduce fallback structures,
- normalize partial inputs,
- repair or complete inadmissible artifacts.

Any such behavior constitutes
a violation of this interface.

---

## Admissibility Enforcement

MMS enforces admissibility strictly
according to RP-defined structures, including:

- problem-atom schema requirements,
- admissible entity types,
- STOP conditions,
- absence rules.

Enforcement is **binary**:
- admit,
- or refuse (STOP).

No graded outcomes are permitted.

---

## Relation to SELF-APPLICATION

Documents such as `SELF-APPLICATION.md`
are **explicitly excluded**
from MMS admissibility sources.

MMS MUST NOT:

- derive admissibility from self-application,
- treat self-plausibility as validation,
- correct or stabilize normative starting points.

If MMS behavior depends on such documents,
a STOP MUST be triggered
(`SchemaViolation.LayerCollapse`).

---

## Interface to the Matrix

MMS MAY forward to the Matrix only:

- fully admissible instantiations,
- explicit STOP records,
- explicit Absence records,
- provenance metadata.

MMS MUST NOT:

- aggregate Matrix entries,
- synthesize relations,
- rank entries,
- suppress STOPs,
- infer missing data.

The Matrix is passive
with respect to MMS decisions.

---

## Auditability

MMS MUST provide sufficient information
to allow external audit, including:

- RP version,
- schema version,
- enforcement rule version,
- timestamp,
- refusal reason (if applicable).

Audit verifies **conformity**, not correctness.

---

## Failure Modes

If MMS fails, it may fail only by:

- refusing admissible input (false negative),
- stopping processing entirely.

MMS MUST NOT fail by
admitting inadmissible structures.

---

## Final Note

MMS exists to prevent
structural erosion under operational pressure.

It enforces rules it does not create.

Any intelligence attributed to MMS
is a category error.

