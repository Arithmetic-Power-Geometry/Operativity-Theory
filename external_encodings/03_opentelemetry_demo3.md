# Paired External Encoding 03 — OpenTelemetry Demo 3.0

## External observation
The OpenTelemetry Demo 3.0 migration changed services and telemetry attribute names. Existing custom dashboards may therefore fail even when the underlying application behavior of interest remains otherwise plausible.

## Competing explanations for a broken dashboard

H1 — **System-behavior failure**:
The monitored service behavior itself changed/fails, so the dashboard is correctly reporting absence/degradation.

H2 — **Observability-contract failure**:
The service remains behaviorally acceptable, but the telemetry schema/attribute/service-name vocabulary changed, so the old dashboard query no longer denotes the intended signal.

These explanations can produce the same coarse observation:

```
dashboard panel has missing/empty/changed data
```

Therefore dashboard output alone does not separate H1 and H2.

## Minimal separating measurement

Measure the raw post-upgrade telemetry at the collector/export boundary and compare:

1. resource/service identity;
2. metric/span/log signal presence;
3. attribute-key set;
4. old-to-new semantic attribute mapping;
5. signal value independently of the legacy dashboard query.

Define:

```
M_sep = (signal_present, service_identity, attribute_keys, semantic_mapping)
```

Interpretation:

- signal absent at collector -> supports H1 or upstream instrumentation failure;
- signal present with expected semantics but renamed service/attributes -> supports H2;
- signal present but value/behavior itself changed -> supports H1;
- both signal behavior and vocabulary changed -> neither simple explanation alone is sufficient.

The key discriminating observation is therefore not another screenshot/dashboard reading. It is **raw telemetry plus the semantic mapping between pre- and post-upgrade observation vocabularies**.

## Conventional encoding

A conventional migration/monitoring specification can explicitly introduce:
- old attribute vocabulary A0;
- new vocabulary A1;
- mapping mu: A0 -> A1;
- dashboard query Q0;
- migrated query Q1;
- equivalence/preservation obligation over mapped signals.

```
forall intended signal s:
    semantics(Q0, T0, s) == semantics(Q1, T1, mu(s))
```

This is direct and expressive.

## TCOP encoding

- x := pre-upgrade telemetry semantics;
- a := Demo 3.0 upgrade;
- x_a := post-upgrade telemetry semantics;
- V0 := legacy dashboard/query observations;
- G_a := upgrade-conditioned availability of new service/attribute observations;
- V_a^infinity := legacy plus migrated/raw-semantic observations;
- preservation := intended monitored semantic signal is unchanged under vocabulary mapping.

PC can hold under coarse/legacy observations while later/raw mapped observations reveal whether the change is behavioral or observational.

## Evaluation

| Item | Conventional migration spec | TCOP |
|---|---|---|
| old/new vocabulary | explicit | V0 / V_a^infinity |
| mapping | explicit mu | still required |
| query semantics | explicit | verifier semantics |
| observer evolution | explicit migration model | first-class G_a |
| backend power | established | same after compilation |
| separating measurement | raw telemetry + mapping | same |
| demonstrated advantage | strong/direct | not yet demonstrated |

## Result

OpenTelemetry is a strong real **EV benchmark**, but the paired encoding does not yet demonstrate a TCOP advantage. The conventional migration formulation is already natural.

The scientific measurement result is valuable independently:

> To distinguish system failure from observability-contract failure after an observability upgrade, inspect raw post-upgrade telemetry and the semantic old-to-new vocabulary mapping rather than relying on the derived dashboard output.

This is an external diagnostic result, not a claim of a new measurement theory.
