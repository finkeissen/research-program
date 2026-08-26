research-program/CONCURRENCY_MODEL.md
# Concurrency Model

## Purpose

This document defines structural rules for concurrent operations
within Layers 0–5.

It does not define execution engines.
It defines admissibility constraints under concurrency.

Concurrency must not introduce:

- implicit prioritization
- hidden authority
- race-based legitimacy
- structural reinterpretation
- silent conflict resolution


---

# 1. Principle of Temporal Neutrality

No artifact gains legitimacy due to:

- earlier timestamp
- later timestamp
- execution order
- processing speed
- system latency

Temporal order does not imply authority.

All ordering effects must be explicitly represented,
not implicitly interpreted.

---

# 2. Concurrent Runs

Multiple runs may execute simultaneously.

Constraints:

- Runs must declare full scope.
- Runs must declare affected artifacts.
- Runs must not mutate shared artifacts.
- Read-only applies strictly.

If two runs produce conflicting outputs:

- both outputs are recorded.
- conflict is represented in Matrix.
- no automatic winner selection.

Resolution belongs to Layer 6.

---

# 3. Actor Neutrality

Concurrent actors:

- must be structurally equal.
- must not gain authority by volume.
- must not gain authority by persistence.
- must not gain authority by repetition.

Repeated submission does not imply legitimacy.

---

# 4. Write Isolation

Under concurrency:

- No run may modify hypothesis artifacts.
- No run may modify prediction artifacts.
- No run may modify integration rules.
- No run may modify Matrix history.

All writes must target declared output paths only.

Violation triggers STOP.

---

# 5. Conflict Under Concurrency

If two runs produce structurally incompatible artifacts:

- both artifacts remain valid representations.
- incompatibility must be recorded.
- no structural reconciliation is permitted internally.

The system may represent conflict.
It may not resolve conflict.

---

# 6. Version Interaction

If a hypothesis is versioned while a run is active:

- the run remains bound to the version declared at start.
- no implicit upgrade permitted.
- no retroactive mutation permitted.

Version binding must be explicit in run-manifest.

---

# 7. Deadlock and Structural Stall

If concurrency produces structural deadlock:

- deadlock must be represented.
- no implicit override permitted.
- no authority may be assigned to break it.

Resolution must occur outside Layers 0–5.

---

# 8. STOP Propagation Under Concurrency

If STOP is triggered in one run:

- it affects only that run.
- it does not invalidate parallel admissible runs.
- it does not escalate automatically.

Global STOP may only originate from Layer 1 invariant violation.

---

# 9. Scaling Constraint

Concurrency must not require:

- prioritization heuristics
- voting mechanisms
- arbitration algorithms
- majority resolution
- implicit ranking

If scaling demands arbitration inside Layers 0–5,
architecture has failed.

---

# 10. Audit Requirements

Each concurrent run must record:

- start timestamp
- bound artifact versions
- declared scope
- declared outputs

Concurrency must be reconstructable from logs.

---

# 11. Non-Authority Statement

Concurrency does not produce authority.

Parallel execution does not imply legitimacy.

Volume does not imply correctness.

Persistence does not imply priority.

Authority remains external.


