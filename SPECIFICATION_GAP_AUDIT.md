# Specification Gap Audit

## Candidate gap

The surviving candidate is not dynamic requirements, dynamic monitors, relational verification, or ordinary property-specification patterns.

It is the following conjunction:

1. a transformation a is under certification;
2. a preservation relation between x and x_a is fixed;
3. current observations certify the transformation;
4. the transformation changes the reachable observation/verifier vocabulary;
5. a newly reachable observation can distinguish x from x_a;
6. certification therefore quantifies over transformation-conditioned future observability.

We call this the **Transformation-Conditioned Observability Preservation (TCOP) pattern** as a working name.

## Closest established neighbors

- Property Specification Patterns: reusable temporal-property schemas.
- Timed/UPPAAL pattern catalogs: pattern frontends compiled to observer automata/formulae.
- Runtime verification with changing requirements: monitors/properties are adapted as requirements evolve.
- Reconfigurable runtime monitors: event triggers and monitored specifications can change.
- HyperLTL/hyperproperties: relations across multiple traces.
- Regression verification: equivalence across program versions.

## Current audit conclusion

These neighbors cover major components of TCOP. The present audit did not identify an exact standard named pattern whose defining semantics is: *the transformation being certified changes which future observations become available, while the preservation obligation itself remains fixed and ranges over that transformation-conditioned future observation set.*

This is evidence of a possible pattern gap, not proof of novelty.

## Falsification conditions

TCOP should be abandoned as a novelty claim if:
- an established pattern with equivalent semantics is found;
- it is a trivial parameterization of an existing pattern with no specification-engineering benefit;
- external examples do not repeatedly instantiate it;
- expert conventional encodings are equally direct and no empirical benefit is shown.

## Required next evidence

1. Collect independent published examples in which system evolution changes observable/event vocabulary.
2. Map each example to TCOP without changing its semantics.
3. Encode each in an established specification formalism/pattern catalog.
4. Measure whether TCOP removes recurring auxiliary modeling structure.
5. Validate translation to an established backend.
