# Domain Translations — Legal Law

This document defines how abstract research artifacts
are interpreted within the Legal Law domain, and how domain artifacts
may be mapped back into research artifacts.

Translations are controlled.
They must not create authority or silently introduce normativity outside the domain.

---

## Incoming Translations (Research → Legal Law)

### Claims → Legally Relevant Statements
A research claim may be translated into a legally relevant statement only if:

- jurisdiction is specified
- the claim is mapped to a legal category explicitly
- the mapping identifies required facts and missing facts
- the claim’s scope is reconciled with legal applicability

If these conditions are not met, translation must yield STOP.

### Evidence → Legal Sources / Legal Proof Context
Evidence artifacts may be translated into legal context as:

- identified sources (statutes, regulations, cases) when they are legal texts
- supporting factual materials (documents, testimony, records) when they are facts

The translation must state:
- whether the item is a legal source or a factual input
- how it is used (authority vs fact)
- any uncertainty about authenticity, relevance, or applicability

### Decision Space → Legal Status Classification
Decision spaces may be mapped to legal status categories:

- mandatory
- forbidden
- permitted
- undecidable (STOP)

This mapping is allowed only with:
- explicit sources
- explicit interpretation profile (or explicit absence)
- explicit conflict handling or STOP

---

## Outgoing Translations (Legal Law → Research)

### Norms → Constraint Artifacts
Legal norms may be exported as research artifacts representing:

- constraints (must/must-not/may)
- applicability conditions
- exception structures
- procedural requirements

These exports must include:
- jurisdiction
- temporal assumptions
- source identification
- interpretation assumptions (if any)

### Conflicts / Ambiguities → Conflict Markers
Legal conflicts and ambiguities may be mapped into research-level conflict markers:

- conflict between norms
- ambiguity in interpretation
- underdetermined applicability

This does not require resolution.

### STOP Reports → STOP Artifacts
Legal STOP outcomes should be exported as explicit STOP artifacts:

- what was missing
- what assumptions would be required
- which boundary triggered STOP

STOP must never be replaced by guessed legal outcomes.

---

## Forbidden Mappings

The following translations are forbidden:

- Legal permission → recommendation
- Legal prohibition → moral condemnation
- Legal status → enforcement prediction
- Legal authority → epistemic truth
- Legal sources → domain-independent “facts”
- Absence of sources → permission (unless explicitly supported)

---

## Loss and Distortion

The following losses/distortions are expected and must be stated when relevant:

- legal meaning depends on jurisdiction and time
- interpretation approaches change outputs
- procedural context may dominate substantive outcomes
- legal categories may not map cleanly to everyday language
- “proof” standards are domain-specific and not numeric certainty

Translations must not hide these distortions.


