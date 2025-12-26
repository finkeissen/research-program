# Semantics Contract

## Input
- Claims (NL/SNL)
- vorhandene Definitionen (falls vorhanden)
- Kontext (Domäne, Ziel-Interface: Logic/Math/Physics)

## Output (Artefakte)
1) ConceptRecord
- term (Begriff)
- intended referent (worauf soll es zeigen?)
- definition_type: stipulative | descriptive | operational | theoretical
- context/scope
- synonyms / near-synonyms
- disallowed mappings (was es NICHT bedeutet)

2) AmbiguityReport
- term
- competing senses (A, B, C)
- risk: low | medium | high
- disambiguation questions (was müsste man präzisieren?)

## Verantwortung
- Semantik entscheidet: Begriffsstruktur, Referenz, Definitionstyp.
- Semantik entscheidet nicht: Wahrheit/Empirie/Beweis.

## Akzeptanzkriterien
- jeder zentrale Term im Claim ist erfasst oder als "undefined" markiert
- Definitionstyp ist angegeben
- Mehrdeutigkeit wird dokumentiert, nicht still aufgelöst

