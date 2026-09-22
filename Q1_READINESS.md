# Q1 Readiness Gate

This file separates mathematical correctness/reproducibility from journal-tier readiness.

## Current strengths
- Precise formal definitions of PC, APS, SIP, invalidation latency.
- Exact latent-invalidator characterization.
- Verifier-partition stability characterization.
- Singleton reachability-transfer theorem.
- Decidable/undecidable transfer corollaries.
- Pair-semantic quotient for generated verifier families.
- Reproducible software and CI artifacts.
- Exhaustive finite benchmark with zero characterization violations in the enumerated family.

## Current weaknesses
- Several initially proposed novelty primitives reduce to established areas: reachability, synthesis, abstraction refinement, dynamic verification, self-reference, or probe effects.
- The strongest results are currently structural unifications/transfer results rather than a clearly irreducible new theorem with broad consequences.
- No substantial real-world dataset/system case study yet.
- No comparison against existing runtime-verification / monitoring baselines.
- No theorem mechanization in a proof assistant.
- Cross-domain generality is conceptual rather than demonstrated.

## Q1 gate

Do not target a strong Q1 venue until at least one of these routes is completed:

### Route A — theorem route
Prove a nontrivial theorem that does not collapse to ordinary reachability/synthesis after natural state augmentation, preferably with a strict separation or complexity result specific to transformation-relative certification.

### Route B — formal-methods route
Turn the framework into a strong verification method with:
- algorithm;
- complexity analysis;
- realistic benchmark suite;
- baseline comparison;
- failure cases that existing present-only certification misses;
- statistically/experimentally meaningful evaluation.

### Route C — mechanized-foundations route
Machine-check the central definitions and theorems and combine them with a substantive new theorem or verified case study.

## Current verdict
Mathematically coherent and reproducible: YES.
Potentially publishable as a focused theory/framework paper: YES, after literature and evaluation strengthening.
Strong-Q1 ready: NOT YET.
New top-level branch established: NO.


## Fair-baseline result

The controlled realistic scenarios were compared against an independently implemented conventional product-state BFS baseline using the same complete state information.

Result:
- 4/4 safety verdicts agree;
- 3 controlled scenarios are latent-invalid;
- 1 stable control remains safe;
- no decision-power advantage is demonstrated for APS.

This confirms the relational-safety reduction rather than an algorithmic superiority claim.

### Locked claim restriction

Do not claim that APS is a new model-checking algorithm, has greater decision power than product-state reachability, or detects violations unavailable to a conventional verifier supplied with the same product-state model.

Any remaining Q1 contribution must be demonstrated in specification structure, diagnostic information, modeling economy, or another measured dimension against established explanation/verification methods.


## Counterexample-explanation collision audit

Counterexample explanation is already a mature research area, including trace minimization, fault localization, causal explanation, domain-specific explanation, and explanations for relational/hyperproperty violations.

Therefore the diagnostic tuple `(PC, APS, SIP, invalidating verifier, invalidation latency)` is not, by itself, sufficient evidence of Q1 novelty.

### Locked restriction
Do not claim novelty merely because APS names the first distinguishing verifier, returns a shortest witness, or localizes a latent violation.

### Remaining defensible route
Evaluate Operativity as a transformation-relative specification pattern for evolving observability/certification that compiles to established product-state/hyperproperty verification. The contribution must be demonstrated through specification economy, modeling clarity, reduced specification errors, or user/benchmark evidence—not superior decision power.


## Specification-gap audit

Closest-neighbor literature includes property-specification patterns, timed observer-pattern catalogs, HyperLTL, regression verification, reconfigurable monitors, and runtime verification with changing requirements. These cover most ingredients of the framework.

The remaining candidate gap is **Transformation-Conditioned Observability Preservation (TCOP)**: the preservation obligation is fixed, but the transformation being certified changes the reachable observation/verifier vocabulary over which preservation must hold.

No exact standard named pattern with this defining semantics was identified in the current audit. This is only a candidate gap, not a novelty proof. It must survive external-example mapping and expert baseline encodings.


## External recurrence result

A strict A/B/C audit was applied: transformation; transformation-induced change in observation capability; new observation exposing a compatibility/preservation distinction. Most dynamic-monitoring and schema-evolution examples satisfy only part of this chain. Upgrade-compatibility examples provide close recurrence of the full dependency shape.

This strengthens real-world motivation but means the phenomenon itself cannot be claimed as newly discovered. TCOP remains only a candidate cross-domain formal specification pattern. Strong-Q1 status still requires multiple independent full recurrences plus expert conventional encodings and measurable specification-engineering benefit.
