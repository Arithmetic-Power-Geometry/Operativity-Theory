# Certification Under Evolving Observability

This repository contains the software, formal specification, tests, external case abstractions, and reproducible computational evaluation for:

**Mohammad Amir Khusru Akhtar (2026). _Certification Under Evolving Observability: Operativity, Latent Invalidators, and Causal Diagnostic Robustness_. Version V1. Zenodo. https://doi.org/10.5281/zenodo.22901704**

## Overview

The study examines preservation claims when a transformation can change which verifiers become realizable later.

A complete state is represented as

```
omega = (x, g)
```

where `x` is the ordinary system configuration and `g` is verifier-generating structure.

The central quantities are:

- **PC(a, omega)** — Present Certification: preservation under currently realizable verifiers.
- **APS(a, omega)** — Absolute Preservation Stability: preservation under verifiers reachable after the transformation and admissible continuation.
- **SIP(a, omega)** — Self-Invalidating Preservation: `PC && !APS`.
- **IL(a, omega)** — Invalidation Latency: minimum continuation depth at which a distinguishing verifier becomes reachable.

For effective product-state representations, APS reduces to ordinary BAD-state reachability. The framework is therefore a transformation-relative certification and diagnostic layer, not a replacement model checker and not an expressiveness-separation claim against general temporal, hyperproperty, or product-state verification.

## Main formal results

The repository includes formal statements and proofs/sketches for:

- latent invalidator characterization;
- verifier-partition stability;
- singleton reachability transfer;
- decidability and undecidability transfer results;
- augmented relational-safety reduction;
- fixed-vocabulary compatibility strictness under transformation-conditioned future observability.

See `THEORY.md`, `THEOREMS.md`, `DECIDABILITY_BOUNDARY.md`, and `COMPATIBILITY_GENERALIZATION.md`.

## Computational evaluation

The reproducible evaluation reported in the paper includes:

- exhaustive enumeration of **144 finite systems**;
- **100** PC-true systems;
- **64** APS-true systems;
- **36** SIP cases;
- **36** explicit counterexamples to `PC => APS`;
- **0** latent-invalidator characterization violations;
- **4/4** verdict agreement with an independently implemented product-state BFS baseline on controlled evolution scenarios;
- four externally grounded evolution cases;
- a distractor-robustness benchmark using 0, 5, 10, 25, and 50 non-causal observables.

In the distractor benchmark, causal nearest-upstream selection retained **100% diagnostic relevance** at every tested distractor level. At 5 distractors, nearest, cheapest, and random difference baselines scored 50%, 0%, and 25%, respectively. At 10, 25, and 50 distractors, they scored 50%, 0%, and 0%.

These results are controlled benchmark results. They do not establish universal production-system superiority or a new model-checking decision procedure.

## Reproducibility

Run the computational evaluation locally with:

```bash
python -m src.run_experiments
```

The GitHub Actions workflow at `.github/workflows/operativity-artifacts.yml` executes the test suite and computational evaluation and uploads machine-readable outputs.

## Repository structure

- `src/` — implementation and experiment runners
- `tests/` — automated tests
- `external_encodings/` — external evolution-case encodings
- `external_case_corpus.csv` — external case corpus
- `external_ground_truth_labels.json` — source-grounded diagnostic labels
- `external_blind_labels.json` — blind-label evaluation data
- `THEORY.md` — formal definitions
- `THEOREMS.md` — theorem package
- `ALGORITHM.md` — computational procedures
- `SPECIFICATION_PATTERN.md` — transformation-relative certification pattern

## Citation

Akhtar, M. A. K. (2026). *Certification Under Evolving Observability: Operativity, Latent Invalidators, and Causal Diagnostic Robustness* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22901704
