# Generated-Verifier APS

## 1. Motivation

The singleton fragment fixes a latent verifier v* in advance. Its APS problem collapses exactly to reachability of the enabling condition for v*.

The richer fragment does not predeclare the future verifier. A transformation changes a verifier-generating structure, and a continuation may synthesize a verifier whose identity and semantics were not enumerated initially.

## 2. Verifier language

Let L be an effective verifier language. Every description p in L denotes, when well formed, a semantic verifier:

```
[[p]] : X -> Y_p
```

Let G_a(omega) be the transformation-conditioned generator induced after executing a at omega.

Let:

```
Lang(G_a, omega)
```

be all verifier descriptions generable along admissible continuations after a.

## 3. Generated Latent Invalidator (GLI)

A generated latent invalidator exists iff:

```
exists p in Lang(G_a, omega):
    [[p]](x) != [[p]](x_a)
```

subject to p becoming operationally realizable along the corresponding continuation.

Define:

```
GLI(a,omega) = true
```

when such a generated verifier exists.

For present-certified transformations:

```
APS(a,omega) iff not GLI(a,omega).
```

## 4. Generated-Verifier APS (GV-APS)

GV-APS asks whether:

```
for every operationally generable verifier p:
    [[p]](x) = [[p]](x_a)
```

Its complement is an existential verifier-synthesis problem:

```
exists p generated after a such that [[p]] distinguishes x and x_a.
```

## 5. Compilation criterion

Generated semantics does NOT by itself escape reachability.

If there is an effective finite or otherwise decidable abstraction A such that every generated verifier's distinguishing effect on the fixed pair (x,x_a) is represented by a finite label in A, then GV-APS collapses to reachability over the product:

```
generator-state x abstraction-of-verifier-effect
```

Thus the relevant obstruction is not generation itself. It is failure of an effective quotient for the generated verifiers' semantics on the preservation pair.

## 6. Pair-Semantic Quotient

For fixed (x,x_a), define verifier equivalence:

```
p ~_(x,x_a) q
iff
([[p]](x), [[p]](x_a)) = ([[q]](x), [[q]](x_a)).
```

Only this pair-semantic quotient matters to APS.

If the reachable quotient is effectively finite and generator transitions on quotient classes are computable, GV-APS is decidable by reachability.

## 7. Pair-Semantic Quotient Theorem

For a fixed present-certified transformation (a,omega), suppose:
1. generated verifier descriptions have decidable semantics on x and x_a;
2. the reachable quotient Lang(G_a,omega)/~_(x,x_a) has an effectively computable finite presentation;
3. reachability of quotient classes is decidable.

Then GV-APS is decidable.

Proof: mark every quotient class whose two semantic components differ as BAD. GV-APS holds exactly when no BAD class is reachable.

## 8. Collision with existing synthesis theory

The unrestricted complement of GV-APS is structurally a synthesis problem: generate some verifier satisfying the distinguishing specification.

Therefore novelty cannot be claimed for:
- synthesizing formulas/monitors/programs;
- undecidability of unrestricted synthesis;
- decidable grammar fragments;
- generated monitor semantics alone.

The Operativity-specific object is the transformation-conditioned generated verifier family used to evaluate preservation of that same transformation.

## 9. Current frontier

The next theorem target is not generic synthesis undecidability. It is to identify conditions under which two transformations with identical present state and present certification induce different pair-semantic verifier quotients, and to quantify the minimum generative power required to create a BAD quotient class.

This keeps the theory tied to self-invalidating preservation rather than relabeling program/formula synthesis.
