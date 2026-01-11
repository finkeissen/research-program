```markdown
# Epistemic Boot Sequence (BIOS-mode)

**Status:** Normative reference (Single Source of Truth)

This document defines the **first-stage boot** of the epistemic stack: **BL-0 … BL-4 (BIOS-mode)**.
It also defines the **handover boundary** to **BL-5 (second-stage research mode init)** and to the **Science OS**.

---

## 0. Purpose

BIOS-mode initializes the **preconditions for rational operation**.
It does **not** do science. It does **not** justify outcomes.
It creates the minimal conditions under which a scientific operating regime can be started and maintained.

---

## 1. Key terms (canonical)

- **BL (Boot Layer):** a numbered stage in the boot sequence. BL is about order and dependency.
- **BIOS-mode:** the metarational first-stage boot context (BL-0…BL-4).
- **Second-stage boot:** post-BIOS initialization of a specific operating mode (here: research mode).
- **Science OS:** sustained scientific operation (methods, models, theories, revision cycles).
- **Downstream systems (e.g., MMS):** operational systems that execute decisions and carry responsibility.

---

## 2. Non-negotiable boundary

### 2.1 BIOS-mode is **IN**
BIOS-mode may only do:
- detect non-viability (irritation)
- formulate minimal requirements (better/worse, not true/false)
- specify operational constraints (“logic spec”)
- commit to those constraints as binding
- hand over to OS / second-stage boot

### 2.2 BIOS-mode is **OUT**
BIOS-mode must not do:
- scientific truth claims about the world
- method selection (“use statistics / experiment X / tool Y”)
- model or theory building
- domain claims (“X causes Y”, “humans are…”, “society is…”)
- moral/ethical responsibility commitments (these belong downstream)

**Hard rule:** BIOS-mode ends where logic is no longer chosen, but assumed.

---

## 3. Invariants (apply to BL-0…BL-4)

1. **No scientific truth claims.**
2. **No method/tool selection.**
3. **No theories/models.**
4. **No hidden premises:** outputs must be explicit, minimal, and versionable.
5. **No responsibility commitment:** responsibility begins in downstream execution (e.g., MMS).
6. **Regression is allowed, but controlled:** foundational conflicts are handled via explicit re-entry rules (see BL-4).

---

## 4. Artifact model

BIOS-mode produces only a small set of artifacts. They are intentionally compact.

- **A0 — Irritation Artifact (BL-0):**
  - one non-viability statement
  - one concrete symptom
  - stability check (persistent / not persistent)
  - boundary statement (“no truth claim”)

- **A1 — Requirements Artifact (BL-1):**
  - 3–7 minimal requirements
  - priority order (P1…Pn)
  - one anti-requirement (explicit non-optimization target)

- **A2 — Logic Spec (BL-2):**
  - baseline posture (1 line)
  - allowed moves
  - forbidden moves
  - contradiction policy
  - revision rule

- **A3 — Commitment Package (BL-3):**
  - commitment statement
  - enforcement/consequences (operational)
  - non-reopening clause (no BL-2 debates inside OS)
  - stop condition

- **A4 — Handover Note (BL-4):**
  - BIOS complete declaration
  - pointers to next stage (BL-5 default variant + OS)
  - re-entry rule (when/how to return to BL-2/BL-1)

---

## 5. Phases (BIOS-mode)

Each phase is defined by:
- **Function**
- **Entry condition**
- **Output artifact**
- **Exit condition**
- **Failure modes**
- **Non-goals**

---

### BL-0 — Irritation Detection

**Function**
Detect and stabilize a **non-viability signal**: “this cannot continue as-is”.
This is pre-logical and non-explanatory.

**Entry condition**
There exists an operational situation (personal/social/system) with sustained friction/tension.

**Output artifact**
A0 — Irritation Artifact.

**Exit condition**
A stable irritation signal exists:
- not a single spike
- not a mood-only report
- expressed operationally (what cannot continue)

**Failure modes**
- denial (“nothing is wrong”)
- distraction (topic switching)
- aestheticization (“it’s just complex”)
- rumination loop (endless talking without a statement)
- premature explanation (causal stories)

**Non-goals**
- no “why” explanations
- no diagnosis of reality
- no blame allocation
- no optimization plan

---

### BL-1 — Minimal Requirements

**Function**
Convert irritation into **minimal pre-logical requirements** for a more viable regime.
The axis is **better/worse**, not **true/false**.

**Entry condition**
A0 exists (explicit non-viability statement + symptom).

**Output artifact**
A1 — Requirements Artifact.

**Exit condition**
3–7 requirements exist and are:
- operational (observable indicators)
- minimal (not utopian)
- prioritized
- accompanied by one anti-requirement

**Failure modes**
- maximalism (“perfect certainty”)
- moralization (“should be fair” without operational indicator)
- vagueness (“be better”)
- requirement inflation (too many / conflicting)
- hidden reintroduction of truth claims

**Non-goals**
- no choice of scientific methods
- no epistemic proof system yet
- no model assumptions

---

### BL-2 — Logic Design

**Function**
Specify the operational constraints that will satisfy BL-1:
a compact **Logic Spec** that defines what moves are allowed/forbidden and how contradictions are handled.

**Entry condition**
A1 exists and priorities are explicit.

**Output artifact**
A2 — Logic Spec.

**Exit condition**
The Logic Spec is explicit enough to be used as a rule set:
- allowed moves defined
- forbidden moves defined
- contradiction policy defined
- revision rule defined

**Failure modes**
- implicit assumptions (“obvious” rules that are not written)
- dogmatic axioms (unargued absolutes)
- overformalization (complexity that blocks use)
- under-specification (“be consistent” without policy)
- philosophical derailment (debate replaces spec)

**Non-goals**
- no scientific claims
- no method selection
- no “proof that logic is correct”
- no attempt to eliminate uncertainty (only to manage it)

---

### BL-3 — Rational Commitment

**Function**
Normative self-binding: treat the Logic Spec as **binding** for coordination.
This is the “start button” for rational operation.

**Entry condition**
A2 exists (Logic Spec is explicit).

**Output artifact**
A3 — Commitment Package.

**Exit condition**
Commitment is explicit and enforceable:
- rules are binding
- consequences are operational (flag/log/correct)
- non-reopening clause exists (BL-2 debates are scheduled, not injected)
- stop condition exists

**Failure modes**
- hedging (“unless I feel like it”)
- exception obsession (rewriting rules during commitment)
- performative commitment (no enforcement)
- silent escape hatch (implicit “I’ll ignore it later”)

**Non-goals**
- no scientific output
- no evaluation of theories
- no downstream responsibility commitments

---

### BL-4 — BIOS → OS Handover

**Function**
Seal BIOS-mode and hand over control to OS operation and optional BL-5 second-stage boot.

**Entry condition**
A3 exists (commitment is explicit).

**Output artifact**
A4 — Handover Note.

**Exit condition**
BIOS completion is declared and enforced:
- logic is now assumed (not re-justified)
- next stage is explicitly pointed to (BL-5 default variant + OS)
- re-entry rule exists for foundational conflicts

**Failure modes**
- regression loop (reopening BL-2 inside OS)
- meta-discussion trap (debating the architecture instead of operating it)
- premature “science claims” (claiming scientific status by declaration)

**Non-goals**
- no additional logic debates
- no method selection
- no responsibility step (belongs downstream)

---

## 6. Re-entry rule (foundation maintenance)

Foundational conflicts may occur during OS operation. When they do:

- OS must **pause** any claim of “scientific operation”
- the conflict must be logged as a **foundational incident**
- the system must **re-enter** BIOS-mode at the correct point:

### 6.1 Default mapping
- Conflict about rule application / contradictions → re-enter **BL-2**
- Conflict about what should be optimized (criteria drift) → re-enter **BL-1**
- Conflict about whether there is any stable non-viability at all → re-enter **BL-0**

**Hard rule:** Re-entry is explicit and logged. BIOS is not silently re-run inside OS.

---

## 7. Post-BIOS: Second-stage boot (BL-5)

After BL-4, a second-stage boot may initialize **Research Mode**.

### 7.1 What BL-5 does
BL-5 initializes a research workflow **within an already rationally booted system**:
- roles (operator/recorder/challenger)
- artifacts (question, assumptions, logs, versioned claims)
- rules (status tags, contradiction logging, definition versioning)
- cadence (observe → claim → test → revise)
- exit criteria

### 7.2 BL-5 variants
BL-5 can exist in multiple guidance levels:
- `raw` (minimal framing)
- `raw-medium` (structured, default)
- `medium` (onboarding)

These variants share the same function; they differ only in explicitness.

---

## 8. OS and downstream: what happens next

### 8.1 Science OS (post-BIOS)
The OS runs scientific work:
- methods and tools
- models and theories
- revision cycles (replicate/refute/refine)
- kernel-like functions (consistency/error handling)

BIOS-mode is not re-litigated in OS.

### 8.2 Downstream systems (e.g., MMS)
Downstream systems execute decisions and therefore boot additional obligations:
- goals
- risk acceptance
- responsibility (ethics/legal/operational constraints)
- monitoring, rollback, incident reporting

**Boundary sentence:** Science is responsible for correctness of its procedure; responsibility for consequences begins where decisions are executed downstream.

---

## 9. File mapping (repo contract)

This document is normative. The repo should map artifacts as follows:

- `docs/boot-sequence.md`  ← this file (SSOT)
- `docs/diagrams/boot-sequence.mmd`  ← diagram source (no SVG inside)
- `docs/diagrams/boot-sequence.svg`  ← optional generated render (derived)
- `bootloader/BL-0-… .prompt` … `bootloader/BL-4-… .prompt`  ← operational prompts for BIOS-mode
- `bootloader/BL-5-ResearchModeInit-*.prompt`  ← second-stage research init
- `downstream/mms.md`  ← pointer + boundary to MMS implementation

**Consistency rule:** Prompts must not introduce normative content that is not defined here.
```

