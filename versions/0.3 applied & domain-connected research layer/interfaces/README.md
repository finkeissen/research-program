# Interfaces (Grundlagen-Schnittstellen)

Dieses Verzeichnis definiert disziplinäre Schnittstellen, die den Übergang von der Boot-Sequenz (insb. BL2–BL5) in formale und empirische Grundlagendisziplinen strukturieren.

## Ziel
- Eine *einheitliche* Art, Wissen/Claims/Begründungen aus dem research-program in disziplinäre Formen zu überführen.
- Disziplinen bleiben getrennt: Logik ≠ Mathematik ≠ Informatik ≠ Physik.
- Jede Schnittstelle liefert klare Artefakte, die später in operative Systeme (z. B. mms) übergeben werden können.

## Grundprinzip
Jede Disziplin hat die gleiche minimale Dateistruktur:

- `contract.md`  
  Definiert Input/Output-Artefakte, Verantwortung und Akzeptanzkriterien.
- `primitives.md`  
  Minimaler Wortschatz + Objekte/Operationen der Disziplin in unserem Kontext.
- `boundary.md`  
  Explizite Nicht-Ziele, Gültigkeitsbereiche, typische Kategoriefehler.
- `translations.md`  
  Mappings zwischen natürlicher Sprache, formalen Repräsentationen und späteren Schemas.

Physik ergänzt:
- `measurement.md`  
  Operationalisierung, Einheiten, Unsicherheit, Messprotokolle.

## Verbindung zur Boot-Sequenz
- BL2 (Logic Design): erzeugt erste formale Struktur → primär `logic/`.
- BL3 (Rational Commitment): Normen/Regeln der Begründung → wirkt in `contract.md` + `boundary.md`.
- BL4 (Handover): Übergabevertrag → `contract.md` wird kompatibel zu späteren operativen Systemen.
- BL5 (Research Mode): Disziplin-Treiber laufen → nutzen `translations.md` + `validation` aus `common/`.

## Output-Form (vorläufig)
Interfaces liefern *Artefakte*, keine „Wahrheiten“:
- strukturierte Claims
- Abhängigkeiten/Begründungsgraphen
- Konsistenz-/Konfliktmarker
- Mess-/Unsicherheitsmetadaten (Physik)

Die endgültige Serialisierung (JSON/YAML/Schemas) wird in `common/representations.md` vorbereitet.

## Architectural Walkthrough

Ein vollständiges End-to-End-Beispiel (ein Claim durch alle Interfaces) liegt zentral unter:

- [docs/architecture/walkthrough.md](../docs/architecture/walkthrough.md)
- [docs/architecture/End-to-End_Walkthrough_Interfaces_v0.pdf](../docs/architecture/End-to-End_Walkthrough_Interfaces_v0.pdf)

Hinweis: Der Walkthrough liegt absichtlich **nicht** unter `interfaces/`, da `interfaces/`
normative Schnittstellen-Definitionen (contracts, boundaries, primitives, translations) enthält,
während Walkthroughs erklärend sind und separat gepflegt werden, um Drift zu vermeiden.

