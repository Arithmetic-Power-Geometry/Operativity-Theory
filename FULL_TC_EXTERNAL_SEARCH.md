# External TC Case Search — Make-or-Break Pass

## Frozen criterion
A full TC case requires:
1. transformation a is the object being certified;
2. before a, distinguishing verifier v* is unavailable;
3. a itself makes v* reachable/available;
4. v* distinguishes reference x from transformed x_a;
5. the preservation obligation remains fixed.

## Candidate classes inspected

### Dynamic instrumentation / observability upgrades
Strong evidence exists that runtime instrumentation can add previously unavailable variable, argument, return-value, stack, or event observations. However, when instrumentation is an independently deployed observer rather than part of the transformation being certified, criterion 3 fails.

### Schema evolution
New fields can create new queryable information, but ordinary compatibility normally evaluates old/new reader-writer behavior directly. Unless the schema transformation itself enables a later verifier that exposes a fixed preservation failure, this is FV/EV rather than full TC.

### Software updates with diagnostics
Updates can add diagnostics/telemetry and therefore create new observations. But a full TC classification requires a published case where those update-created diagnostics expose a preservation distinction of the same update. Generic observability claims are insufficient.

### Sensor/system replacement
Replacement hardware can change both system behavior and available sensing/diagnostic information. Compatibility literature contains close operational examples, but current evidence is not yet strong enough to establish multiple independent published full-TC cases under the strict criterion.

## Result of make-or-break pass

No robust set of multiple independent published full-TC cases has been established under the frozen criterion.

This is a negative empirical result.

## Consequence

Do not promote TCOP as a strong-Q1 verification-method contribution on current evidence.

Retain:
- formal PC/APS/SIP framework;
- T17 scoped fixed-vocabulary strictness;
- reproducible implementation and negative controls;
- TCOP as a candidate formal specification pattern.

Recommended positioning:
**focused formal framework / specification-pattern paper**, with explicit limitations and negative results.

A future strong-Q1 claim should be reopened only if independent real systems satisfying the frozen full-TC criterion are documented or if a controlled specification study demonstrates substantial practical benefit.
