# Logic Contract

## Status
exploratory — stabilisiert erst, wenn BL2/BL4 finalisiert sind.

## Input (aus research-program)
- Claims (NL/SNL) inkl. Scope, Annahmen, Abhängigkeiten
- Definitionen (Term-Festlegungen, Typen/Sorten, Abkürzungen)
- Inferenzanforderung (was soll gezeigt/abgeleitet/geprüft werden?)
- Optional: Referenzen/Quellen (nur als Kontext, nicht als Beweis)

## Output (Artefakte)
1) **Signature**
- Symbole, Prädikate, Funktionen, Sorten/Typen (minimaler Wortschatz)

2) **Formalized Claims**
- Formel(n) pro Claim (ggf. mehrere Kandidaten)
- Mapping NL ↔ Formel
- Scope-/Kontextbedingungen

3) **Derivation Graph**
- Knoten: Formeln/Definitionen
- Kanten: Ableitungsschritte (mit Regel-Label)

4) **Consistency & Conflict Markers**
- `consistent | inconsistent | unknown`
- Konfliktarten:
  - direkte Kontradiktion (φ und ¬φ)
  - Scope-Konflikt (gleiches Symbol, anderer Geltungsbereich)
  - Mehrdeutigkeit (mehrere nicht-äquivalente Formalisierungen)

## Verantwortung
- Logik liefert *Struktur* (Ableitbarkeit/Konsistenz), keine empirische Wahrheit.
- Jede Formalisierung muss rückübersetzbar sein (Translationspflicht).

## Akzeptanzkriterien (minimal)
- Jede Formel hat:
  - referenzierten Claim
  - Scope/Context
  - verwendete Signatur
- Jede Ableitung:
  - benennt die Regel
  - benennt Inputs/Outputs
- Konfliktmarker erklären *warum* (nicht nur „fail“)

## Failure Modes (explizit)
- „False precision“: Formalisierung suggeriert Eindeutigkeit, wo NL mehrdeutig ist.
- „Scope erasure“: Kontextbedingungen werden verschluckt.
- „Category leak“: Empirische Evidenz wird als logischer Beweis ausgegeben.

