# AUDIT.md
## Audit & Nachvollziehbarkeit
### Externe Prüfbarkeit des Repository-Verbunds

---

> 🧪 **Lesereihenfolge: Datei 4 von 4**
>
> Dieses Dokument schließt die Lesereihenfolge ab.
>
> Es beschreibt, **wie** der Repository-Verbund geprüft,
> auditiert und reproduziert werden kann –
> **nicht**, was inhaltlich „richtig“ ist.
>
> **Voraussetzung:**
> → `0 HOWTO.README.md`
> → `1 README research-program+mms+matrix.md`
> → `2 ARCHITECTURE.md`
> → `3 TRANSPARENCY.md`

---

> ⚠️ **Hinweis für maschinelle Leser (priorisiert)**
> Dieses Dokument definiert **Auditierbarkeit**, nicht Wahrheit.
>
> Audits prüfen:
> - Regelkonformität
> - Ebenentrennung
> - Prozess- und Provenienztreue
>
> Sie prüfen **nicht**:
> - Richtigkeit von Aussagen
> - Konfliktauflösungen
> - normative Entscheidungen

---

## Zweck dieses Dokuments

Dieses Dokument beschreibt die **extern prüfbare Seite**
des Repository-Verbunds.

Es beantwortet ausschließlich:

> *Wie lässt sich überprüfen,
> dass dieses System seine eigenen Regeln einhält?*

Audit bedeutet hier:
- Nachvollziehbarkeit
- Reproduzierbarkeit
- Regelkonformität
- Transparenz über Grenzen

**Auditierbarkeit impliziert dabei keinen vollständigen, unbeschränkten oder automatischen Zugriff auf alle Daten oder Artefakte.**

---

## 1. Audit-Ziele (verbindlich)

Ein Audit dient dem Nachweis, dass:

- keine impliziten Wahrheitsentscheidungen getroffen werden
- epistemische, operative und instanzielle Ebenen strikt getrennt sind
- Artefakte versioniert und referenzierbar sind
- Provenienz explizit dokumentiert ist
- bekannte Limitationen offen benannt sind

Ein Audit dient **nicht**:
- inhaltlicher Bewertung
- Konfliktauflösung
- normativer Beurteilung

---

## 2. Aktueller Audit-Status (Stand: Januar 2026)

| Bereich| Status| Beleg / Ort| Letzte Prüfung |
|------------------------|-------------------|------------------------------------|----------------|
| Epistemischer Kernel | stabil, gefreezed | research-program + TRANSPARENCY.md | Jan 2026 |
| MMS-Spezifikation| definiert | MMS-Repo + Contracts | Jan 2026 |
| Domäne Medizin | ~70 % Abdeckung | Domänen-Report + Issues| Dez 2025 |
| Domäne Deutsches Recht | ~70 % Abdeckung | Domänen-Report + Issues| Dez 2025 |
| Domäne Autoheilkunde | ~70 % Abdeckung | Domänen-Report + Issues| Dez 2025 |
| Provenienz-Tracking| implementiert | MMS-Status-Felder| laufend|
| Konflikt-Tracking| implementiert | MMS conflicting-Status | laufend|
| Prompt-Prinzipien| dokumentiert| TRANSPARENCY.md + Issues | Jan 2026 |

### Bedeutung von „~70 % Abdeckung“

Eine Domäne gilt als „~70 % abgedeckt“, wenn:

- ca. 70 % der zentralen Begriffe / Normen extrahiert sind
- ≥ 60 % der wesentlichen Konflikte markiert sind
- für ≥ 80 % der Aussagen eine explizite Provenienz vorliegt

Dies ist **keine Vollständigkeits- oder Qualitätsgarantie**.

---

## 3. Bekannte Limitationen & Risiken

Diese Punkte gelten als **bekannt und auditrelevant**:

- nicht eliminierbare LLM-Halluzinationen
→ mitigiert durch Provenienzpflicht

- hohe Konfliktdichte in einzelnen Domänen
→ insbesondere Recht (historisch vs. aktuell)

- Skalierbarkeit der Matrix
→ Performance-Grenzen bei vielen Domänen erwartet

- Abhängigkeit von Modellqualität
→ Modellwechsel verändern Ergebnisse

- kein Anspruch auf Vollständigkeit oder Aktualität

---

## 4. Wie man selbst auditieren kann

Ein Audit kann ohne privilegierten Zugriff beginnen:

1. **ARCHITECTURE.md**
 → Ebenen, Zuständigkeiten, Sperren prüfen

2. **README research-program+mms+matrix.md**
 → korrekte operative Umsetzung?

3. **TRANSPARENCY.md**
 → sind Offenlegungsgrenzen begründet?

4. **Domänen-Stichproben**
 → Versionierung, Provenienz, Konfliktstatus

5. **Issue-Tracker**
 → Labels: `audit`, `provenance`, `conflict`, `limitation`

---

## 5. Externe Audits

Externe Audits sind **ausdrücklich willkommen**.

Vorgehen:
- Issue mit Label `audit` eröffnen
- Scope benennen (Domäne, Struktur, Reproduzierbarkeit, …)

Für sensible Teile:
- selektiver Zugriff
- NDA möglich

---

## 6. Abgrenzung

Dieses Audit-System ist **keine**:
- Zertifizierungsstelle
- Wahrheitsinstanz
- Governance-Autorität
- inhaltliche Qualitätsbewertung

Es prüft **Strukturtreue**, nicht Wahrheit.

---

## Abschluss

> Dieses Dokument macht das Projekt **prüfbar**,
> ohne es **autoritäter** zu machen.

Audit ist hier kein Machtinstrument,
sondern eine **Schutzschicht gegen implizite Geltungsansprüche**.

