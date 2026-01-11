# Logic Interface

Diese Schnittstelle formalisiert Claims aus dem research-program als logische Objekte: Signaturen, Formeln, Inferenzregeln, Ableitungen und Konfliktmarker.

## Zweck
- BL2 (Logic Design) operationalisieren: „Rationalität → Ableitbarkeit“.
- Begründen/Entkräften von Claims durch explizite Regeln statt implizite Rhetorik.
- Konflikte sichtbar machen (Widerspruch, Mehrdeutigkeit, Scope-Kollision).

## Liefert
- formalisiertes Claim-Set (Formeln + Kontext)
- Ableitungs-/Abhängigkeitsgraph
- Konsistenz-/Konfliktmarker
- Boundary-/Scope-Markierungen (was gilt wo?)

## Nutzt
- `interfaces/common/*` (Glossar, Repräsentationslevel, Unsicherheit, Validation)

