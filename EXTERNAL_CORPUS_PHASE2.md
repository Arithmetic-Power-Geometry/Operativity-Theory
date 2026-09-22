# External Evaluation Phase 2 — Evolving Observability

## Purpose
Expand the frozen external corpus with real systems in which upgrades alter telemetry/audit/observation vocabularies.

## OpenTelemetry
The official stability specification permits new signals to be introduced while stable APIs retain compatibility guarantees. The OpenTelemetry Demo 3.0 upgrade also changed services and attribute names, breaking existing custom dashboards.

Classification: **EV**.

Why not full TC: the sources establish upgrade-conditioned evolution of observability and compatibility consequences, but do not establish that a newly created signal subsequently invalidates the preservation claim of the same transformation.

## OneUptime v11
The upgrade migrates logs, traces, metrics, exceptions, profiles, monitor logs and audit logs to new tables, renames entity columns, and migrates dashboards/monitors/alerts.

Classification: **EV**.

Why useful: it provides a concrete paired-encoding target where observable vocabulary and dependent monitoring artifacts evolve together.

## Confluence Advanced Audit Log
An upgrade introduced Advanced Audit Log and a migration task converting legacy audit records into the new format.

Classification: **EV**.

Why useful: an upgrade changes audit/observation capability and historical representation, giving a second independent observability-evolution domain.

## Phase-2 conclusion
External evidence now clearly supports the practical recurrence of **evolving observation vocabularies under system upgrades**.

It still does not establish the stricter full-TC condition that the transformation under certification creates a new verifier which then exposes failure of that same transformation's fixed preservation obligation.

Therefore these cases strengthen motivation and benchmark realism, not the strong TCOP novelty claim.
