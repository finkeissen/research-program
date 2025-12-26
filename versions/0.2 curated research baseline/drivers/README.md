# Drivers

Drivers sind Adapter, die Inputs in Interface-Artefakte überführen oder Artefakte gegen minimale Regeln prüfen.
Sie sind der operative Teil des research-program (explorativ), aber noch **nicht** mms.

## Prinzip
- Drivers produzieren Records/Reports in SNL/strukturierter Form.
- Jeder Driver referenziert genau ein Interface als „Owner“ der Artefakte.
- Drivers dürfen *keine* disziplinäre Arbeit ersetzen (z. B. Physik messen, Logik beweisen),
  sondern nur strukturieren, validieren, zusammenführen.

## Minimaler Driver-Stack (empfohlen)
1) claim/Claim Driver
2) semantics/Concept Driver
3) validation/Cross Validation Driver
4) evidence/Evidence Aggregator
5) metrology/Unit & Calibration Driver (sobald Physik-Messungen kommen)

