"""Compare causal separator synthesis against simple diagnostic baselines."""
import random
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Sequence

from src.causal_observation_synthesis import causal_separator, opentelemetry_causal_case
from src.external_causal_cases import oneuptime_case, confluence_audit_case

@dataclass(frozen=True)
class BaselineResult:
    case: str
    method: str
    node: str | None
    diagnostic_relevant: bool

def nearest_differing_field(left: Mapping[str,Any], right: Mapping[str,Any], observable: Iterable[str]):
    for k in sorted(set(observable)):
        if k in left and k in right and left[k] != right[k]:
            return k
    return None

def cheapest_differing_field(left: Mapping[str,Any], right: Mapping[str,Any], observable: Iterable[str], costs: Mapping[str,float]):
    cands=[k for k in observable if k in left and k in right and left[k] != right[k]]
    if not cands:
        return None
    return sorted(cands,key=lambda k:(costs.get(k,1.0),k))[0]

def random_differing_field(left: Mapping[str,Any], right: Mapping[str,Any], observable: Iterable[str], seed:int=0):
    cands=sorted(k for k in observable if k in left and k in right and left[k] != right[k])
    if not cands:
        return None
    return random.Random(seed).choice(cands)

def case_bundle():
    oleft,oright,ograph,oobs=opentelemetry_causal_case()
    one_l,one_r,one_g,one_o,one_sym=oneuptime_case()
    con_l,con_r,con_g,con_o,con_sym=confluence_audit_case()
    return {
        "opentelemetry": {
            "left":oleft,"right":oright,"graph":ograph,"obs":oobs,"symptom":"dashboard",
            "relevant":{"raw_signal","service_identity","attribute_mapping"},
            "costs":{"raw_signal":1.0,"service_identity":1.2,"attribute_mapping":2.0,"query_result":0.5,"dashboard":0.0}
        },
        "oneuptime_v11": {
            "left":one_l,"right":one_r,"graph":one_g,"obs":one_o,"symptom":one_sym,
            "relevant":{"migrated_query","table_schema"},
            "costs":{"telemetry_semantics":0.5,"table_schema":1.0,"migrated_query":1.5,"monitor_result":0.0}
        },
        "confluence_audit": {
            "left":con_l,"right":con_r,"graph":con_g,"obs":con_o,"symptom":con_sym,
            "relevant":{"migration_state","audit_format"},
            "costs":{"event_semantics":0.5,"audit_format":1.0,"migration_state":1.5,"audit_view":0.0}
        },
    }

def evaluate_baselines():
    rows=[]
    for case,d in case_bundle().items():
        left,right,obs=d["left"],d["right"],d["obs"]
        outputs={
            "nearest_differing_field": nearest_differing_field(left,right,obs),
            "cheapest_differing_field": cheapest_differing_field(left,right,obs,d["costs"]),
            "random_differing_field": random_differing_field(left,right,obs,seed=7),
        }
        cs=causal_separator(left,right,d["graph"],d["symptom"],obs)
        outputs["causal_nearest_upstream"]=cs.node if cs else None
        for method,node in outputs.items():
            rows.append(BaselineResult(case,method,node,node in d["relevant"] if node else False))
    return rows
