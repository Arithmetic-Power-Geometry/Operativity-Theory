# Theorem Package

## T1. Present/Absolute Separation

There exist finite operative certification systems and transformations `a` such that:

```
PC(a, omega) = true
APS(a, omega) = false
```

## T2. Latent Invalidator Characterization

Let:

```
D(a, omega) = { v : v(x) != v(x_a) }
```

Then:

```
APS(a, omega)
iff
D(a, omega) intersect V_inf(a, omega) = empty
```

If `PC(a, omega)` holds, then:

```
SIP(a, omega)
iff
D(a, omega) intersect (V_inf(a, omega) \ V(omega)) != empty
```

## T3. Verifier-Partition Stability

Assume `V(omega) subseteq V_inf(a, omega)`.

Present observational equivalence and absolute observational equivalence coincide uniformly on `X` iff:

```
Pi(V(omega)) = Pi(V_inf(a, omega))
```

Equivalently, every reachable future verifier is constant on every equivalence class induced by the current verifier family.

## T4. Unrestricted APS Undecidability

For effectively presented operative certification systems with computationally universal verifier-generation dynamics, universal decision of `APS(a, omega)` is undecidable.

Reduction idea:
- encode machine `M` and input `w`,
- perform a present-certified transformation,
- effectively simulate `M(w)`,
- enable a distinguishing verifier iff the simulation halts.

A universal APS decider would therefore decide halting.

## T5. Singleton-Emergence Undecidability

The undecidability in T4 persists even when:

```
|V_inf(a, omega) \ V(omega)| <= 1
```

Thus undecidability does not require an unbounded family of emergent verifiers.

## T6. Finite Explicit-State Decidability

If:
- the complete state space is finite,
- admissible transitions are finite and explicit,
- verifier availability is decidable,
- verifier evaluation is decidable,

then `V_inf(a, omega)` is computable by finite graph reachability and `APS(a, omega)` is decidable.

## T7. Open boundary problem

Characterize the weakest verifier-generating system class for which APS crosses from decidable to undecidable.

This is intentionally left as the next theorem target.
