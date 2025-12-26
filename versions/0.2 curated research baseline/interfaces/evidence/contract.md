# Evidence Contract

## Input
- Claims (SNL/formal)
- Proof/Derivation summaries (Logic/Math)
- Data + inference outputs (Physics/Probability)
- Computational verification outputs (CS)

## Output
1) EvidenceRecord
- evidence_type: formal | empirical | computational | testimonial
- supports_claim_id
- method_summary
- quality_notes
- uncertainty_summary
- scope alignment (match/mismatch)

2) ConflictReport
- conflicting claims/evidence
- conflict_type: contradiction | scope mismatch | model mismatch | measurement mismatch
- what would resolve it? (info needed)

3) SupportGraph
- nodes: claims, evidence
- edges: supports, contradicts, depends_on

## Akzeptanzkriterien
- Evidenztyp ist angegeben
- Scope-Match ist angegeben
- Konflikte sind als Artefakt exportiert (nicht versteckt)


