# Drivers Walkthrough (Beispiel)

Dieses Dokument illustriert anhand eines konkreten Beispiels,
wie die **Drivers** des research-programs zusammenwirken.
Es ist **erklärend**, nicht normativ.

---

## Input (Freitext)
"Bei idealem freien Fall nahe der Erdoberfläche ist die Beschleunigung konstant."

---

## 1. Claim Driver → ClaimRecord (SNL)

```yaml
claim_record:
  id: C-001
  statement: "Bei idealem freien Fall nahe der Erdoberfläche ist die Beschleunigung konstant."
  scope:
    - "nahe der Erdoberfläche"
    - "Luftwiderstand vernachlässigt"
  assumptions:
    - "homogenes Gravitationsfeld (lokale Näherung)"
  dependencies: []
  status: hypothesis
  confidence: qualitative
```

---

## 2. Concept Driver (Semantics) → ConceptRecords

```yaml
concept_records:
  - term: "freier Fall"
    sense_id: "FREE_FALL/IDEALIZED"
    referent_hint: "Bewegung unter Gravitation ohne weitere Kräfte"
    definition_type: theoretical
    ambiguity: low

  - term: "Beschleunigung"
    sense_id: "ACCELERATION/PHYSICS"
    referent_hint: "zweite Zeitableitung der Position"
    definition_type: theoretical
    ambiguity: low

  - term: "konstant"
    sense_id: "CONST/MATH"
    referent_hint: "zeitlich invariant im betrachteten Intervall"
    definition_type: stipulative
    ambiguity: low
```

Ambiguity Report (Auszug):
```yaml
ambiguity_report:
  term: "nahe der Erdoberfläche"
  competing_senses:
    - "Höhe << Erdradius"
    - "innerhalb Messunsicherheit konstantes g"
  risk: medium
```

---

## 3. Cross Validation Driver → ValidationReport

```yaml
validation_report:
  target: "C-001"
  result: pass_with_warnings
  issues:
    - "Scope unpräzise: 'nahe der Erdoberfläche'"
  suggested_fixes:
    - "Höhenbereich oder Messgenauigkeit angeben"
```

---

## 4. Übergabe an Interfaces (konzeptionell)

Ab hier übernehmen die Interfaces (Logic, Mathematics, Physics, …).
Drivers strukturieren nur die Übergabe.

---

## 5. Evidence Aggregator → EvidenceRecords

```yaml
evidence_records:
  - evidence_type: formal
    supports_claim_id: C-001
    method_summary: "Mathematisches Modell mit konstanter Beschleunigung"
    scope_alignment: match

  - evidence_type: empirical
    supports_claim_id: C-001
    method_summary: "Messreihe Position vs. Zeit"
    scope_alignment: match
```

---

## Ergebnis

- Claims sind strukturiert
- Begriffe sind explizit
- Qualität ist prüfbar
- Evidenz ist als Artefakt modelliert

Dieses Walkthrough dient ausschließlich der **Erläuterung der Driver-Architektur**.
