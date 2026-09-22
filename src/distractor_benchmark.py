"""Distractor-rich diagnostic benchmark.

Adds observable version metadata that differs across upgrades but is not on the
causal path to the shared symptom. This tests whether causal ranking rejects
non-diagnostic differences.
"""
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping
from src.causal_observation_synthesis import causal_separator
from src.causal_baseline_comparison import nearest_differing_field, cheapest_differing_field, random_differing_field, case_bundle

@dataclass(frozen=True)
class HardResult:
    case: str
    distractors: int
    method: str
    node: str | None
    relevant: bool

def _augment(case: dict, d: int):
    left=dict(case["left"]); right=dict(case["right"])
    obs=set(case["obs"]); graph={k:list(v) for k,v in case["graph"].items()}
    costs=dict(case["costs"])
    # Version/build metadata differs but has no directed path to the symptom.
    for i in range(d):
        k=f"meta_{i:03d}"
        left[k]=f"old_{i}"
        right[k]=f"new_{i}"
        obs.add(k)
        costs[k]=0.01 + i*0.001
        graph.setdefault(k, [])
    return left,right,graph,obs,costs

def evaluate_hard(distractor_levels=(0,5,10,25,50)):
    rows=[]
    for case_name,case in case_bundle().items():
        for d in distractor_levels:
            left,right,graph,obs,costs=_augment(case,d)
            outputs={
                "nearest_differing_field": nearest_differing_field(left,right,obs),
                "cheapest_differing_field": cheapest_differing_field(left,right,obs,costs),
                "random_differing_field": random_differing_field(left,right,obs,seed=7+d),
            }
            cs=causal_separator(left,right,graph,case["symptom"],obs)
            outputs["causal_nearest_upstream"]=cs.node if cs else None
            for method,node in outputs.items():
                rows.append(HardResult(
                    case_name,d,method,node,
                    bool(node in case["relevant"] if node else False)
                ))
    return rows
