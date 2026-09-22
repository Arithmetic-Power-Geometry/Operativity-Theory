# Final T17 Adversarial Audit

## Purpose

This is the final novelty attack on T17. No further primitive hunting follows from this audit.

## Closest prior art

### Dynamic software updating (DSU)
Client-oriented specifications can express rich client-visible behavioral correctness across updates, including backward-compatible, post-update, and conformable properties. Old and new programs can be merged and checked with off-the-shelf tools.

### Behavioral DSU verification
Algebraic/model-checking approaches verify that dynamically updated systems satisfy desired behavioral properties.

### Changing-requirement runtime verification
Runtime monitors can be adapted when requirements change while preserving accumulated verification knowledge.

### Evolution-aware instrumentation
Recent runtime-verification work safely reuses instrumentation across program revisions and re-monitors specifications, explicitly coupling software evolution and monitoring infrastructure.

## Result

These works invalidate any broad claim that TCOP is the first formalism for:
- update correctness;
- changing observers/monitors;
- evolution-aware monitoring;
- relational old/new behavior;
- verification after interface change.

They do NOT invalidate the scoped T17 theorem because T17's comparison class is explicitly limited to compatibility semantics whose verifier/test vocabulary is fixed independently of the transformation.

Rich DSU, temporal, HyperLTL, product-state, and evolution-aware RV formalisms lie outside that restricted class whenever they encode observer/environment evolution.

## Frozen theorem claim

T17 may be stated only as:

> TCOP conservatively extends fixed-vocabulary compatibility semantics; the extension is strict when the transformation makes reachable a new verifier outside the fixed family that distinguishes the preservation pair.

Do not state or imply that TCOP is more expressive than general temporal logic, HyperLTL, DSU verification, runtime verification, or product-state model checking.

## Final research direction

Theory is now frozen. No additional primitives or theorem-number expansion should be pursued merely to rescue novelty.

Remaining work is empirical:
1. assemble independent compatibility/evolution cases;
2. encode them with expert conventional specifications;
3. encode them with TCOP;
4. compile TCOP to the same backend;
5. compare correctness, specification size, auxiliary modeling, authoring effort, and errors;
6. reassess venue level from evidence.

If this empirical comparison is not favorable, position the work as a focused formal framework/pattern paper rather than a strong-Q1 methods paper.
