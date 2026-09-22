from __future__ import annotations
import json, random, time
from pathlib import Path
from collections import deque
from .model import State, System

OUT=Path("artifacts")

def make_case(n, latent, seed):
    rng=random.Random(seed)
    # Two-bit preserved pair: v1 cannot see the changed second bit.
    states={"s0":State("s0",(0,0),frozenset({"v1"})),
            "s1":State("s1",(0,1),frozenset({"v1"}))}
    trans={}
    prev="s1"
    reveal=rng.randint(1,max(1,n-1)) if latent else None
    for i in range(1,n):
        name=f"q{i}"
        avail=frozenset({"v1","v2"}) if latent and i>=reveal else frozenset({"v1"})
        states[name]=State(name,(0,1),avail)
        trans[prev]=(name,)
        prev=name
    trans[prev]=()
    ver={"v1":lambda x:x[0],"v2":lambda x:x[1]}
    return System(states,trans,ver),"s0","s1",reveal

def main():
    OUT.mkdir(exist_ok=True)
    rows=[]
    for n in (10,100,1000,5000):
      for latent in (False,True):
       for rep in range(5):
        s,b,a,reveal=make_case(n,latent,10000*n+100*latent+rep)
        t=time.perf_counter(); pc=s.pc(b,a); tpc=time.perf_counter()-t
        t=time.perf_counter(); aps=s.aps(b,a); taps=time.perf_counter()-t
        il=s.invalidation_latency(b,a)
        rows.append({"states":n,"latent":latent,"rep":rep,"pc":pc,"aps":aps,
                     "pc_seconds":tpc,"aps_seconds":taps,
                     "invalidation_latency":None if il==float("inf") else il})
    summary={
      "runs":len(rows),
      "latent_cases":sum(r["latent"] for r in rows),
      "pc_accepts_latent_cases":sum(r["latent"] and r["pc"] for r in rows),
      "aps_detects_latent_cases":sum(r["latent"] and not r["aps"] for r in rows),
      "false_latent_flags_on_stable":sum((not r["latent"]) and (not r["aps"]) for r in rows),
      "max_states":max(r["states"] for r in rows),
    }
    (OUT/"scalability_cases.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    (OUT/"scalability_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
