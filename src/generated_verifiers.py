from __future__ import annotations
import itertools, json
from pathlib import Path

OUT=Path("artifacts")

# Boolean verifier expressions over two bits.
# Expressions are represented as nested tuples.
def eval_expr(e,x):
    op=e[0]
    if op=="x": return x[e[1]]
    if op=="0": return 0
    if op=="1": return 1
    if op=="not": return 1-eval_expr(e[1],x)
    a=eval_expr(e[1],x); b=eval_expr(e[2],x)
    if op=="and": return a & b
    if op=="or": return a | b
    if op=="xor": return a ^ b
    raise ValueError(op)

def expressions(depth):
    base={("x",0),("x",1),("0",),("1",)}
    allset=set(base); frontier=set(base)
    for _ in range(depth):
        new={("not",e) for e in frontier}
        pool=list(allset)
        for op in ("and","or","xor"):
            for a,b in itertools.product(pool,pool):
                new.add((op,a,b))
        new-=allset
        allset|=new; frontier=new
    return allset

def main():
    OUT.mkdir(exist_ok=True)
    exprs=expressions(2)
    configs=list(itertools.product((0,1),repeat=2))
    rows=[]
    violations=0
    for x,xa in itertools.product(configs,configs):
        quotient={}
        bad_syntax=[]
        for e in exprs:
            sig=(eval_expr(e,x),eval_expr(e,xa))
            quotient.setdefault(sig,0)
            quotient[sig]+=1
            if sig[0]!=sig[1]:
                bad_syntax.append(e)
        full_aps=(len(bad_syntax)==0)
        quotient_aps=all(a==b for a,b in quotient)
        if full_aps!=quotient_aps:
            violations+=1
        rows.append({
          "x":x,"xa":xa,"syntactic_verifiers":len(exprs),
          "pair_semantic_classes":len(quotient),
          "full_aps":full_aps,"quotient_aps":quotient_aps,
          "bad_semantic_classes":sum(a!=b for a,b in quotient),
        })
    summary={
      "expression_depth":2,
      "syntactic_verifiers":len(exprs),
      "preservation_pairs":len(rows),
      "quotient_equivalence_violations":violations,
      "all_pair_semantic_checks_pass":violations==0,
      "max_pair_semantic_classes":max(r["pair_semantic_classes"] for r in rows),
      "max_syntax_to_semantics_compression":max(r["syntactic_verifiers"]/r["pair_semantic_classes"] for r in rows),
    }
    (OUT/"generated_verifier_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    (OUT/"generated_verifier_cases.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    if violations: raise AssertionError("pair-semantic quotient changed APS")

if __name__=="__main__":
    main()
