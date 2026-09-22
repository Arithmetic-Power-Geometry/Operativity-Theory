# APS Decidability Boundary

## Central reduction

In the singleton-emergent-verifier fragment, let v* be unavailable initially, let it distinguish the pre/post configurations, and let F be exactly the generator configurations in which v* is available.

Then:

```
APS  <=>  F is unreachable
SIP  <=>  F is reachable
```

So APS is not assigned a separate arbitrary complexity boundary. Its boundary transfers from reachability in the chosen verifier-generator model.

## Consequences

| Generator model | Reachability | Singleton APS |
|---|---|---|
| finite-state | decidable | decidable |
| one-stack pushdown | decidable | decidable |
| Petri net / VASS | decidable | decidable |
| two-stack pushdown | undecidable in general | undecidable in general |
| two-counter Minsky | undecidable | undecidable |

## Interpretation

Unbounded state does not by itself destroy certifiability. Petri nets/VASS provide the key counterexample: their state spaces can be infinite while reachability remains decidable.

Conversely, very small machine descriptions can generate undecidable APS once their reachability problem is undecidable.

## What remains open

The next nontrivial problem is not singleton APS. It is APS with dynamically generated verifier identities/semantics, where the set of possible latent invalidators is not fixed in advance.
