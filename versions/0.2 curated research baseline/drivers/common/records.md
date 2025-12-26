# Driver Records (Common)

Diese Datei beschreibt minimale Record-Formate, die Drivers erzeugen.

## ClaimRecord (SNL)
- id
- statement
- scope
- assumptions
- dependencies
- status
- confidence (qualitativ)

## ConceptRecord (Semantics)
- term
- sense_id
- referent_hint
- definition_type
- context/scope
- ambiguity (low/medium/high)

## ValidationReport
- target (file/record id)
- checks_run
- result (pass/fail)
- issues (list)
- suggested_fixes (list)

## EvidenceRecord
- evidence_type
- supports_claim_id
- method_summary
- quality_notes
- uncertainty_summary
- scope_alignment

