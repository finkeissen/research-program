# End-to-End Walkthrough – Interfaces (v0)

## Purpose
This walkthrough demonstrates a complete traversal of a simple claim through all foundational interfaces
of the research-program. The goal is architectural validation, not scientific depth.

---

## Ausgangs-Claim
**Claim (NL):**
Bei idealem freien Fall nahe der Erdoberfläche ist die Beschleunigung konstant.

**Scope:**
- Nähe der Erdoberfläche
- Vernachlässigung von Luftwiderstand

**Annahmen:**
- Homogenes Gravitationsfeld

---

## 0. Structured Natural Language (Pre-Boot)
Der Claim wird strukturiert (Statement, Scope, Annahmen), aber noch keiner Disziplin zugeordnet.

Artefakt:
- ClaimRecord (SNL)

---

## 1. Logic Interface
**Ziel:** formale Ableitbarkeit.

Formalisierung (Kandidat):
∀t₁,t₂ : g(t₁) = g(t₂)

Ergebnis:
- logisch konsistent
- scope-guarded

Artefakte:
- FormalClaimRecord
- DerivationContext

---

## 2. Mathematics Interface
**Ziel:** Struktur und Modell.

Modell:
x''(t) = g₀

Folgerungen:
- v(t) = g₀·t + v₀
- x(t) = ½ g₀·t² + v₀·t + x₀

Artefakte:
- DefinitionRecord
- ModelRecord

---

## 3. Computer Science Interface
**Ziel:** Berechenbarkeit.

Algorithmus:
- numerische Ableitung von Positionsdaten
- Varianz der Beschleunigung

Eigenschaften:
- O(n)
- approximativ (Diskretisierung)

Artefakte:
- AlgorithmRecord
- ComplexityRecord

---

## 4. Physics Interface
**Ziel:** Weltkontakt.

Messung:
- Größe: Position x(t)
- Gerät: Kamera / Lichtschranke
- Einheiten: Meter, Sekunde

Unsicherheit:
- statistisch: Messrauschen
- systematisch: Luftwiderstand

Artefakte:
- MeasurementRecord
- DataSetRecord
- ErrorModelRecord

---

## 5. Probability & Statistics Interface
**Ziel:** Evidenzbewertung.

Modell:
aᵢ ~ Normal(μ, σ²)

Ergebnis:
- μ ≈ 9.8 m/s²
- kleine Varianz im Scope

Artefakte:
- ProbabilityModelRecord
- InferenceRecord

---

## 6. Methodology Interface
**Ziel:** Forschungsentscheidung.

Test:
- H₀: Beschleunigung konstant
- Varianztest

Entscheidung:
- vorläufig akzeptiert
- gültig nur im definierten Scope

Artefakte:
- TestSpecRecord
- DecisionRecord

---

## Rückkopplung
Abweichungen führen zu:
- engerem Scope
- erweitertem Modell (z. B. Luftwiderstand)
- neuen Claims

---

## Hinweis
Dieses Dokument ist ein architektonisches Beispiel und erhebt keinen Anspruch auf Vollständigkeit
oder didaktische Ausarbeitung.
