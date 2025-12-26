# Concept Driver Spec

## Input
- ClaimRecords (SNL)

## Output
- ConceptRecords
- AmbiguityReport (optional)

## Schritte
1) Term Extraction
- Nomen/Phrasen als Term-Kandidaten
2) Sense Proposal
- mögliche Bedeutungen (falls domänenübergreifend)
3) Definition Type
- stipulative / descriptive / operational / theoretical

## Checks
- jeder Claim hat ConceptRecords für Schlüsselterme
- markiere `ambiguous` wenn mehrere plausible senses

## Example
Claim: "Beschleunigung ist konstant"
Terms:
- Beschleunigung (theoretical → operationalizable)
- konstant (mathematical/descriptive)

