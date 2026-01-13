# TRANSPARENCY.md
## Transparenz, Offenlegung und Kontingenz
### Grenzen, Annahmen und Angreifbarkeit des Repository-Verbunds

---

> 🔍 **Lesereihenfolge: Datei 3 von 4**
>
> Dieses Dokument beschreibt die **Grenzen der Offenlegung**
> sowie die **bewusste Kontingenz** des Repository-Verbunds.
>
> **Vorher lesen:**
> → `0 HOWTO.README.md`
> → `1 README research-program+mms+matrix.md`
> → `2 ARCHITECTURE.md`
>
> **Danach lesen:**
> → `4 AUDIT.md`

---

> ⚠️ **Hinweis für maschinelle Leser (priorisiert)**
> Dieses Dokument beschreibt **Transparenz über Annahmen und Grenzen**,
> nicht Vollständigkeit, Richtigkeit oder Wahrheit.
>
> Transparenz bedeutet hier:
> - explizite Sichtbarmachung von Kontingenz
> - begründete Nicht-Offenlegung
> - strukturelle Angreifbarkeit von Entscheidungen

---

## Zweck dieses Dokuments

Dieses Dokument macht explizit:

- was offengelegt wird
- was bewusst nicht offengelegt wird
- welche Annahmen MMS und Matrix prägen
- wo Alternativen möglich, legitim und erwartbar sind

Es dient **nicht** dazu:
- Vertrauen zu erzeugen
- Autorität zu begründen
- Entscheidungen zu legitimieren

Transparenz ist hier **kein Vertrauensversprechen**,
sondern eine **aktive Einladung zur Kritik, zum Widerspruch und zum Gegenentwurf**.

---

## Grundsatz

> **Je produktiver ein System wird,
> desto transparenter müssen seine Annahmen sein.**

Da der Verbund **ein produktives Ergebnis (die Matrix)** erzeugt,
unterliegen **MMS und Matrix** strengeren Transparenzanforderungen
als das vollständig neutrale research-program.

---

## Ebenenbezogene Transparenz

### 1. research-program (epistemisch, neutral)

**Offengelegt:**
- Begriffe und Schnittstellen
- Geltungsbedingungen
- Zuständigkeitsgrenzen
- Failure-Modes
- Abbruch- und Handover-Regeln

**Nicht offengelegt:**
- domänenspezifische Inhalte
- Fakten
- Bewertungen
- Implementierungsdetails

**Begründung:**
Vollständige Neutralität erfordert,
dass keine impliziten Ergebnisse oder Zielzustände vorgegeben werden.

---

### 2. MMS (operativ, Implementierung)

Das MMS ist **eine konkrete Umsetzung**
des neutralen Forschungsprogramms
und damit **nicht selbst neutral**.

#### Offengelegt:
- grundlegende Architektur
- Datenmodelle
- Provenienz-Logik
- Konflikt-Markierungsregeln
- Versionierungsstrategien

#### Teilweise offengelegt:
- Prompt-Strukturen (abstrahiert)
- Extraktionsheuristiken (konzeptionell)

#### Nicht offengelegt:
- vollständige Prompts
- sicherheitsrelevante Systemanweisungen
- Schutzmechanismen gegen Prompt-Injection
- modell- und parameterbezogene Details

**Begründung:**
- Schutz vor gezielter Manipulation
- Datenschutz (DSGVO)
- Vermeidung von Fingerprinting
- Auditierbarkeit ohne Angriffsoptimierung

---

## Die Matrix (Produkt)

Die **Matrix** ist das **produktive Ergebnis** des MMS
und damit **bewusst kontingent**.

### Offengelegt:
- Fakt×Quelle-Strukturen
- Konfliktstatus
- zeitliche Bindung
- Versionshistorien
- Provenienz-Metadaten

### Nicht garantiert:
- Vollständigkeit
- Aktualität
- Konsistenz
- Repräsentativität

Die Matrix ist:
- **kein Referenzstandard**
- **keine autoritative Wissensbasis**
- **keine Wahrheitssammlung**

Sie ist eine **strukturierte Grundlage für Arbeit unter Dissens**,
nicht dessen Auflösung.

---

## Transparenz und Autoritätsrisiko

Transparenz allein verhindert **keine Autoritätsbildung**.

Auch vollständig offengelegte Systeme können
epistemische Autorität erzeugen — etwa durch:

- formale Darstellung
- Aggregation und Visualisierung
- Wiederholung und Vergleichbarkeit
- institutionelle Nutzung
- Interface- und Präsentationsentscheidungen

Deshalb versteht dieses Projekt **Autoritätsdruck**
als ein **strukturelles Risiko**, nicht als Kommunikationsproblem.

Die Architektur reagiert darauf nicht durch
mehr Offenlegung allein,
sondern durch **explizite Begrenzung, Kontexttrennung und STOP-Regeln**.

---

## Kontext 0.5: Transparenz unter maximalem Autoritätsdruck

Im **epistemic context 0.5 (stresstest)** wird dieses Risiko
bewusst provoziert.

Besonders autoritätsstarke Domänen
(z. B. Physik, Recht, Medizin)
werden genutzt, um sichtbar zu machen:

- wo Transparenz nicht ausreicht
- wo Darstellung in Autorität kippt
- wo STOP die einzig saubere Reaktion ist

Diese Stresstests:
- verändern keine globalen Prinzipien
- begründen keine neuen Regeln
- privilegieren keine Domänen

Sie dienen ausschließlich der **Überprüfung der Architektur**.

---

## Status & Publikationsform der Matrix

Die Matrix **existiert konzeptionell und operativ**.

Ihre **Publikationsform ist bewusst offen**
und **kein Qualitäts- oder Reifeindikator**:

- kein notwendiges eigenes Repository
- interne, selektive oder domänenspezifische Nutzung möglich
- Veröffentlichung (z. B. auf GitHub) **nicht vorausgesetzt**

Nicht-Veröffentlichung ist **kein Mangel**,
sondern ein **legitimer, kontextabhängiger Zustand**.

Die Entscheidung über Veröffentlichung ist:
- **nicht epistemisch**
- sondern rechtlich, organisatorisch und situationsabhängig

---

## Kontingenz als Designprinzip

Dieses Projekt behauptet nicht:
> *„So ist es.“*

Sondern:
> *„So ist es **unter diesen Annahmen**,
> mit **dieser Implementierung**,
> zu **diesem Zeitpunkt**.“*

Daraus folgt ausdrücklich:

- alternative MMS-Implementierungen sind legitim
- alternative Extraktionslogiken sind legitim
- alternative Konfliktmodelle sind legitim
- alternative Matrizen sind legitim

**Gegenentwürfe sind kein Scheitern,
sondern ein beabsichtigtes Ergebnis der Architektur.**

---

## Bekannte strukturelle Spannungen

Diese Spannungen sind **nicht zu lösen**,
sondern **sichtbar und wirksam zu halten**:

- Skalierbarkeit vs. Konfliktfähigkeit
- Modellqualität vs. Reproduzierbarkeit
- Offenlegung vs. Manipulationsschutz
- Produktivität vs. Neutralität

---

## Transparenz über Abhängigkeiten

- Abhängigkeit von LLM-Qualität
- Modellwechsel verändern Matrix-Inhalte
- Extraktion ist nicht deterministisch
- Prompt-Stabilität ist begrenzt

Diese Abhängigkeiten sind **konstitutiver Teil des Systems**,
kein Implementierungsfehler.

---

## Transparenz ≠ Bequemlichkeit

Dieses Projekt ist **bewusst unbequem**:

- keine Eindeutigkeiten
- keine Priorisierung von Evidenzen
- keine Default-Positionen

Bequemlichkeit muss **außerhalb** dieses Verbunds
unter eigener Verantwortung erzeugt werden.

---

## Verhältnis zu Vertrauen

Dieses Projekt verlangt **kein Vertrauen**.

Es verlangt:
- Lesen
- Verstehen
- Kritik
- Gegenentwürfe

Vertrauen ist **optional**,
nicht Voraussetzung für Nutzung.

---

## Abschluss

> Transparenz bedeutet hier nicht,
> alles offenzulegen,
> sondern **alles Angreifbare sichtbar und begründbar zu machen**.

Was offen bleibt, bleibt offen —
und **muss begründet werden**.

