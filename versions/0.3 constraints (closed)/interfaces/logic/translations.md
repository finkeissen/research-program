# Logic Translations

## Ziel
Übersetze zwischen:
- NL/SNL Claims ↔ formale Formeln
- formale Ableitungen ↔ erklärbare Begründungen
- Logik-Artefakte ↔ spätere operative Schemas (mms)

## Mapping: Claim → Formel
Pro Claim entsteht ein Translation-Record:
- claim_id
- nl_statement
- signature_used
- formula_candidates: [φ1, φ2, ...]
- disambiguation_notes
- scope_binding (welche Variablen/Indices repräsentieren Scope?)

## Mehrdeutigkeit behandeln
Wenn mehrere Kandidaten nicht äquivalent sind:
- markiere alle als `candidate`
- definiere „Decision Point“:
  - welche Zusatzdefinition/Scope-Angabe würde Kandidaten eliminieren?
  - welche empirische Information wäre nötig? (nur als Hinweis, nicht als Logik)

## Rückübersetzung: Formel → Erklärung
- kurze paraphrase (NL)
- Liste verwendeter Regeln
- Abhängigkeiten (welche Annahmen waren nötig?)

## Übergabeformat (vorläufig)
- `SignatureRecord`
- `FormalClaimRecord`
- `DerivationGraphRecord`
- `ConflictReport`

Details (Serialisierung) kommen aus `interfaces/common/representations.md`.

