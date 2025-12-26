# Decision Primitives

## Objekte
- **Atomic Problem**
  - minimaler Entscheidkontext: Ziel, Kontext, Aktionsraum, Constraints
- **Action / Option**
  - das, was klassifiziert wird (Handlung, Schluss, Empfehlung, Auswahl)
- **Constraint**
  - Regel/Bindung, die den Entscheidraum begrenzt
- **Decision Space**
  - Partitionierung der Aktionen in Klassen

## Klassen
- **mandatory**
  - unter den Preconditions zwingend erforderlich
- **permissible**
  - erlaubt; keine Verletzung bekannter Constraints
- **forbidden**
  - verletzt Constraints / widerspricht Evidenz / scope mismatch
- **undecidable**
  - nicht entscheidbar unter gegebenen Preconditions/Evidenz
- **STOP**
  - Abbruch: Preconditions/Responsibility/Scope unzureichend

## Marker
- `scope-mismatch`
- `missing-precondition`
- `responsibility-unclear`
- `conflict-unresolved`
- `assumption-introduced` (sollte bei STOP nicht vorkommen)

