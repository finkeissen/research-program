# Cross Validation Driver Spec

## Input
- beliebige Records (Claim, Concept, Measurement, Evidence, …)

## Output
- ValidationReport

## Minimalchecks
- Required fields vorhanden
- Scope vorhanden (falls nötig)
- Keine Kategoriefehler:
  - empirical evidence als formal proof markiert? → fail
  - missing uncertainty in physics/probability → warn/fail (je nach policy)

## Ergebnis-Klassen
- pass
- pass_with_warnings
- fail

