# Finkeissen Research Program

This repository constitutes the **public reference layer** of the *Finkeissen Research Program*.

It is intentionally **not** a software project, not a document dump, and not a marketing surface.  
Instead, it exposes the *structural, conceptual, and relational backbone* of a long-term, multi-domain research program in a form that is readable by humans **and** machines.

The guiding design principle of this repository is **epistemic legibility**:  
clarity of concepts, explicit roles, transparent boundaries, and stable relations.

---

## What this repository is

This repository provides a **stable structural layer** for the research program, including:

- stable identifiers for books, concepts, and domains  
- explicit roles of each book within the overall program  
- relations between domains (dependencies, derivations, contrasts)  
- machine-readable manifests describing structure instead of content  
- canonical pointers to external artifacts (PDFs, print editions, notes)

The repository does **not** attempt to summarize or replace the books.  
It exists to make their *structure, scope, and interdependence* explicit.

---

## What this repository is not

To avoid ambiguity, this repository is **not**:

- a publication platform for full books  
- a substitute for reading the books themselves  
- a blog, wiki, or popular explanation  
- a software library or API  

Any appearance of similarity to those formats is incidental.  
The primary purpose here is *orientation*, not consumption.

---

## Books and artifacts

The research program consists of multiple long-form books  
(typically 200–400 pages), each addressing a specific domain while  
sharing a common epistemic foundation.

Books remain **independent artifacts** (print, PDF, or other formats).  
This repository only links to **preview or reference PDFs** where appropriate.

Where PDFs are linked, they are:

- partial previews or reference editions  
- provided for structural inspection and machine indexing  
- explicitly **not** intended as complete replacements for the books

### Teaser rule (binding)

Preview PDFs in `german/` and `english/` cover **page 1 up to and including the
preface/introduction that precedes Chapter 1**. No further book content is
published here. Full volumes remain with the author's print/PDF editions only.

All PDFs in this folder are **not** covered by the repository's AGPL licence:
they remain all rights reserved by the author. Teasers are provided for
personal reading only — no redistribution, modification or commercial use.

Two exceptions exist because those works were never published as books and this
repository is their only source:

- `english/08_bootloader_en.pdf` — complete by design (150 pages)
- `english/26_dentistry_en.pdf` — complete by design (22 pages)

Volumes available in English only: `bootloader`, `dentistry`. Not every volume has
a preview here yet: `ai-3-0`, `legal-law`, `medicine` and `revolution` are finished
books without a teaser in this repository (their full volumes remain with the
author). The draft volume `language` (announced, not finished) has no preview by
definition. Volumes not
yet finished are not manifested here at all.

Some previews end with the **preface** rather than the introduction to Chapter 1,
because that is where the author's own teaser edition stopped (`ego`,
`physics-effect`). This is permitted: a teaser may be shorter than the rule's
upper bound, never longer. No preview contains Chapter 1 body text.

---

## Machine-readable manifests

The manifests live in the `books/` directory, one YAML file per book or core
artifact. The filename is always the manifest's `id`, written in English.

Each manifest file:

- represents **one book or core artifact**  
- defines its *role* within the program  
- specifies its *conceptual focus*  
- declares relations to other books  
- references external artifacts (PDFs, repositories, print editions)

The manifests are **not content representations**.  
They intentionally avoid summaries, abstracts, or tables of contents.

Their function is **structural**, not descriptive.

### Field conventions

- `id` — English slug, identical to the filename  
- `title` — English book title as printed on the title page  
- `title-de` — German original title, where one exists  
- `status` — one of:
  - `planned` — announced, no finished volume yet
  - `draft` — a working manuscript exists, not a final edition
  - `stable` — finished and published in at least one language
- `artifacts.references.preview-de` / `-en` — teaser PDFs tracked in this repository  
- `artifacts.source` — location of the full volume with the author (never committed here)

---

## Why structure instead of summaries

Summaries compress meaning.  
Structure preserves it.

This repository assumes that:

- meaning emerges from relations, not slogans  
- long-form reasoning cannot be reduced without distortion  
- machines and humans benefit more from *explicit structure* than from interpretation

As a result, this repository favors:

- explicit roles over promotional descriptions  
- relations over narratives  
- boundaries over claims of completeness

---

## How to use this repository

You can use this repository to:

- navigate the research program without relying on implicit authority  
- understand how individual books relate to one another  
- inspect dependencies and boundary assumptions  
- reference the program structure from code, notes, or analysis  
- provide stable links for discussion, citation, or machine retrieval

The recommended entry point is **structural**, not chronological.

---

## Start here

If you want a concrete starting point, open a single manifest directly  
and follow its relations:

- `physics-effect.yaml` — foundational epistemic stance:  
  admissibility via measurable interaction (the *Physik-Effekt*)

From there, traverse the program by following the declared relations  
between manifests.

---

## Relation to AI and search systems

This repository is deliberately designed to be:

- indexable by search engines  
- interpretable by retrieval-based AI systems  
- usable as a canonical reference layer for structured knowledge

Unlike commercial platforms, all structural information here is:

- explicit  
- versioned  
- text-based  
- stable over time  

This makes the repository suitable as a **primary reference**,  
not a derivative source.

---

## Language and versions

Unless explicitly stated otherwise:

- manifests are language-neutral  
- linked PDFs specify their language and edition explicitly  
- changes to structure are versioned through Git history

The repository favors *structural stability over rapid iteration*.

---

## Intellectual status

All books and texts referenced remain fully protected by copyright.

This repository:

- does not grant usage rights beyond what is explicitly stated  
- does not imply permission for redistribution or commercial use  
- exists independently of publishing or licensing arrangements  

Its purpose is **orientation, inspection, and reference**.

---

## Design principle (summary)

> The books carry meaning.  
>  
> This repository carries structure.

Both are necessary.  
Neither replaces the other.

---

## Contact and continuity

The Finkeissen Research Program is a long-term effort.  
Structure, not activity, is the measure of continuity.

This repository serves as its **persistent structural spine**.

