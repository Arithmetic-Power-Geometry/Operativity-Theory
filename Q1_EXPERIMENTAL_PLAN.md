# Q1 Experimental Plan

## Research questions

**RQ1 — Latent invalidation.** Can transformations that preserve all currently available observations later become distinguishable when the transformed system enables additional observations?

**RQ2 — Diagnostic value.** Beyond an unsafe/safe verdict, does APS identify the newly enabled distinguishing verifier and minimum invalidation latency in a useful way?

**RQ3 — Cost.** What state-space and runtime overhead is introduced by the APS product/closure analysis relative to present-only checking and a conventional product-state reachability implementation?

**RQ4 — Complementarity.** On established versioned verification benchmarks, does the transformation-relative verifier model expose failures or explanations not naturally produced by regression/difference verification baselines?

## Scenario families

1. API migration: same public response, later diagnostic/provenance observation.
2. Authorization upgrade: same immediate authorization decision, later audit of authority/delegation source.
3. Instrumentation upgrade: same functional output, later higher-resolution timing observation.
4. Stable controls with the same verifier expansion but no semantic difference.

The initial versions are controlled executable models, not empirical claims about deployed systems.

## Baselines required for a Q1 submission

1. Present-only certification (explanatory lower baseline).
2. Plain product-state reachability using the same state information.
3. Relational/regression verification where applicable.
4. A standard model-checking implementation/tool on translated benchmark instances.

## Metrics

- latent-invalid transformations detected;
- false flags on stable controls;
- shortest invalidation latency;
- witness/verifier localization;
- explored states/transitions;
- runtime and peak memory;
- translation/product-state overhead;
- result agreement with conventional reachability;
- diagnostic information beyond the conventional unsafe witness.

## Q1 falsification rule

If APS produces the same decision, essentially the same witness, and no meaningful modeling or efficiency advantage over ordinary product-state verification across realistic benchmarks, the work should not be sold as a new verification method. It should be reframed as a conceptual taxonomy/framework.

If the transformation-relative verifier abstraction provides reproducibly smaller search, earlier witnesses, or materially better diagnostic localization on realistic tasks, that can support a formal-methods contribution.
