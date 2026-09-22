# Transformation-Relative Certification Pattern

## Purpose
Operativity is here treated as a specification pattern, not a replacement model checker.

## Declaration
A specification declares:
1. reference state x;
2. transformation a producing x_a;
3. present verifier family V0;
4. transformation-conditioned verifier-generation model G_a;
5. preservation relation for verifier outputs;
6. optional certification horizon.

## Obligations
```
PC  := forall v in V0: v(x) = v(x_a)
APS := forall reachable v through G_a: v(x) = v(x_a)
SIP := PC and not APS
```

## Compilation
For effective product-representable systems define:
```
BAD := exists reachable verifier v: v(x) != v(x_a)
```
Then:
```
APS <=> AG(not BAD)
SIP <=> PC and EF(BAD)
```

The pattern therefore compiles to established verification backends.

## Empirical hypothesis
The remaining hypothesis is not yet established:

> Transformation-relative preservation with evolving observability can be specified more directly and with fewer semantic encoding mistakes using the PC/APS/SIP pattern than by manually constructing equivalent product-state or hyperproperty specifications.

## Required Q1 evaluation
- external transformation/evolving-observation task corpus;
- manual conventional temporal/hyperproperty encodings;
- pattern encodings compiled to the same backend;
- specification size;
- construction time;
- encoding defects / semantic mismatches;
- verification-result agreement;
- preferably a controlled user study.

Without this evidence the pattern is a conceptual contribution, not a strong Q1 result.
