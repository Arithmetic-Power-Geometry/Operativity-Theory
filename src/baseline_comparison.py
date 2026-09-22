from __future__ import annotations
import json,time
from collections import deque
from pathlib import Path
from .realistic_scenarios import api_migration,authorization_upgrade,instrumentation_upgrade,stable_control

OUT=Path("artifacts")

def conventional_product_reachability(s,before,after):
    # Independent baseline formulation: fixed reference config plus reachable
    # transformed complete states; unsafe if any available verifier distinguishes.
    ref=s.states[before].x
    target=s.states[after].x
    q=deque([(after,0)])
    seen={after}
    explored=0
    while q:
        name,d=q.popleft(); explored+=1
        st=s.states[name]
        for v in st.available:
            if s.verifiers[v](ref)!=s.verifiers[v](target):
                return False,d,v,explored
        for nxt in s.transitions.get(name,()):
            if nxt not in seen:
                seen.add(nxt); q.append((nxt,d+1))
    return True,None,None,explored

def run_one(name,builder):
    s,b,a=builder()
    t=time.perf_counter(); aps=s.aps(b,a); ta=time.perf_counter()-t
    t=time.perf_counter(); safe,depth,witness,explored=conventional_product_reachability(s,b,a); tb=time.perf_counter()-t
    il=s.invalidation_latency(b,a)
    return {"scenario":name,"aps_safe":aps,"baseline_safe":safe,
            "verdict_agreement":aps==safe,
            "aps_latency":None if il==float("inf") else il,
            "baseline_witness_depth":depth,"baseline_witness":witness,
            "baseline_explored_states":explored,
            "aps_seconds":ta,"baseline_seconds":tb}

def main():
    OUT.mkdir(exist_ok=True)
    builders=[("api_migration",api_migration),("authorization_upgrade",authorization_upgrade),
              ("instrumentation_upgrade",instrumentation_upgrade),("stable_control",stable_control)]
    rows=[run_one(*z) for z in builders]
    summary={"cases":len(rows),"verdict_agreements":sum(r["verdict_agreement"] for r in rows),
             "all_verdicts_agree":all(r["verdict_agreement"] for r in rows),
             "latent_cases":sum(not r["aps_safe"] for r in rows)}
    (OUT/"baseline_comparison.json").write_text(json.dumps({"summary":summary,"cases":rows},indent=2),encoding="utf-8")
    print(json.dumps({"summary":summary,"cases":rows},indent=2))

if __name__=="__main__": main()
