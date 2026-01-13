# Logic Primitives

## Objekte
- **Term**: Objekt-/Individuen-Ausdruck
- **Predicate**: Eigenschaft/Relation über Terme
- **Formula**: zusammengesetzte Aussage (Prädikatenlogik o. ä.)
- **Signature**: Symbolmenge + Typen/Sorten
- **Context / Scope**: Gültigkeitsbedingungen (Domäne, Zeit, Modellannahmen)
- **Rule**: Inferenzregel (z. B. Modus Ponens, ∀-Elim, …)
- **Derivation Step**: (inputs, rule, output)

## Minimal-Formen
- Atome: P(t1,...,tn)
- Junktoren: ¬, ∧, ∨, →, ↔
- Quantoren: ∀, ∃
- Gleichheit (optional, aber häufig nötig): =

## Markierungen
- `candidate`: mehrere Formalisierungen möglich
- `requires_definition`: Term/Prädikat unklar, Definition fehlt
- `scope_guarded`: Formel gilt nur unter Scope-Bedingung

## Scope-Container (SNL → formal)
- domain: worüber quantifiziert wird
- conditions: Nebenbedingungen (z. B. „für endliche Systeme“, „unter idealen Bedingungen“)
- time/index: falls benötigt (t, n, …) statt „implizit“

