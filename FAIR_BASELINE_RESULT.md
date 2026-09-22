# Fair Baseline Result

## Controlled scenarios

The current controlled scenario suite contains:
- API migration;
- authorization upgrade;
- instrumentation upgrade;
- stable authorization control.

APS was compared with an independently implemented conventional product-state breadth-first reachability analysis.

## Result

All four verdicts agree.

Three scenarios contain a reachable future verifier that distinguishes the preservation pair. Both APS and the conventional baseline classify them unsafe/latent-invalid.

The stable control is accepted by both.

## Scientific interpretation

This is a negative result for algorithmic novelty and a positive result for implementation validity.

It experimentally supports the product-state reduction theorem.

It does NOT support claims that APS:
- has greater decision power;
- finds violations conventional product reachability cannot find when given equivalent information;
- is inherently faster;
- constitutes a new model-checking algorithm.

## Remaining empirical question

Does the PC/APS/SIP formulation provide measurable specification or diagnostic value relative to established counterexample/explanation methods?

This must be evaluated against external benchmarks and established tools before a Q1 claim is justified.
