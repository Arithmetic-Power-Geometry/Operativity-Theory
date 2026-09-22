# External Evaluation Protocol (Frozen)

## Objective
Evaluate TCOP as a specification-engineering pattern, not as a new verification algorithm.

## Inclusion
An external case must come from a published paper, public benchmark, or production compatibility specification and must contain:
1. an old/new transformation or evolution step;
2. a preservation/compatibility obligation;
3. an observation, client, event, schema, instrumentation, or monitor vocabulary relevant to checking that obligation.

Cases are tagged:
- **FV**: fixed vocabulary; ordinary compatibility is sufficient.
- **EV**: explicitly evolving vocabulary/environment already modeled by the source formalism.
- **TC**: transformation-conditioned observation vocabulary is necessary to state the intended preservation obligation naturally.

## Predeclared comparison
For each accepted case create:
A. a conventional expert-style encoding faithful to the source;
B. a TCOP encoding;
C. translation of TCOP to the same verification semantics/backend where feasible.

Record:
- semantic obligations;
- specification atoms/AST nodes;
- auxiliary state/variables;
- explicit cross-version mappings;
- observer/event-generation declarations;
- result agreement;
- unsupported assumptions.

## No cherry-picking
Negative cases remain in the corpus. FV and EV cases are not discarded merely because TCOP has no advantage.

## Success criterion
A Q1 methods claim requires more than shorter syntax. It requires repeated external TC cases plus a reproducible advantage in specification structure, correctness, authoring effort, or errors against credible conventional encodings.

## Failure criterion
If most external cases are FV/EV or conventional encodings express TC cases equally directly, TCOP is retained only as a focused conceptual/formal pattern.
