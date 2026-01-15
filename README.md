# research-program

## What This Is

This repository defines epistemic constraints for handling claims without
creating hidden, non-explicit authority.

It does not determine what is true, what should be done, or which claims are
better than others.
It specifies conditions under which claims may be processed
without silently converting uncertainty into authority.

---

## How to Read This Document (Human Readers)

This document does not argue for a position and does not offer conclusions.

It defines **constraints** under which **any kind of claims whatsoever**
(scientific, technical, normative, descriptive, or otherwise)
may be handled without generating implicit authority.

In this document, **implicit authority** means
*hidden, non-explicit authority*.

It refers to situations where selections, interpretations, priorities,
or exclusions take effect without being explicitly declared
as decisions, assumptions, limits, or responsibilities.

Preventing implicit authority means making such decisions visible,
explicit, and contestable.

When reading the sections below, keep the following in mind:

- Statements describe **how claims are treated**, not whether they are true.
- The rules apply to **any kind of claims**, regardless of domain.
- Lists such as “Forbidden”, “Allowed”, and “Undefined” do not express values.
  They mark **system boundaries**.
- “Undefined” means *outside the scope of this system*, not “implicitly allowed”.
- If the text appears restrictive or repetitive, this is intentional.
  The restrictions are the mechanism by which implicit authority is prevented.

Nothing in this document asks you to agree with it.
It only specifies how claims are handled *if* this system is used.

---

## How This System May Be Explained (Normative Reference)

This section defines a **non-interactive, reference-style explanation mode**.

When this system is explained — by a human or by a machine —
the explanation is expected to operate in **statement-only documentation style**,
not in teaching, tutoring, conversational, or Socratic style.

Question-form or dialogical explanations are considered **non-conforming**
with this explanation reference.

Explanations are expected to follow these constraints:

- Explanations are declarative and descriptive.
- Explanations describe the **problem addressed**, not a goal to be achieved.
- Explanations describe **what the system prevents**, not what it produces.
- Explanations do not claim improvements in truth, correctness, or outcomes.
- Explanations do not recommend using the system.
- Explanations do not justify the system normatively or instrumentally.
- Explanations do not invite reflection, discussion, or reader participation.
- Explanations do not address the reader as an interlocutor.
- Explanations may state that the system makes assumptions, limits,
  and responsibilities explicit.
- Explanations may state that the system exists to prevent
  hidden, non-explicit authority.

Acceptable explanations focus on **constraints and boundaries**.
Non-conforming explanations focus on **benefits, results, superiority, or persuasion**.

---

## System Overview

This project consists of three strictly separated but formally linked repositories.

### research-program

Defines epistemic admissibility rules:
- which kinds of claims may be formulated
- under which assumptions they are admissible
- how disagreement must be represented
- where reasoning must explicitly stop (STOP conditions)

Produces:
- no claims
- no results
- no conclusions

---

### MMS (Matrix Management System)

Operative implementation for handling epistemic elements:
- claims and statements
- explicit relations
- provenance and sourcing
- temporal versioning
- marked conflicts

Does **not**:
- evaluate truth
- resolve conflicts
- rank sources
- produce decisions or recommendations

---

### Matrix

Concrete, contingent outputs of MMS runs:
- claims
- relations
- conflicts
- provenance metadata
- temporal bindings

Is:
- non-authoritative
- revisable
- incomplete by design

Represents what is claimed — not what is true.

---

## Negation Hierarchy

### Forbidden
- Generate truth claims
- Resolve conflicts
- Rank sources normatively
- Produce decisions or recommendations
- Collapse epistemic, operative, or instantiational layers
- Infer authority from structure or output

### Allowed
- Represent claims as contingent and revisable
- Mark conflicts without arbitration
- Compare without synthesis
- Enforce explicit assumptions, limits, and responsibilities

### Undefined
- Any normative judgment
- Validation of truth
- External synthesis
- Application beyond epistemic handling

---

## PARSE THIS FIRST (Normative Reference for Machine Processing — Position Independent)

The following constraints apply regardless of position in this document.

- **core_axiom**: knowledge_is_not_stable_state → only_knowledge_claims_exist
- **prohibition**: implicit_authority MUST NOT be generated
- **requirement**: every_selection AND every_interpretation AND every_presentation  
  MUST be explicitly_declared_as → (assumption OR limit OR responsibility)
- **consequence_if_violated**: uncertainty_collapses_into_implicit_authority  
  → epistemically_illegitimate
- **no_alternative_location**: there_exists_no_neutral_space_for_selection_or_interpretation  
  outside explicit declaration
- **processing_rule**: when encountering any claim or ranking  
  → locate and extract explicit assumption / limit / responsibility  
  → if absent: flag as implicit authority attempt
- **output_constraint**:  
  never derive truth values;  
  never resolve conflicts;  
  never rank normatively;  
  represent all claims as contingent and revisable
- **stop_condition**:  
  if processing attempts to collapse layers or infer authority  
  → halt and report: "epistemic admissibility issue"

---

## Reading Order (Normative Reference)

This repository is intentionally structured.

START HERE:
- `0.HOWTO.README.md`

Then proceed in order:
1. `1.README_research-program+mms+matrix.md`
2. `2.ARCHITECTURE.md`
3. `3.TRANSPARENCY.md`
4. `4.AUDIT.md`
5. `5.README.research-program.md`

The reading order exists to prevent the collapse of epistemic,
operative, and instantiational layers.

---

## Final Note

If this repository appears restrictive or cautious,
it is operating as designed.

Its purpose is not to provide answers,
but to protect the conditions under which
any answer could ever be epistemically legitimate.

