# Decision-Regime Audit

## Eliminated claim

A preservation transformation changing the decidability or complexity class of future verification is not, by itself, an independent novelty target.

Nearby established areas include:
- dynamic software update correctness;
- parameterized verification with decidable and undecidable subclasses;
- self-modifying system model checking;
- verification of systems whose transition structure changes.

Therefore decision-regime transition is retained only as a possible phenomenon/example, not as the foundation of Operativity Theory.

## New candidate frontier

Certification must be treated as an action inside the system.

Let a be the transformation whose preservation is being certified and k the certification procedure. If executing k changes the verifier-generating structure, then the certificate may alter the future conditions under which its own claim is judged.

Dependency:

```
a
 -> certification action k
 -> changed certification/verifier environment
 -> future validity of Cert_k(a)
```

This reflexive form is the next adversarial target. No novelty claim is made until it survives comparison with reflective verification, proof-carrying systems, proof-producing verification, runtime assurance, and self-reference in logic.
