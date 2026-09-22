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


## Compatibility-generalization result

T17 establishes a scoped strictness result. Any compatibility semantics determined solely by a preservation pair and a transformation-independent verifier/test family embeds as the fixed-vocabulary case of TCOP. The extension is strict when a transformation makes reachable a new verifier outside the fixed family that distinguishes the pair.

This is a genuine mathematical separation from fixed-vocabulary compatibility, but NOT an expressiveness separation from HyperLTL, temporal logic, product-state verification, dynamic-update logics, or compatibility frameworks that explicitly model future environment/observer evolution.

### Q1 implication
This improves the theoretical contribution from a mere notation/pattern proposal to a conservative-extension theorem with a constructive strictness witness. Strong-Q1 readiness nevertheless still requires evidence that fixed-vocabulary compatibility is a practically important limitation and that TCOP improves specification engineering on external cases.


## Final T17 audit — theory frozen

The strongest neighboring work includes client-oriented dynamic-software-update specifications, behavioral DSU verification, changing-requirement runtime verification, and instrumentation-driven evolution-aware runtime verification. These eliminate broad claims of novelty in update correctness, observer evolution, relational old/new behavior, and evolution-aware monitoring.

T17 survives only in its already restricted form: strict conservative extension of compatibility semantics whose test/verifier vocabulary is fixed independently of the transformation. Rich DSU/RV/temporal/hyperproperty formalisms that model observer evolution are outside this comparison class.

**Theory freeze:** no further primitive hunting. Q1 advancement now requires external empirical specification-engineering evidence.


## Make-or-break external TC search

Under the frozen full-TC criterion, the external search did not establish a robust set of multiple independent published cases in which the transformation being certified itself creates the later distinguishing observation capability while the preservation obligation remains fixed.

This is recorded as a negative empirical result. On current evidence, TCOP should not be promoted as a strong-Q1 verification-method contribution. Recommended current positioning is a focused formal framework/specification-pattern paper with T17, reproducible software, scoped claims, and explicit negative controls. Reopen the strong-Q1 methods claim only with independent full-TC real systems or substantial controlled specification-engineering evidence.

## 22 September 2026 evidence update

The evaluation has advanced beyond the earlier three-case baseline stage. A fourth source-grounded external evolution case was added and the full workflow passed in run 102. A subsequent distractor-robustness benchmark passed in run 106.

Key measured result from run 106:
- at 0 distractors, nearest, cheapest, random, and causal selectors all score 4/4;
- at 5 distractors, nearest = 2/4, cheapest = 0/4, random = 1/4, causal = 4/4;
- at 10, 25, and 50 distractors, nearest = 2/4, cheapest = 0/4, random = 0/4, causal = 4/4.

This establishes a controlled diagnostic-robustness advantage for the causal nearest-upstream selector within the declared benchmark. It does not establish universal superiority, production-system effectiveness, or a new verification decision procedure. Independent expert annotation and a larger natural external corpus remain the strongest validation extensions.

**Current manuscript gate:** sufficient evidence exists to write the full paper now. For a strong-Q1 submission, the current package is materially stronger than the earlier status, but independent expert/real-system validation would still improve the empirical claim.
