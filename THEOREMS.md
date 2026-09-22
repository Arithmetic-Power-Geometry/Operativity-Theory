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


## T10. Augmented-State Collapse of Semantic Expansion

Fix a transformation a and preservation pair (x,x_a). Suppose generated verifier descriptions and all information needed to determine their pair semantics can be represented effectively in an augmented transition state z, with a decidable predicate:

```
BAD(z) iff z contains/enables a verifier p with [[p]](x) != [[p]](x_a).
```

Then Generated-Verifier APS reduces to safety/reachability in the augmented transition system:

```
APS(a,omega) iff no BAD augmented state is reachable after a.
```

Therefore dynamic creation of new verifier syntax, predicates, or semantic distinctions is not by itself an irreducible Operativity phenomenon whenever it admits such an effective state representation.

## T11. Decision-Regime Transition (new frontier)

Let C(omega) denote the decision class of the APS problem induced by the verifier-generation structure at complete state omega (for example, a class with decidable reachability versus one capable of undecidable reachability).

A transformation a causes a decision-regime transition when:

```
C(omega) != C(a(omega)).
```

The strongest case for Operativity is a present-certified transformation satisfying:

```
PC(a,omega)=true,
APS-before regime decidable,
APS-after regime undecidable (or strictly harder under a fixed formal hierarchy).
```

This is not yet claimed as a novel theorem. It is the next target. The research question is whether transformation-induced changes in verification decidability/complexity yield nontrivial preservation laws beyond standard parameterized verification and dynamic-system model changes.


## T12. Decision-Regime Transition Is Not Retained as a Novel Primitive

A transformation can move a system between verification classes with different decidability or complexity. However, dynamic software update, parameterized verification, self-modifying-system verification, and related formal-methods literature already study verification under changing system models and identify restricted decidable versus general undecidable classes.

Therefore the bare condition:

```
C(omega) != C(a(omega))
```

is locked as insufficient for an independent Operativity theory.

## T13. Reflexive Certification Frontier

The next candidate is explicitly reflexive. Introduce a certification procedure k for a preservation claim P(a,omega). Executing k is itself an admissible physical/computational transformation:

```
k : omega_a -> omega_{a,k}.
```

The certification is reflexively stable only if the act of establishing the certificate does not create a reachable verifier/condition that defeats the certified claim.

A minimal form is:

```
RC(k,a,omega) := Cert_k(P(a,omega))
                  and APS(a,omega_{a,k}).
```

The key dependency is now:

```
transformation a
 -> certification action k
 -> changed verifier-generating structure
 -> validity of the certificate produced by k.
```

This is a candidate frontier only. It must be reduced against proof-carrying code, reflective logics, proof-producing verification, runtime assurance, interactive proofs, and self-referential verification before any novelty claim.


## T14. Reflexive-Certification Novelty Audit

The bare claim that certification/monitoring changes the system being certified is not retained as a novelty primitive. Runtime verification and instrumentation literature explicitly studies monitor interference, observer/probe effects, and instrumentation-induced behavioral change. Likewise, formal logic already has deep theories of self-reference, reflection, and internal provability/certification.

Therefore the following are locked as established-adjacent rather than Operativity-specific foundations:
- self-certification in the logical sense;
- certificates as first-class proof objects;
- certification procedures that consume resources;
- monitor/instrumentation back-action;
- observer/probe effects;
- self-reference alone.

The defensible Operativity nucleus remains the joint formal package:
1. present certification PC;
2. transformation-relative future verifier closure;
3. absolute preservation stability APS;
4. self-invalidating preservation SIP;
5. latent invalidator characterization;
6. verifier-partition stability;
7. reachability-transfer theorem;
8. pair-semantic quotient for generated verifiers.

These results should be presented as a unified formal framework unless a stronger irreducible theorem is subsequently established.


## T15. Relational-Safety Reduction of APS

For a fixed transformation a and complete initial state omega, APS compares the original configuration x with the transformed configuration x_a while quantifying over verifier-generation continuations. This is a relational property of the reference/transformed pair.

Construct a product/augmented transition system whose state contains:
- the fixed reference configuration x (or its required semantic representation);
- the evolving transformed complete state;
- verifier-generator state;
- any effective representation needed to evaluate currently enabled/generated verifiers on x and x_a.

Define:

```
BAD iff an enabled/generated verifier distinguishes x from x_a.
```

Whenever this product construction is effective:

```
APS(a,omega) iff BAD is unreachable.
SIP(a,omega) iff PC(a,omega) and BAD is reachable.
```

Thus APS belongs to the established pattern of relational / k-safety verification reducible by product construction or self-composition to ordinary safety verification. This rules out a general non-reducibility claim based solely on the fact that APS compares pre/post behaviors.

## T16. Consequence for theory status

No general separation theorem can claim that APS is invisible to all conventional safety/reachability representations if those representations are allowed the natural product/augmented state carrying the reference, transformed state, and verifier-generation information.

Any future irreducibility result would therefore require a precisely restricted representation class and proof that the restriction is scientifically justified rather than chosen merely to manufacture separation.


## T17. Fixed-Vocabulary Compatibility Strictness

Let a compatibility semantics depend only on a preservation pair `(x,x_a)` and a transformation-independent verifier family `V0`. TCOP conservatively embeds that semantics by taking `V_a^infinity=V0`.

If there exists a transformation-conditioned future verifier `v* in V_a^infinity minus V0` with `v*(x) != v*(x_a)`, the extension is strict: current/fixed-vocabulary compatibility may hold while APS fails.

A constructive two-transformation witness uses the same reference state, the same transformed ordinary configuration, and the same current verifier family, but different future verifier closures. The fixed-vocabulary semantics gives the same verdict to both transformations; APS distinguishes them.

**Scope restriction.** This is not an expressiveness separation from HyperLTL, temporal logic, product-state verification, or any formalism allowed to encode future observer-generation state. It is a separation from compatibility semantics whose observation/test vocabulary is fixed independently of the transformation.
