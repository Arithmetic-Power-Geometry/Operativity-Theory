# Operativity Theory

Operativity Theory studies preservation claims when the transformation being certified can change which verifiers become realizable in the future.

Core distinction:

```
certified now != stable under verifiers the transformation itself can enable
```

The repository contains:
- a frozen mathematical specification,
- theorem statements and proof sketches,
- a finite exact checker,
- reproducible experiments,
- GitHub Actions workflows that generate machine-readable artifacts.

## Core objects

A complete state is `omega = (x, g)`, where `x` is the ordinary configuration and `g` is the verifier-generating structure.

For a transformation `a`:
- `PC(a, omega)`: Present Certification.
- `APS(a, omega)`: Absolute Preservation Stability.
- `SIP(a, omega)`: Self-Invalidating Preservation, defined by `PC && !APS`.
- `IL(a, omega)`: Invalidation Latency.

The characteristic dependency is:

```
Transformation -> Verifier Genesis -> Retrospective Distinction -> Self-Invalidation
```

## Reproducibility

Run locally:

```bash
python -m src.run_experiments
```

The workflow `.github/workflows/operativity-artifacts.yml` runs the exact benchmark and uploads `operativity-results` as a GitHub Actions artifact.

## Latest reproducible evaluation

The current workflow includes exact finite validation, a conventional product-state reachability baseline, external evolution-case abstractions, causal observation synthesis, blind/source-grounded label evaluation, and a distractor-robustness benchmark.

Canonical workflow evidence reported from run 106 (commit `8d2a3e23bcb0574b93d3e469458198fee5d81259`):
- 144 finite systems exhaustively enumerated;
- 0 latent-invalidator characterization violations;
- 36 explicit counterexamples to `PC => APS`;
- 4/4 verdict agreement with an independent product-state BFS baseline on the controlled scenarios;
- causal upstream selection retained 100% diagnostic relevance across 0, 5, 10, 25, and 50 non-causal distractors, while simple nearest/cheapest/random difference baselines degraded once distractors were added.

These results support the repository's intended positioning: Operativity is a transformation-relative certification and diagnostic specification layer that compiles to established verification backends when an effective product representation exists. The repository does not claim a new model-checking decision procedure or an expressiveness separation from general temporal, hyperproperty, or product-state verification.
