# Domain Primitives — Legal Law

This document defines the **primitive terms and constructs** used by the
Legal Law domain connector.

All terms are **domain-bound**: they do not claim global meaning and must not
be silently transferred to other domains.

---

## Terms

- **Jurisdiction**
  - Meaning: The legal system context in which a norm is valid (e.g. a country, state, court system, regulatory regime).
  - Scope: Must be explicitly stated for every legal artifact.
  - Notes: Undefined jurisdiction triggers STOP.

- **Source**
  - Meaning: A formally recognized legal text or decision that grounds a norm (statute, regulation, case, treaty, administrative guidance).
  - Scope: Must be traceable or at least identifiable (citation, identifier, or stable reference).
  - Notes: “General knowledge” is not a source.

- **Norm**
  - Meaning: A legal rule that prescribes, permits, or prohibits actions or states.
  - Scope: Domain-internal; not moral or political by default.
  - Notes: Norms can conflict; conflict does not imply invalidity.

- **Applicability**
  - Meaning: The conditions under which a norm applies to a case.
  - Scope: Explicitly conditional; depends on facts, jurisdiction, and time.
  - Notes: If applicability cannot be established, return STOP or “underdetermined”.

- **Validity (Legal)**
  - Meaning: The formal standing of a norm within a jurisdiction at a given time.
  - Scope: Legal validity only; not truth, not legitimacy.
  - Notes: A norm may be valid and still contested or interpreted differently.

- **Interpretation**
  - Meaning: A mapping from a legal source to an operational meaning (how a norm is understood in practice or jurisprudence).
  - Scope: Must state interpretive assumptions (textualism, purposive reading, precedent reliance, etc.).
  - Notes: Interpretation introduces uncertainty and must be made explicit.

- **Requirement (Mandatory)**
  - Meaning: A legal obligation: something must be done or must be the case.
  - Scope: Conditional on applicability.
  - Notes: Do not confuse with “best practice”.

- **Prohibition (Forbidden)**
  - Meaning: A legal constraint: something must not be done or must not be the case.
  - Scope: Conditional on applicability.
  - Notes: Must be distinguished from “discouraged”.

- **Permission (Allowed)**
  - Meaning: A legal allowance: something may be done without violating a norm.
  - Scope: Conditional on applicability.
  - Notes: Permission does not imply recommendation.

- **Right**
  - Meaning: A legally recognized entitlement held by an actor under certain conditions.
  - Scope: Jurisdiction-bound and often procedural.
  - Notes: Rights can conflict or be limited by exceptions.

- **Duty**
  - Meaning: A legally recognized obligation borne by an actor under certain conditions.
  - Scope: Jurisdiction-bound; may be primary or derived.
  - Notes: Duties may be strict or qualified.

- **Exception**
  - Meaning: A condition that removes or modifies applicability of a norm.
  - Scope: Must be represented explicitly; exceptions are not “edge cases”.
  - Notes: Exceptions often define the real boundary of a norm.

- **Procedure**
  - Meaning: A legally required process step (notice, filing, hearing, review, due process requirements).
  - Scope: Often as important as the substantive norm.
  - Notes: Missing procedures frequently trigger STOP.

- **Standard of Review / Standard**
  - Meaning: A legal threshold or evaluative criterion (e.g. reasonableness, proportionality, beyond reasonable doubt).
  - Scope: Must be named; does not reduce to numeric certainty.
  - Notes: Standards encode domain-specific uncertainty handling.

- **Actor / Legal Person**
  - Meaning: An entity recognized by law as capable of rights/duties (individual, corporation, state body, etc.).
  - Scope: Jurisdiction-bound.
  - Notes: Not identical to “agent” in psychology or economics.

- **Fact Pattern**
  - Meaning: The relevant factual description used to assess applicability.
  - Scope: Facts are inputs; the domain does not manufacture facts.
  - Notes: Missing or disputed facts must be marked explicitly.

- **Remedy / Consequence**
  - Meaning: A legal outcome attached to a norm (damages, injunction, nullity, penalty, enforcement mechanisms).
  - Scope: Conditional; often procedural.
  - Notes: Not to be interpreted as recommendation or action guidance.

- **Conflict**
  - Meaning: Two or more norms or interpretations that cannot all be satisfied simultaneously under the given fact pattern.
  - Scope: May remain unresolved.
  - Notes: Conflict detection is allowed; conflict resolution may be refused.

- **Ambiguity**
  - Meaning: Multiple plausible readings of a source or applicability condition.
  - Scope: Must be stated; ambiguity is not silently collapsed.
  - Notes: Ambiguity is a STOP trigger if it blocks classification.

- **Temporal Applicability**
  - Meaning: The time window in which a norm or interpretation is in force.
  - Scope: Must be explicit when relevant.
  - Notes: Law changes; artifacts can expire.

---

## Constructs

- **Legal Constraint Set**
  - Description: A set of obligations, prohibitions, and permissions derived from identified sources under stated assumptions.
  - Assumptions: Jurisdiction, time, interpretation approach, and fact pattern are explicit.
  - Limitations: Not a complete view of the law; may omit unknown or inaccessible sources.

- **Applicability Test**
  - Description: A structured set of conditions mapping fact patterns to norm applicability.
  - Assumptions: Facts are sufficiently specified; interpretation approach is stated.
  - Limitations: If facts are incomplete, result must be “underdetermined” or STOP.

- **Interpretation Profile**
  - Description: A declared stance for interpreting sources (precedent weight, textual vs purposive, administrative deference, etc.).
  - Assumptions: Profile is a modeling choice, not an authority claim.
  - Limitations: Different profiles can yield different outputs.

- **Legal Status Classification**
  - Description: A classification outcome for an action/state: mandatory / forbidden / permitted / undecidable.
  - Assumptions: Depends on applicability, conflicts, and standards.
  - Limitations: Classification may be partial (e.g. “permitted but procedurally constrained”).

- **STOP Report (Legal)**
  - Description: A structured record explaining why legal classification cannot be produced.
  - Assumptions: STOP is legitimate and expected.
  - Limitations: Does not imply illegality or legality; only insufficient determination.

---

## Forbidden Terms

The following terms are forbidden unless explicitly defined for a specific sub-scope:

- “Just”, “unjust”, “ethical”, “moral”, “good”, “bad”
- “Optimal”, “efficient”, “best”
- “True”, “false” (as global truth claims)
- “Advice”, “recommendation”
- “Should” (unless explicitly marked as a legal requirement within scope)

