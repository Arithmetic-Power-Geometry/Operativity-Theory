# Frozen Theory Specification

## 1. Complete state

A complete state is

```
omega = (x, g)
```

where:
- `x` is the ordinary system configuration,
- `g` is the verifier-generating structure.

An admissible transformation is

```
a : omega -> omega_a
```

with `omega_a = (x_a, g_a)`.

## 2. Verifiers

Each semantic verifier `v` is a total observation map on ordinary configurations:

```
v : X -> Y_v
```

`V(omega)` denotes the verifiers physically realizable at `omega`.

For a transformation `a`, define the transformation-relative future verifier closure:

```
V_inf(a, omega)
```

as every verifier that becomes realizable after executing `a` and then following any admissible continuation.

## 3. Present Certification

```
PC(a, omega)
iff
for every v in V(omega): v(x) = v(x_a)
```

## 4. Absolute Preservation Stability

```
APS(a, omega)
iff
for every v in V_inf(a, omega): v(x) = v(x_a)
```

## 5. Distinguishing set

```
D(a, omega) = { v : v(x) != v(x_a) }
```

Hence:

```
APS(a, omega)
iff
D(a, omega) intersect V_inf(a, omega) = empty
```

and

```
PC(a, omega)
iff
D(a, omega) intersect V(omega) = empty
```

## 6. Self-Invalidating Preservation

```
SIP(a, omega)
iff
PC(a, omega) and not APS(a, omega)
```

Equivalently, assuming PC:

```
SIP(a, omega)
iff
D(a, omega) intersect (V_inf(a, omega) \ V(omega)) != empty
```

## 7. Invalidation Latency

```
IL(a, omega)
```

is the minimum continuation depth at which a newly realizable verifier distinguishes `x` from `x_a`; `IL = infinity` if no such verifier is reachable.

## 8. Observational partitions

For a verifier family `V` define:

```
x ~_V y
iff
for every v in V: v(x) = v(y)
```

and let `Pi(V) = X / ~_V`.

Present and absolute equivalence coincide uniformly exactly when reachable verifier generation does not strictly refine the present observational partition.

## 9. Novelty target

The theory is not claiming novelty for changing monitors, evolving specifications, runtime verification, self-modification, refinement, or expanding observations separately.

The specific target is the conjunction:

```
Transformation
-> transformation-dependent verifier generation
-> newly realizable distinction
-> invalidation of that transformation's own preservation claim
```

## 10. Scope discipline

This repository treats Operativity Theory as a formal research program. It does not claim that a new top-level scientific discipline has already been established.


## 11. Generated-verifier extension

When future verifier identities are not fixed in advance, use an effective verifier language L and transformation-conditioned generator G_a(omega). The generated latent invalidator problem asks whether some operationally generated verifier description p satisfies:

```
[[p]](x) != [[p]](x_a).
```

For a fixed preservation pair define the pair-semantic equivalence:

```
p ~_(x,x_a) q
iff
([[p]](x),[[p]](x_a)) = ([[q]](x),[[q]](x_a)).
```

APS depends only on the reachable pair-semantic quotient, not on verifier syntax itself. See GENERATED_VERIFIERS.md.
