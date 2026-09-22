# External Corpus — Phase 1

The corpus deliberately begins with strong neighboring and negative-control cases rather than examples selected to favor TCOP.

## Seed cases

- **DSU / Redis:** client-oriented specifications already express continuity across updates, post-update behavior, and conformable interface changes. This is a hard negative/neighbor.
- **iMOP:** evolution-aware runtime verification explicitly reuses instrumentation across revisions and re-monitors specifications. This is an EV case, not evidence of TCOP novelty.
- **Apache Pulsar schema compatibility:** backward/forward/full compatibility provides a concrete fixed-vocabulary compatibility family and is useful for validating T17's embedding.
- **EvoBench:** a public NoSQL schema-evolution benchmark suitable for case-level inspection; it is not labeled TC until the strict dependency is demonstrated.

The next phase is to expand the corpus and perform paired encodings. Negative results remain part of the published artifact.
