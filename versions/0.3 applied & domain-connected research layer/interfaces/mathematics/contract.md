# Mathematics Contract

## Status
exploratory — disziplinspezifisch stabil, aber noch ohne feste Serialisierung.

## Input
- Logisch formalisierte Claims (aus `logic/`)
- Definitionen oder Definitionsanforderungen
- Zieltyp:
  - Existenz
  - Eindeutigkeit
  - Invarianz
  - Abschätzung / Schranke
- Optional: informelle mathematische Intuition

## Output (Artefakte)
1) **Definitions**
- explizite mathematische Definitionen
- Typen/Strukturen (z. B. Mengen, Räume, Ordnungen)

2) **Assumption / Axiom Set**
- minimale Annahmen
- explizite Abhängigkeiten

3) **Lemma / Theorem Chain**
- strukturierte Beweiskette
- Abhängigkeiten zwischen Resultaten

4) **Model Candidates**
- konkrete Modelle, die die Axiome erfüllen
- Hinweise auf Nicht-Modelle / Gegenbeispiele

## Verantwortung
- Mathematik klärt:
  - *was folgt woraus* unter welchen Annahmen
- Mathematik entscheidet nicht:
  - ob Annahmen „realistisch“ sind
  - ob Modelle empirisch zutreffen

## Akzeptanzkriterien
- Jede Definition:
  - referenziert verwendete Begriffe
  - ist nicht zirkulär
- Jedes Lemma/Theorem:
  - listet Annahmen
  - verweist auf vorherige Resultate
- Modelle:
  - erfüllen die angegebenen Axiome explizit

## Failure Modes
- Overaxiomatization (unnötig starke Annahmen)
- Hidden assumptions (implizit verwendete Eigenschaften)
- Symbol drift (gleiches Symbol, andere Bedeutung)

