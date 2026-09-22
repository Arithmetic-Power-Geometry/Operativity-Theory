# External Recurrence Audit

## Strict inclusion rule

A source counts as a full TCOP recurrence only if it documents:
A. a transformation/upgrade;
B. the transformation enables or changes an observation/verifier capability;
C. that observation is used to expose a preservation/compatibility distinction not captured by the earlier observation regime.

Partial A+B examples are recorded but do not count as full TCOP recurrences.

## Findings

### Runtime verification with changing requirements
Status: NEIGHBOR, not TCOP.
The requirement/property itself changes and monitors are adapted. This overlaps dynamic verification but differs from a fixed preservation obligation quantified over a transformation-conditioned future observation vocabulary.

### Dynamic instrumentation
Status: A+B supported; C not established generically.
Runtime probes can add capture of variables, arguments, return values, stack traces, and other state without redeployment. This demonstrates that observation vocabulary can be expanded dynamically. It does not by itself establish retrospective invalidation of a fixed preservation claim.

### Schema evolution / new fields
Status: A+B supported; C only compatibility-adjacent.
Schema evolution adds fields/columns and changes what downstream consumers can query. Compatibility engineering explicitly reasons about old/new readers and data. This is a strong neighboring domain but not automatically the exact TCOP semantics.

### Automotive system/sensor upgrade compatibility
Status: CLOSE RECURRENCE.
A documented compatibility architecture considers replacement/addition of sensors, changed output/timing parameters, and detection of incompatibility created by the update. This exhibits the dependency shape transformation -> changed observable/performance information -> compatibility distinction.

## Conclusion

The external audit does not support claiming discovery of the underlying phenomenon. Dynamic monitoring, schema compatibility, and upgrade compatibility already contain close operational instances.

The defensible claim is narrower:

> TCOP is a candidate cross-domain formal specification pattern that factors a recurring transformation-conditioned-observability compatibility structure into PC/APS/SIP obligations and compiles it to established verification backends.

This remains unproven as a useful new specification pattern until multiple independent full recurrences and expert baseline encodings are assembled.

## Q1 consequence

External recurrence evidence strengthens motivation but weakens any foundational novelty claim. Q1 viability now depends on formal pattern novelty plus empirical specification-engineering benefit.
