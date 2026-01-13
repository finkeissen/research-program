# Decision Interface

Diese Schnittstelle definiert, wie aus **Atomic Problems** und **Bound Evidence** ein
strukturierter **Decision Space** abgeleitet wird.

Sie ist eine normative Schnittstelle (im Sinne: Regeln/Constraints), aber kein
„Entscheider“ im Sinne moralischer Gewichtung oder finaler Wahrheit.

## Zweck
- Entscheidbarkeit als Artefakt: was ist **mandatory / permissible / forbidden / undecidable**?
- Expliziter Abbruchmechanismus: **STOP** wenn Preconditions fehlen oder Verantwortung unklar ist.
- Brücke zwischen:
  - `interfaces/evidence/` (Evidenz + Konflikte)
  - `interfaces/methodology/` (Test-/Decision-Prozesse)

## Quellen (explanatory)
Die konzeptionelle Herleitung steht hier:
- `docs/architecture/derivers/atomic-problem-decision-deriver.md`

## Liefert
- DecisionSpaceRecord (als Artefakt zur weiteren Verwendung)
- DecisionBoundary Notes (warum STOP / warum undecidable)

## Nutzt
- EvidenceRecords (Evidence Interface)
- ValidationReports (Cross Validation)
- Methodology DecisionRecords (Methodology Interface)

