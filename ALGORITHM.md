# APS Analysis Algorithm

## Goal

Given a transformation a, reference complete state omega, and an effective product representation, decide present certification and search for latent invalidation.

## Product state

A product node stores:

```
(reference x, transformed state y, verifier-generator state g)
```

The reference is fixed. The transformed/generator components evolve.

## BAD predicate

```
BAD(x,y,g)
iff
exists verifier v available at g:
    v(x) != v(x_a)
```

For the current finite implementation x_a is the ordinary transformed configuration fixed immediately after a. Extensions may use a declared preservation target semantics.

## Algorithm

1. Evaluate every currently available verifier.
2. If one distinguishes x from x_a, return IMMEDIATE_INVALID.
3. Initialize graph search from the complete post-transformation state.
4. Explore reachable product states.
5. At each state inspect newly/currently available verifiers.
6. If any distinguishes x from x_a:
   - return LATENT_INVALID;
   - return the shortest witness path;
   - return the invalidating verifier;
   - return invalidation latency.
7. If finite/effectively exhausted with no BAD state, return ABSOLUTELY_STABLE.
8. If the chosen generator class does not admit complete exploration, return UNKNOWN unless a sound abstraction proves safety.

## Output classes

```
IMMEDIATE_INVALID : PC = false
LATENT_INVALID    : PC = true, APS = false
ABSOLUTELY_STABLE : APS = true
UNKNOWN           : analysis incomplete
```

The UNKNOWN outcome is essential for sound use on classes where exhaustive reachability is unavailable.

## Baseline

The minimal baseline is present-only certification:

```
BASELINE(a,omega) = PC(a,omega)
```

It necessarily misses every LATENT_INVALID case by definition.

Stronger experimental baselines must include established reachability/model-checking approaches on the same product representation. The contribution cannot be claimed merely from outperforming the deliberately weaker PC baseline.
