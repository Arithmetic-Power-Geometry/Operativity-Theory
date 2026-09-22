# Non-Reducibility Audit

## Question

Can two systems be identical under every conventional reachability/safety representation yet differ in APS?

## Result

Not under the natural effective product-state representation.

APS is relational: it compares a reference configuration with a transformed configuration while following future verifier-generation behavior.

A product/augmented system can carry both sides plus verifier-generator state. A BAD state is reached exactly when an enabled/generated verifier distinguishes the pair.

Therefore:

```
APS <=> BAD unreachable
SIP <=> PC and BAD reachable
```

This matches the established formal-methods pattern in which relational / 2-safety properties are reduced to ordinary safety through self-composition or product programs.

## Locked conclusion

The project will not claim that APS is fundamentally beyond conventional reachability or safety verification.

A separation theorem would only be meaningful relative to a justified restricted representation class.

## Research consequence

Operativity Theory should now be developed as a focused transformation-relative certification framework and algorithmic method, not as a demonstrated new top-level mathematical branch.

The next high-value route is empirical/formal-methods:
1. define a concrete APS analysis algorithm;
2. identify present-only certification baselines;
3. construct realistic systems where those baselines accept transformations that APS flags as latently invalidatable;
4. measure detection, cost, state-space overhead, and scalability;
5. compare product-state APS against established runtime/model-checking techniques.
