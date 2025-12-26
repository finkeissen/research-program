# Claim Driver Spec

## Input
- Freitext (Notizen, Absätze, Bulletpoints)

## Output
- Liste von ClaimRecords (SNL)

## Heuristik (minimal)
- Sätze mit Verben wie "ist", "führt zu", "impliziert", "tritt auf", "erhöht" → Claim-Kandidaten
- Scope-Kandidaten: "unter", "bei", "falls", "für", "in", "nahe", "ohne"
- Annahmen-Kandidaten: "angenommen", "idealisierend", "wir nehmen an", "vernachlässigt"

## Failure Modes
- Claim ohne Scope → `unscoped`
- zu viele Claims in einem Satz → split recommendation

## Example
Input:
"Bei idealem freien Fall nahe der Erdoberfläche ist die Beschleunigung konstant."

Output ClaimRecord:
- id: C-001
- statement: ...
- scope: Nähe Erdoberfläche, Luftwiderstand vernachlässigt
- assumptions: homogenes Gravitationsfeld
- status: hypothesis

