# Decision Contract

## Status
exploratory — normativ in der Form, aber noch nicht operativ stabilisiert.

## Input
1) **AtomicProblemRecord**
- Problemdefinition auf minimaler Ebene (Ziel, Kontext, erlaubte Aktionen)
- Scope (Gültigkeitsbereich)
- Verantwortungs-/Kompetenzgrenzen (responsibility boundary)

2) **BoundEvidence**
- EvidenceRecords (formal/empirical/computational/...)
- ConflictReports (falls vorhanden)
- Uncertainty summaries (falls vorhanden)

3) Optional: **Methodology Records**
- Testspezifikation / DecisionRecord (vorläufige Akzeptanz/Verwerfung)
- Validierungsanforderungen

## Output (Artefakte)
1) **DecisionSpaceRecord**
- mandatory: Aktionen/Schlüsse, die unter den Preconditions zwingend sind
- permissible: Aktionen/Schlüsse, die erlaubt sind
- forbidden: Aktionen/Schlüsse, die ausgeschlossen sind
- undecidable: Aussagen/Aktionen, die unter den gegebenen Preconditions nicht entscheidbar sind
- stop: Abbruchflag + Grund (wenn Preconditions/Boundary verletzt)

2) **DecisionRationale**
- kurze Begründung je Klasse (mandatory/permissible/forbidden/undecidable)
- benannte Preconditions (welche Annahmen/Scope wurden verwendet?)

## Verantwortung
- Decision Interface entscheidet:
  - Klassifikation innerhalb eines klaren Entscheidraums (constraints + evidenzgebunden)
  - ob STOP notwendig ist (fehlende Preconditions / unklare Verantwortung / scope mismatch)
- Decision Interface entscheidet nicht:
  - moralische Bewertung/Utility-Abwägung
  - empirische Wahrheit
  - Auswahl „der besten“ Option (das ist eine nachgelagerte Policy-/Ethik-/Produktfrage)

## Akzeptanzkriterien (minimal)
- Input enthält expliziten Scope + responsibility boundary
- Jede Ausgabe-Klasse (mandatory/permissible/forbidden/undecidable/stop) ist begründet
- Scope alignment wurde geprüft:
  - wenn Evidence scope nicht passt → entweder STOP oder undecidable mit Begründung
- Wenn STOP gesetzt wird:
  - keine stillen Zusatzannahmen dürfen eingeführt werden

## Failure Modes
- Hidden assumptions: Klassifikation basiert auf nicht dokumentierten Annahmen
- Scope laundering: Evidenz außerhalb des Scope wird als gültig behandelt
- Responsibility blur: Decision wird getroffen ohne klare Zuständigkeitsgrenze
- False determinacy: undecidable wird fälschlich als mandatory/permissible ausgegeben

