# Theorem Package

## T1. Present/Absolute Separation
There exist finite operative certification systems and transformations `a` with `PC(a,omega)=true` and `APS(a,omega)=false`.

## T2. Latent Invalidator Characterization
Let `D(a,omega)={v : v(x) != v(x_a)}`. Then:
```
APS(a,omega) iff D(a,omega) intersect V_inf(a,omega) = empty.
```
If PC holds:
```
SIP(a,omega) iff D(a,omega) intersect (V_inf(a,omega) \ V(omega)) != empty.
```

## T3. Verifier-Partition Stability
Assume `V(omega) subseteq V_inf(a,omega)`. Present and absolute observational equivalence coincide uniformly on X iff:
```
Pi(V(omega)) = Pi(V_inf(a,omega)).
```
Equivalently, every reachable future verifier is constant on every present observational equivalence class.

## T4. Computationally-Universal APS Undecidability
For effectively presented systems whose verifier-generation dynamics can simulate an arbitrary Turing machine, universal decision of APS is undecidable.

Reduction:
1. encode machine M and input w;
2. execute a present-certified transformation;
3. simulate M(w) in verifier-generation dynamics;
4. enable one distinguishing verifier iff M(w) halts.

An APS decider would decide the halting problem.

## T5. Singleton-Emergence Undecidability
T4 persists even when at most one new semantic verifier can emerge:
```
|V_inf(a,omega) \ V(omega)| <= 1.
```
The source of undecidability is therefore reachability of a latent invalidator, not an unbounded verifier vocabulary.

## T6. Finite Explicit-State Decidability
If the reachable complete-state graph is finite and explicit and verifier availability/evaluation are decidable, then V_inf is computable by graph reachability and APS is decidable.

## T7. Finite Reachable-Quotient Decidability
APS remains decidable for a possibly infinite concrete system whenever there exists an effectively computable finite quotient Q satisfying:
1. every reachable concrete complete state maps to a state of Q;
2. quotient reachability is sound and complete for verifier availability;
3. for every verifier capable of distinguishing x from x_a, availability is decidable on Q;
4. verifier evaluation on x and x_a is decidable.

Then APS reduces to finite reachability of a distinguishing-verifier label in Q.

This strictly improves T6: finiteness of the concrete state space is sufficient but not necessary.

## T8. Decidability Sandwich
The established boundary is currently a sandwich, not an exact frontier:
```
effective finite verifier-reachability quotient
        => APS decidable

computationally universal verifier genesis
        => APS undecidable
```

Infinite-state alone is not an undecidability criterion: known verification theory contains both decidable and undecidable infinite-state classes. Therefore the exact weakest boundary cannot be identified merely with finiteness, infiniteness, self-modification, or changing observations.

## Open Boundary Problem
Characterize the weakest structural conditions between T7 and T4/T5 under which latent-invalidating-verifier reachability changes from decidable to undecidable.

This remains open and is not claimed as solved.
