# Representations (Cross-Discipline)

Diese Datei beschreibt minimale Repräsentationsformen, die in mehreren Interfaces wiederkehren.

## Repräsentations-Level
1. Natural Language (NL)
2. Structured NL (SNL): Claims + Felder (Bedingungen, Scope, Quellen)
3. Formal: Logik/Mathe (Signatur, Axiome, Ableitung)
4. Algorithmic: Informatik (Datenmodell, Algorithmus, Test/Verifier)
5. Operational: Physik (Messprotokoll, Einheit, Unsicherheit, Gerätebezug)

## Claim Record (SNL)
Minimalfelder (vorläufig):
- id
- statement (NL)
- scope (Gültigkeitsbereich)
- assumptions (Liste)
- dependencies (Liste)
- status (hypothesis | lemma | theorem | empirical | heuristic)
- confidence (qualitativ, vorläufig)

## Evidenz Record (vorläufig)
- source (paper, dataset, measurement, proof)
- method (formal | empirical | computational)
- quality (notes)
- uncertainty (falls relevant)

