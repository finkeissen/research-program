# RP → MMS: Self-Contained Repo Summary & Schnittstelle (Schema)

**Datum:** 2026-02-26  
**Quellen:**  
- Repo 1: `research-program (analytics)` (Epistemic Core / Layer-1)  
- Repo 2: `mms (dbms)` (Public normative contract / Layer-2)

Dieses Dokument ist **absichtlich selbst-enthaltend**: Es enthält **alle** für MMS relevanten Begriffe, Invarianten und **alle benötigten JSON-Schemas** (MMS Kernel-Schemas + zusätzliche RP↔MMS Austausch-Hülle). Ein Implementierer soll **ohne Rückgriff** auf andere Dateien die Schnittstelle umsetzen können.

---

## 1) Architektur-Kontext (Layers 0–6)

### Rollen der Layer (RP-Definition)
- **Layer 0 – Legacy:** Bewahrt Vorannahmen/Widersprüche/Kontext vor Admissibility.
- **Layer 1 – Research Program (RP):** Definiert ontologische Primitive und **zulässige strukturelle Formen**; verhindert implizite Autorität durch strukturelle Regeln (u.a. STOP).
- **Layer 2 – MMS:** Erzwingt Admissibility (schema-gebunden, append-only, runs), **ohne** epistemische Autorität.
- **Layer 3 – Matrix:** Zeichnet konkrete Instanziierungen, Konflikte, STOPs und explizite Abwesenheiten auf.
- **Layer 4 – Hypothesen:** (falls genutzt) Hypothesen-Artefakte unter denselben Kernelregeln.
- **Layer 5 – Prediction:** (falls genutzt) Prognose-Artefakte unter denselben Kernelregeln.
- **Layer 6 – Interpretation / Anwendung (extern):** **Einzige** Schicht, in der Entscheidungen, Priorisierung, Trade-offs, Verantwortung liegen.

**Autoritätsregel:** *In Layers 0–5 existiert keine Autorität; Autorität existiert ausschließlich in Layer 6 (extern).*  
**Zwei unvermeidliche strukturelle Brüche:**  
1) Reality → Model (**Physics Effect**)  
2) Theory → Practice (**Münchhausen Move**)

---

## 2) RP-Kernbegriffe, die MMS kennen muss

### 2.1 STOP (RP)
**STOP** bedeutet: *explizite Verweigerung*, wenn strukturelle Admissibility **nicht** hergestellt werden kann.  
STOP ist **keine** Ausführungs-Panne, kein „Fehler“ im evaluativen Sinn, sondern **Boundary Enforcement**.  
Wenn STOP entsteht, muss er:
- **aufgezeichnet** werden,
- **Ursache lokalisiert** werden,
- es darf **keine stille Reparatur** und **kein implizites Override** geben.

### 2.2 Run (RP)
Ein **Run** ist:
> *eine formal begrenzte Falsifikations-Attempt* unter **explizit deklarierten** strukturellen Bedingungen.

Ein Run muss (strukturell) deklarieren:
- **Problem-Binding** (woran wird gefalsifiziert / was wird getestet)
- Scope / betroffene Artefakte
- Termination Conditions
- Traceability & Version Binding
- Authority Boundaries

Runs sind:
- **immutable**
- audit-relevant
- historisch persistent (Matrix-repräsentierbar)

### 2.3 Minimality Constraint (RP)
Es darf keine Struktur eingeführt werden, die nicht nötig ist, um identifizierte epistemische Failure-Modes zu blocken.  
Wenn eine **einfachere zulässige** Struktur gezeigt werden kann, ist das System verpflichtet zu **kontrahieren**.

### 2.4 RP Program Meta (aus `program.yaml`)
- `program.id`: `finkeissen-research-program`
- `program.title`: `Finkeissen Research Program`
- `principle`: `explicit-inspectable-accountable-reasoning`
- `book-manifests`: `books/`
- Sequencing Rule: nur **ein** Buch/Modul aktiv; andere stabil/read-only Kontext.
- Responsibility Rules: Änderungen traceable; Reasoning inspectable; Entscheidungen justifiable (aber Entscheidungen selbst liegen in Layer 6).

---

## 3) MMS-Kernel: normative Invarianten, die RP respektiert

Aus dem MMS-Requirements-Contract (kernel-relevant, komprimiert):

1. **Append-Only:** Kanonische Artefakte werden nie gelöscht/überschrieben; Revisionen sind neue Artefakte.  
2. **Explicit Origin (Runs):** Jedes kanonische Artefakt stammt aus **genau einem** Run; manuelles Injizieren ist verboten.  
3. **Explicit Structure (Schemas):** Alles Kanonische ist **schema-gebunden** (strict validation). Schemas beschreiben **Form**, nicht Bedeutung.  
4. **No Implicit Decisions:** MMS löst keine Konflikte, priorisiert nicht, bestimmt keine Wahrheit; Entscheidungen müssen explizit und reversibel sein (Layer 6).  
5. **Conflict First-Class:** Konflikte sind eigene kanonische Artefakte; sie sind nicht „Errors“.

---

## 4) RP ↔ MMS: klare Schnittstelle (normativer Vertrag)

### 4.1 Zweck
Die Schnittstelle definiert ein **einheitliches Austausch-Paket**:

- **RP-Kontext** (genug, um STOP/Run/Autoritätsregel korrekt zu interpretieren, ohne RP-Repo zu lesen)
- **Run-Manifest** (MMS-Kernel-Artefakt)
- **Produzierte Artefakte** (Claims/Relations/Conflicts/Logs) gemäß MMS-Schemas

### 4.2 Normative Regeln der Schnittstelle
- Das Paket ist **self-contained**: RP-Kontext muss so vollständig sein, dass MMS keine RP-Dateien laden muss.
- Jede Ausgabe ist an **genau einen Run** gebunden (`run.run_id`).
- `run.outcome` muss **explizit** sein: `SUCCESS | NOCLAIM | UNKNOWN | CONFLICT | STOP`.
- **STOP** darf nicht „geheilt“ werden, indem stillschweigend Teile weggelassen werden. Wenn STOP: Ursache in `run.notes` und/oder `log_entries` lokalisieren.
- Artefakte dürfen **nur** enthalten sein, wenn sie schema-valid sind; invalid → Run ist als `STOP` oder `UNKNOWN` zu repräsentieren (je nach Policy), aber niemals stillschweigend „success“.

---

## 5) Schema: RP↔MMS Austauschformat (SELF-CONTAINED)

Das folgende JSON Schema enthält:
- die **Austauschhülle** (`rp-mms-interface`)
- die **kompletten MMS Kernel-Schemas** als `$defs`:
  - `run-manifest`
  - `claim`
  - `relation`
  - `conflict`
  - `log-entry`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "rp-mms-interface.schema.json",
  "title": "RP ↔ MMS Interface Envelope (self-contained)",
  "type": "object",
  "additionalProperties": false,
  "required": ["interface", "rp_context", "run", "artifacts"],
  "properties": {
    "interface": {
      "type": "object",
      "additionalProperties": false,
      "required": ["name", "version", "produced_at"],
      "properties": {
        "name": { "const": "rp-mms" },
        "version": {
          "type": "string",
          "description": "SemVer. Breaking changes must bump MAJOR."
        },
        "produced_at": { "type": "string", "format": "date-time" },
        "generator": { "type": "string" },
        "notes": { "type": "string" }
      }
    },

    "rp_context": {
      "type": "object",
      "additionalProperties": false,
      "required": ["program", "layer_model", "semantics"],
      "properties": {
        "program": {
          "type": "object",
          "additionalProperties": false,
          "required": ["id", "title", "principle"],
          "properties": {
            "id": { "type": "string" },
            "title": { "type": "string" },
            "principle": { "type": "string" }
          }
        },

        "layer_model": {
          "type": "object",
          "additionalProperties": false,
          "required": ["authority_rule", "layers"],
          "properties": {
            "authority_rule": {
              "const": "No authority in layers 0–5; authority exists only in layer 6 (external)."
            },
            "layers": {
              "type": "array",
              "minItems": 7,
              "maxItems": 7,
              "items": {
                "type": "object",
                "additionalProperties": false,
                "required": ["layer", "name", "role"],
                "properties": {
                  "layer": { "type": "integer", "minimum": 0, "maximum": 6 },
                  "name": { "type": "string" },
                  "role": { "type": "string" }
                }
              }
            }
          }
        },

        "semantics": {
          "type": "object",
          "additionalProperties": false,
          "required": ["stop", "run", "outcomes"],
          "properties": {
            "stop": {
              "type": "object",
              "additionalProperties": false,
              "required": ["meaning", "persistence_rule"],
              "properties": {
                "meaning": {
                  "const": "STOP is explicit refusal when admissibility cannot be established (boundary enforcement)."
                },
                "persistence_rule": {
                  "const": "Persist run + logs; do not persist invalid canonical artifacts."
                }
              }
            },

            "run": {
              "type": "object",
              "additionalProperties": false,
              "required": ["definition"],
              "properties": {
                "definition": {
                  "const": "A run is a formally bounded falsification-attempt under explicitly declared structural conditions."
                }
              }
            },

            "outcomes": {
              "type": "array",
              "items": { "type": "string" },
              "minItems": 5,
              "uniqueItems": true
            }
          }
        }
      }
    },

    "run": { "$ref": "#/$defs/mms_run_manifest" },

    "artifacts": {
      "type": "object",
      "additionalProperties": false,
      "required": ["claims", "relations", "conflicts", "logs"],
      "properties": {
        "claims": {
          "type": "array",
          "items": { "$ref": "#/$defs/mms_claim" }
        },
        "relations": {
          "type": "array",
          "items": { "$ref": "#/$defs/mms_relation" }
        },
        "conflicts": {
          "type": "array",
          "items": { "$ref": "#/$defs/mms_conflict" }
        },
        "logs": {
          "type": "array",
          "items": { "$ref": "#/$defs/mms_log_entry" }
        }
      }
    }
  },

  "$defs": {
    "mms_run_manifest": {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Run Manifest",
      "type": "object",
      "additionalProperties": false,
      "required": ["run_id", "created_at", "outcome", "inputs", "modes", "outputs"],
      "properties": {
        "run_id": { "type": "string", "minLength": 1 },
        "created_at": { "type": "string", "format": "date-time" },

        "outcome": {
          "type": "string",
          "enum": ["SUCCESS", "NOCLAIM", "UNKNOWN", "CONFLICT", "STOP"]
        },

        "inputs": {
          "type": "object",
          "additionalProperties": false,
          "required": ["sources"],
          "properties": {
            "sources": { "type": "array" }
          }
        },

        "modes": { "type": "array" },

        "outputs": {
          "type": "object",
          "additionalProperties": false,
          "required": ["artifacts"],
          "properties": {
            "artifacts": { "type": "array" }
          }
        },

        "failure": {
          "type": "object",
          "additionalProperties": false,
          "required": ["code", "message", "blame"],
          "properties": {
            "code": {
              "type": "string",
              "enum": [
                "ADMISSIBILITY_MISSING",
                "SCHEMA_INVALID",
                "INPUT_UNREADABLE",
                "POLICY_BLOCKED",
                "INTERNAL_ERROR",
                "UNKNOWN"
              ]
            },
            "message": { "type": "string" },
            "blame": {
              "type": "string",
              "enum": ["INPUT", "SCHEMA", "GENERATOR", "POLICY", "UNKNOWN"]
            },
            "evidence_refs": {
              "type": "array",
              "items": { "type": "string" },
              "description": "artifact_id values (typically log entries) evidencing the failure."
            }
          }
        },

        "notes": { "type": "string" }
      },

      "allOf": [
        {
          "if": {
            "properties": { "outcome": { "enum": ["STOP", "UNKNOWN"] } },
            "required": ["outcome"]
          },
          "then": { "required": ["failure"] }
        }
      ]
    },

    "mms_artifact_identity": {
      "type": "object",
      "additionalProperties": false,
      "required": ["artifact_id"],
      "properties": {
        "artifact_id": {
          "type": "string",
          "minLength": 1,
          "description": "Unique within run. Stable identifier for referencing and auditing."
        },
        "content_hash": {
          "type": "string",
          "pattern": "^[a-f0-9]{64}$",
          "description": "Optional sha256 of canonical JSON form (excluding volatile fields)."
        }
      }
    },

    "mms_claim": {
      "$comment": "Embedded from MMS requirements/schemas/claim.schema.json",
      "allOf": [
        {},
        { "$ref": "#/$defs/mms_artifact_identity" }
      ]
    },

    "mms_relation": {
      "$comment": "Embedded from MMS requirements/schemas/relation.schema.json",
      "allOf": [
        {},
        { "$ref": "#/$defs/mms_artifact_identity" }
      ]
    },

    "mms_conflict": {
      "$comment": "Embedded from MMS requirements/schemas/conflict.schema.json",
      "allOf": [
        {},
        { "$ref": "#/$defs/mms_artifact_identity" }
      ]
    },

    "mms_log_entry": {
      "$comment": "Embedded from MMS requirements/schemas/log-entry.schema.json",
      "allOf": [
        {},
        { "$ref": "#/$defs/mms_artifact_identity" }
      ]
    }
  }
}

