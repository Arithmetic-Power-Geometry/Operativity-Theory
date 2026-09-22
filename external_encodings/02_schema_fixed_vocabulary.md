# Paired External Encoding 02 — Versioned Schema Compatibility

## Source role
Fixed-vocabulary control. This case tests T17's conservative-embedding prediction rather than seeking a TCOP advantage.

## Conventional obligation
For schemas s (old) and s' (new), backward compatibility is abstractly:

```
forall payload p:
    valid_s(p) -> valid_s'(p)
```

Forward and full compatibility reverse or combine the relevant reader/writer direction.

## TCOP embedding
Take:
- x := old schema behavior;
- x_a := new schema behavior;
- transformation a := schema evolution;
- V0 := payload/reader-writer compatibility tests;
- V_a^infinity := V0.

Because the observation/test vocabulary is fixed:

```
APS = PC = conventional compatibility.
```

## Result
No strictness should appear. TCOP is a conservative re-expression of the ordinary compatibility obligation.

| Metric | Conventional schema relation | TCOP | Verdict |
|---|---|---|---|
| compatibility semantics | direct/native | embedded | conventional simpler |
| future verifier generation | unnecessary | degenerate G_a | no benefit |
| decision result | native | same | tie |
| specification burden | minimal | additional framework terms | conventional wins |

## Conclusion
This is a **negative control passed**: TCOP does not manufacture an advantage where the verifier vocabulary is fixed. It validates the intended scope of T17.

A strict TCOP case requires a real source where the transformation itself changes the reachable observation/test vocabulary.
