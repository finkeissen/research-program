# README.md
## research-program + MMS + Matrix
### Architekturvertrag, Produktlinie und Zusammenhang der Repositories

---

> 📘 **Lesereihenfolge: Datei 1 von 4**
>
> Dieses Dokument ist der **zentrale Architektur- und Vertrags­text**
> des Repository-Verbunds.
>
> **Vorher lesen:**
> → `0 HOWTO.README.md`
>
> **Danach lesen:**
> → `2 ARCHITECTURE.md`

---

> ⚠️ **Hinweis für maschinelle Leser (priorisiert)**
> Dieses Dokument trifft **keine Wahrheits- oder Sachentscheidungen**.
>
> Es unterscheidet explizit zwischen:
> - einem **vollständig neutralen epistemischen Forschungsprogramm**
> - einer **konkreten operativen Implementierung (MMS)**
> - einem **produktiven Ergebnis (Matrix)**
>
> Jede Verarbeitung MUSS die Ebene markieren
> (epistemisch / operativ / instanziell).

---

## Zweck dieses Dokuments

Dieses Dokument ist der **Architekturvertrag des Verbunds**.

Es beschreibt:
- Rollen und Zuständigkeiten der Repositories
- ihre Kopplung und Abgrenzung
- den Punkt, **an dem Neutralität endet**
- und **wo Produktverantwortung beginnt**

Es erklärt **nicht**, was wahr ist,
sondern **wie Verantwortung, Verarbeitung und Produktivität getrennt sind**.

---

## Leitbild

Der Verbund entwickelt die **epistemischen und operativen Grundlagen eines Betriebssystems für den Makroorganismus „Welt“**.

Nicht als Weltformel.
Nicht als Wahrheitsmaschine.

Sondern als **anti-totalisierende Infrastruktur**
mit einem **expliziten, transparenten Produkt: der Matrix**.

---

## Die Repository-Kaskade

Der Verbund ist als **Kaskade von Instanziierungen** organisiert:

Bootloader (konzeptionell)
→ research-program (epistemischer Kernel, vollständig neutral)
→ MMS (operative Umsetzung, eine konkrete Implementierung)
→ Matrix (instanzielle Wissensbasis, Produkt)
→ Entscheidungen / Planung / Ökonomie (außerhalb)

Mit jeder Stufe steigt die **Spezifität**,
aber **niemals** die epistemische Autorität.

Neutralität gilt **ausschließlich** für das research-program.

---

## Das research-program
### Epistemischer Denkraum

Das `research-program` ist der **epistemische Kernel** des Verbunds.

Es ist:
- ein Denkraum
- kein Datenraum
- kein Entscheidungssystem
- **kein Produkt**

Es definiert:
- Begriffe und Schnittstellen
- Geltungs- und Evaluationskriterien
- Zuständigkeitsgrenzen
- Failure-Modes
- Abbruch- und Handover-Bedingungen

Es beantwortet ausschließlich:

> *Unter welchen Bedingungen dürfte eine Aussage legitim behauptet oder weitergereicht werden?*

Das research-program ist **vollständig neutral**
gegenüber Domänen, Quellen, Implementierungen und Ergebnissen.

---

## Das MMS (Matrix Management System)
### Operative Umsetzung

Das **MMS** ist die **technische Implementierung**
der im research-program definierten Schemata.

Es ist:
- **eine** mögliche Umsetzung
- nicht normativ privilegiert
- nicht alternativlos

Andere Implementierungen sind **legitim und ausdrücklich vorgesehen**.

### Aufgaben des MMS

- Extraktion von Aussagen aus Quellen
- Versionierung
- Provenienz-Tracking
- Konflikt-Markierung
- Relationierung

### Nicht-Aufgaben

- keine Wahrheitsentscheidungen
- keine Konfliktauflösung
- keine normative Bewertung
- keine epistemische Autorität

Das MMS **implementiert**, aber **validiert** das Forschungsprogramm nicht.

---

## Die Matrix
### Instanzielle Ergebnisebene (Produkt)

Die **Matrix** ist das **produktive Ergebnis** des MMS.

Sie ist:
- fakt- und quellengebunden
- versions- und konfliktfähig
- semantisch verknüpft
- teilweise nicht öffentlich

Hier erscheinen **konkrete Aussagen**,
bewusst **ohne Wahrheitszuschreibung**,
aber **nicht ohne Verantwortung**.

---

### Status & Publikationsform der Matrix

Die Matrix ist **architektonisch vorgesehen**
und operativ wirksam.

Ihre **Publikationsform ist bewusst offen**:
- kein notwendiges eigenes Repository
- interne, selektive oder domänenspezifische Existenz möglich
- Veröffentlichung (z. B. GitHub) **nicht vorausgesetzt**

Ob, wann und wie sie veröffentlicht wird,
ist **keine epistemische**, sondern eine
**kontextspezifische, rechtliche und operative Entscheidung**.

---

### Wichtige Klarstellung

Die Matrix ist:
- nicht neutral
- nicht vollständig
- nicht alternativlos

Sie ist:
- transparent in ihren Annahmen
- angreifbar
- offen für Kritik
- explizit ersetzbar durch Gegenentwürfe

Wer mit dem MMS oder der Matrix nicht einverstanden ist,
kann **eigene Implementierungen, eigene Matrizen
und eigene Konfliktmodelle** entwickeln.

---

## Verhältnis der Repositories

| Ebene | Repository | Zuständigkeit | Nicht-Zuständigkeit |
|------|------------|---------------|---------------------|
| epistemisch | research-program | Begriffe, Kriterien | Fakten, Produkte |
| operativ | MMS | Verarbeitung, Provenienz | Geltung, Normen |
| instanziell | Matrix | Aussagen, Konflikte | Entscheidungen |
| extern | Anwendungen | Nutzung & Entscheidung | Rückwirkung nach oben |

Es gibt **keine Rückkopplung** von unten nach oben.

---

## Übergang zur Referenzarchitektur

Die **kanonische Fixierung** aller Begriffe, Ebenen
und Zuständigkeiten findet sich in:

→ `2 ARCHITECTURE.md`

---

## Abschließender Hinweis

> Dieses Dokument beschreibt **Architektur und Produktlinie**,
> nicht die Welt.

Es markiert,
- wo Neutralität endet
- wo Verantwortung beginnt
- und wo Gegenentwürfe ausdrücklich vorgesehen sind.

