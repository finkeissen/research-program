# Decision Translations

## Evidence → Decision Constraints
- EvidenceRecords erzeugen Constraints:
  - supports → erlaubt/fordert unter Bedingungen
  - contradicts → verbietet unter Bedingungen
- ConflictReports erhöhen Unsicherheit:
  - führen häufig zu `undecidable` oder STOP

## Methodology → Decision Context
- TestSpecRecord liefert:
  - worüber überhaupt entschieden wird
  - welche Schwellen/Validationskriterien gelten
- DecisionRecord liefert:
  - vorläufige Prozessentscheidung (akzeptiert/verworfen/offen)
  - wird hier nicht überschrieben, sondern in DecisionSpace integriert

## DecisionSpace → Handoff (später mms)
Exportfähig (typisch):
- DecisionSpaceRecord (strukturierte Klassifikation + rationale)
Nicht exportfähig (typisch):
- implizite Heuristiken ohne explizite Preconditions

## Mapping auf Schema (Envelope)
Empfohlen:
- envelope.type = `decision_space`
- payload = DecisionSpaceRecord
- links:
  - derived_from → AtomicProblemRecord id
  - depends_on → EvidenceRecord ids

