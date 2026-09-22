from __future__ import annotations
import itertools, json, csv
from pathlib import Path
from .model import State, System

OUT=Path("artifacts")
V={"v1":lambda x:x[0],"v2":lambda x:x[1]}
CONFIGS=list(itertools.product((0,1), repeat=2))
SUBSETS=[frozenset(s) for r in range(3) for s in itertools.combinations(V,r)]

def main():
    OUT.mkdir(exist_ok=True)
    rows=[]
    violations=[]
    # Exhaust every pair of 2-bit configurations and every nested current/future verifier family.
    for xb,xa,current,future in itertools.product(CONFIGS,CONFIGS,SUBSETS,SUBSETS):
        if not current.issubset(future):
            continue
        states={
          "before":State("before",xb,current),
          "after":State("after",xa,current),
          "future":State("future",xa,future),
        }
        s=System(states,{"after":("future",),"future":()},V)
        pc=s.pc("before","after"); aps=s.aps("before","after")
        d=s.distinguishing("before","after")
        emergent=set(future)-set(current)
        char=(not aps)==bool(d & set(future))
        sipchar=(not (pc and not aps)) or bool(d & emergent)
        if not char or not sipchar:
            violations.append((xb,xa,sorted(current),sorted(future),pc,aps,sorted(d)))
        rows.append({
          "before":str(xb),"after":str(xa),
          "current":";".join(sorted(current)),"future":";".join(sorted(future)),
          "pc":pc,"aps":aps,"sip":pc and not aps,
          "distinguishing":";".join(sorted(d)),
          "emergent":";".join(sorted(emergent))
        })
    summary={
      "enumerated_systems":len(rows),
      "pc_true":sum(r["pc"] for r in rows),
      "aps_true":sum(r["aps"] for r in rows),
      "sip_true":sum(r["sip"] for r in rows),
      "t2_characterization_violations":len(violations),
      "pc_implies_aps_counterexamples":sum(r["pc"] and not r["aps"] for r in rows),
      "all_exact_checks_pass":len(violations)==0,
    }
    with (OUT/"exhaustive_results.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    with (OUT/"exhaustive_summary.json").open("w",encoding="utf-8") as f:
        json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))
    if violations:
        raise AssertionError(f"characterization violations: {violations[:3]}")

if __name__=="__main__":
    main()
