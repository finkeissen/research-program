# Schemas (Envelope + Records)

Dieses Verzeichnis definiert eine gemeinsame Serialisierung für Artefakte aus Interfaces und Drivers.

## Ziel
- Einheitliche Verpackung aller Artefakte (ein gemeinsamer **Envelope**)
- Modulare, typisierte **Payloads** (Records), die je Disziplin/Driver variieren
- Stabiler Pfad Richtung operative Systeme (z. B. mms), ohne mms vorwegzunehmen

## Konzept

### Envelope (für alles gleich)
Jedes Artefakt wird als Envelope gespeichert:

- `id` (global eindeutig)
- `type` (Discriminator, z. B. `claim`, `concept`, `measurement`, `inference`, `evidence`, `validation`)
- `schema_version` (Envelope-Version)
- `record_version` (Payload-Version, empfohlen)
- `created_at` (ISO-8601)
- `scope` (Gültigkeitsbereich)
- `provenance` (Quelle/Autor/Driver/Commit)
- `links` (Bezüge zu anderen Artefakten)
- `payload` (typisierter Record)

### Records (typisierte Payloads)
Die Felder in `payload` werden pro Typ unter `records/*.schema.json` definiert.

## Dateien
- `envelope/envelope.schema.json`
- `records/*.schema.json`
- `examples/` (Einzelbeispiele + Bundles als JSONL)

## Bundling
- Einzelartefakt: `*.json` (ein Envelope)
- Bundle: `*.jsonl` (ein Envelope pro Zeile)

## Stabilität
- Envelope: möglichst stabil
- Records: dürfen evolvieren; Versionierung beachten

## Quickstart
- `examples/walkthrough_bundle.jsonl` zeigt ein komplettes Mini-Set.
