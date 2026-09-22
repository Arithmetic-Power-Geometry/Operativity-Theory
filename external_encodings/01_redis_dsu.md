# Paired External Encoding 01 — Redis / Client-Oriented DSU

## Source role
Hard negative control. Client-oriented dynamic-software-update specifications already support relational old/new correctness, post-update behavior, backward compatibility, and conformable interface change.

## Published-style conventional obligation
Abstract the client-oriented obligation as a relation over old/new executions and an update point:

```
CO(phi, P_old, P_new, u)
```

where phi specifies the client-visible relation required across the update. Rich CO-specifications may explicitly relate old and new state and behavior.

## TCOP encoding
Map:
- reference x := relevant pre-update client-visible state/history;
- transformation a := software update;
- x_a := post-update state/history;
- V0 := client observations/tests available under the original interface;
- G_a := any update-conditioned observation/interface evolution;
- preservation relation := the client-oriented compatibility obligation.

Then:
```
PC := all V0 observations preserve the declared relation
APS := all reachable observations induced/available after a preserve it
SIP := PC and not APS
```

## Result

### Case 1 — fixed client vocabulary
If the CO-specification uses a fixed observation/client vocabulary:
```
V_a^infinity = V0
```
TCOP collapses to the fixed-vocabulary compatibility case. No semantic advantage.

### Case 2 — interface/observer evolution explicitly encoded by CO-spec
If the conventional specification explicitly relates the changed interface/client observations, the relevant future vocabulary is already represented in the conventional model. TCOP provides a different factoring but no demonstrated expressive advantage.

### Case 3 — transformation-conditioned observation generation omitted by the conventional model
TCOP can make the dependency explicit through G_a, but this is only an advantage if the source requirement genuinely needs that dependency and conventional expert modeling repeatedly requires auxiliary structure to express it.

## Paired score (current evidence)

| Metric | Conventional CO-spec | TCOP | Verdict |
|---|---|---|---|
| old/new relational behavior | native | native | tie |
| post-update properties | native | native | tie |
| interface change | supported | represented through G_a/verifiers | tie |
| transformation-conditioned observation closure | can be modeled in rich state/specification | first-class declaration | TCOP factoring only |
| decision power | strong existing verification backend | compiles to same class | no advantage |
| external empirical evidence | published DSU evaluation/cases | none yet | conventional wins |

## Conclusion
Redis/CO-spec is **not a TCOP win**. It is a hard neighbor and presently a tie/loss. TCOP's only plausible benefit is first-class factoring of transformation-conditioned observation closure, which is not yet empirically demonstrated.

This negative result is retained.
