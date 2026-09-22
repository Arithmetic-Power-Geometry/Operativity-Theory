# Compatibility Embedding and Strictness Audit

## 1. Ordinary compatibility as a fixed-verifier special case

Let an established compatibility relation be represented by a family W of compatibility tests/verifiers. For example, schema backward compatibility can be represented by tests indexed by payloads p:

```
w_p(s,s') = 1 iff sigma_s(p)=1 implies sigma_s'(p)=1.
```

If the verifier family is fixed under the transformation,

```
V_a^infinity = V0 = W,
```

then APS adds no semantic strength beyond the chosen ordinary compatibility relation.

Hence fixed-vocabulary compatibility embeds into TCOP/APS.

## 2. Candidate strictness condition

Strictness can arise only when:

```
V0 is a proper subset of V_a^infinity
```

and at least one newly reachable verifier distinguishes the preservation pair.

Equivalently:

```
PC(a,x) = true
and
D(a,x) intersect (V_a^infinity minus V0) is nonempty.
```

This is exactly SIP.

## 3. Strictness witness

Consider two transformations a and b with the same reference state x and transformed ordinary state x':

```
a(x) = b(x) = x'.
```

Both have the same current verifier family V0 and therefore the same ordinary fixed-vocabulary compatibility verdict.

Let their transformation-conditioned futures differ:

```
V_a^infinity = V0
V_b^infinity = V0 union {v*}
```

with

```
v*(x) != v*(x').
```

Then:

```
PC(a,x) = PC(b,x) = true
APS(a,x) = true
APS(b,x) = false.
```

Therefore any compatibility formalism whose semantics depends only on the fixed pair (x,x') and fixed test family V0 cannot distinguish a and b, while TCOP can.

## 4. What this does and does not prove

This proves strictness only relative to **fixed-vocabulary compatibility relations**.

It does NOT prove that TCOP is strictly more expressive than:
- arbitrary temporal logic;
- HyperLTL;
- product-state model checking;
- dynamic software-update logics;
- compatibility frameworks that explicitly include future environment/observer evolution.

Those richer formalisms can encode the verifier-generation state.

## 5. Defensible theorem

**Fixed-Vocabulary Compatibility Strictness Theorem.**
For any compatibility semantics determined solely by a preservation pair and a transformation-independent verifier family V0, TCOP conservatively extends that semantics. If a transformation can make reachable a verifier outside V0 that distinguishes the pair, the extension is strict.

The proof is constructive by the a/b witness above.

## 6. Q1 significance

This is a real mathematical separation, but its comparison class is intentionally restricted and natural: conventional compatibility notions with a fixed observation/test vocabulary.

Its publication value depends on showing that this restriction actually occurs in important compatibility practice and that transformation-conditioned observer evolution is otherwise awkward to specify.
