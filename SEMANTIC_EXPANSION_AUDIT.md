# Semantic Expansion Reduction Audit

## Result

Semantic expansion is not retained as an independent primitive.

For a fixed preservation pair (x,x_a), if the verifier generator, generated verifier representation, and pair semantics can be included effectively in an augmented state, define BAD as the augmented states that contain or enable a verifier distinguishing x from x_a.

Then:

```
APS iff BAD is unreachable.
```

This includes cases where new verifier syntax or new predicates are generated during execution.

## Why this matters

Formal verification already uses state/abstraction refinement in which new predicates are discovered and incorporated into the verification representation. Therefore "new distinctions appear later" is not sufficient for an independent theory.

## Locked elimination

The following are no longer novelty targets:

- generated verifier syntax;
- predicate discovery;
- semantic expansion by itself;
- pair-semantic quotient growth by itself;
- undecidability inherited solely from reachability or synthesis.

## New frontier: decision-regime transitions

The remaining stronger possibility is that the preservation transformation changes the formal decision regime governing its future certification.

Write C(omega) for a formally specified decision class associated with the verifier-generation structure.

Study transformations:

```
a : omega -> omega_a
```

for which:

```
C(omega) != C(omega_a).
```

Especially:

```
PC(a,omega)=true
```

while a moves the future certification problem from a decidable generator class into an undecidable one, or into a strictly harder class in a chosen hierarchy.

This is only a candidate frontier. It must next be reduced against dynamic verification, parameterized verification, self-modifying systems, and complexity-changing transformations before being treated as Operativity-specific.
