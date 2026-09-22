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
