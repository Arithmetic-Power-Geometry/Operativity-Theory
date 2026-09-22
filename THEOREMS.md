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

## T4. Singleton Reachability-Transfer Theorem
Consider the fragment in which:
1. `PC(a,omega)` holds;
2. exactly one initially unavailable semantic verifier `v*` can emerge;
3. `v*(x) != v*(x_a)`;
4. `v*` becomes available exactly when the verifier-generator reaches a designated enabling set `F`.

Then:
```
APS(a,omega) iff F is not reachable after a.
SIP(a,omega) iff F is reachable after a.
```

Therefore, for any effectively presented verifier-generator class C, the singleton APS decision problem is computationally interreducible (up to complementation) with the corresponding reachability problem for C.

This is the structural decidability boundary: APS does not have one independent automata-theoretic frontier; in this fragment it inherits the reachability frontier of the verifier-generation formalism.

## T5. Computationally-Universal APS Undecidability
If verifier-generation dynamics can simulate a model with undecidable reachability/halting, singleton APS is undecidable by T4.

In particular, a two-counter Minsky generator suffices:
- encode machine M and input w;
- execute a present-certified transformation;
- enable the single distinguishing verifier v* iff the target/halting configuration is reached.

A universal APS decider would decide the machine reachability/halting problem.

## T6. Singleton-Emergence Undecidability
The undecidability in T5 persists with:
```
|V_inf(a,omega) \ V(omega)| <= 1.
```
The source of undecidability is reachability of a latent invalidator, not an unbounded verifier vocabulary.

## T7. Finite Explicit-State Decidability
If the reachable complete-state graph is finite and explicit and verifier availability/evaluation are decidable, then V_inf is computable by graph reachability and APS is decidable.

## T8. Effective Finite-Quotient Decidability
APS remains decidable for a possibly infinite concrete system whenever there exists an effectively computable finite quotient that is sound and complete for reachability of every distinguishing-verifier enabling condition.

Thus finiteness of the concrete state space is sufficient but not necessary.

## T9. Model-Class Transfer Corollaries
By T4, known reachability results transfer directly to singleton APS.

- Finite-state verifier generators: decidable.
- One-stack pushdown verifier generators: decidable.
- Petri-net / VASS verifier generators: decidable, despite infinite state spaces.
- Two-stack pushdown verifier generators: undecidable in general.
- Two-counter Minsky verifier generators: undecidable in general.

These are transfer corollaries, not claims that Operativity Theory discovered the underlying reachability results.

## Boundary conclusion
The previous open question "where does APS cross from decidable to undecidable?" is sharpened as follows:

For the singleton-emergent-verifier fragment, the boundary is exactly parameterized by reachability in the verifier-generator model. There is no valid universal finite-vs-infinite boundary.

## Remaining theory problem
The genuinely open extension is the multi-verifier / dynamically generated semantic-verifier case, especially when:
- the verifier vocabulary itself is unbounded or generated symbolically;
- distinguishing status is not fixed in advance;
- verifier semantics can depend on generated structure;
- APS requires quantification over an unbounded generated verifier family.

The next target is to determine whether this richer APS problem is strictly harder than generator reachability, and under which restrictions it collapses back to reachability.
