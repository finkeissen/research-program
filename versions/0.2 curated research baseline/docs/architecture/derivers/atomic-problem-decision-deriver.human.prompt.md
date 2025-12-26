# Atomic Problem Decision Deriver (Human-readable)
## From Evidence to Legitimate Decision Space

This document belongs to the research program.
It explains how decisions are derived from
atomic problems and bound evidence.

It does not execute decisions.
It defines when decisions are legitimate.

---

## Purpose

This deriver determines which decisions are:

- mandatory
- permissible
- forbidden
- undecidable

for a given ATOMIC PROBLEM,
under the currently bound EVIDENCE.

It does not choose.
It constrains choice.

---

## Preconditions

This deriver operates only on:

- ATOMIC PROBLEMS
- with explicitly bound EVIDENCE
- including uncertainty and conflict markers

If these preconditions are not met,
decision derivation is illegitimate.

---

## What Counts as a Decision

A decision is an intentional intervention
that changes at least one of:

- causes
- constraints
- consequences
- responsibilities

A decision is not:
- an explanation
- a preference
- a prediction
- an optimization

Decisions always imply responsibility.

---

## Decision Classes

For each ATOMIC PROBLEM,
possible decisions are classified as:

### Mandatory
A decision is mandatory if:
- failure to act necessarily worsens outcomes
- responsibility is clearly attributable
- no alternative avoids the consequence

Non-action is itself a violation.

---

### Permissible
A decision is permissible if:
- multiple actions are consistent with evidence
- consequences are comparable or uncertain
- responsibility can be assumed

Choice remains open.

---

### Forbidden
A decision is forbidden if:
- it contradicts established evidence
- it violates explicit constraints
- it shifts responsibility illegitimately

Such decisions must not be presented as options.

---

### Undecidable
A decision is undecidable if:
- evidence is insufficient
- conflicts cannot be resolved
- consequences cannot be bounded

Undecidable is a valid outcome.

---

## Role of Uncertainty and Conflict

Uncertainty:
- reduces the scope of mandatory decisions
- increases the space of permissible ones

Conflict:
- may eliminate mandatory decisions entirely
- often leads to undecidable outcomes

Conflicts are not resolved at this level.

---

## STOP Condition

Decision derivation MUST STOP if:
- no decision can be classified legitimately
- further classification would introduce assumptions
- responsibility cannot be clearly attributed

STOP indicates the boundary of justified action.

---

## Responsibility Boundary

The deriver does not:
- select among permissible options
- weigh preferences
- evaluate moral worth

Responsibility for choice remains external.

The deriver only defines the legitimate space.

---

## Result

The result of this deriver is:

- a constrained decision space
- explicit exclusions
- explicit uncertainty
- explicit STOP where applicable

This output enables action
without simulating authority.

---

## Orientation Statement

> The system does not decide.  
> It determines when deciding is legitimate.

---

## End

