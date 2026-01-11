# Decision Boundary

## Nicht-Ziele
- Keine normative Zieloptimierung (kein Utility maximization).
- Keine Ethik-/Werteentscheidung. (Dafür ggf. eigenes Ethics Interface später.)
- Keine Erzeugung neuer Evidenz (keine Messung/kein Beweis).
- Keine „Wahrheitsbehauptung“ — nur Klassifikation im Entscheidraum.

## Typische Kategorienfehler
- „mandatory“ = „wahr“ (falsch: mandatory ist eine Constraint-Klassifikation)
- „permissible“ = „empfohlen“ (falsch: Empfehlung erfordert Policy/Präferenzen)
- „undecidable“ = „falsch“ (falsch: undecidable = Informationsmangel / Unterbestimmtheit)
- Scope ignorieren: Evidenz aus anderem Regime wird übernommen

## STOP-Regeln (harte Grenzen)
STOP, wenn mindestens eines gilt:
- Scope ist nicht definiert oder widersprüchlich
- responsibility boundary fehlt oder ist unklar
- entscheidende Evidenz fehlt und kann nicht plausibel ersetzt werden
- Konflikte sind zentral und unaufgelöst (und verändern die Klassifikation)

## Verhältnis zu anderen Interfaces
- nutzt `evidence/` für Stützung/Widerspruch
- nutzt `methodology/` für Test-/Validationslogik
- kann `validation/` (common) als Gate verwenden

