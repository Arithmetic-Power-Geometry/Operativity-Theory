"""Blind-source diagnostic evaluation.

Ground-truth relevance labels are frozen in a provenance file derived from
external documentation, separate from algorithm code and baseline logic.
"""
import json
from pathlib import Path
from collections import defaultdict
from src.causal_baseline_comparison import evaluate_baselines

PROVENANCE_PATH=Path("external_blind_labels.json")

def load_blind_labels():
    return json.loads(PROVENANCE_PATH.read_text())

def evaluate_blind():
    labels=load_blind_labels()
    rows=evaluate_baselines()
    scored=[]
    for r in rows:
        target=set(labels[r.case]["relevant_nodes"])
        scored.append({
            "case":r.case,
            "method":r.method,
            "node":r.node,
            "blind_relevant": bool(r.node in target if r.node else False),
            "source":labels[r.case]["source"],
        })
    summary=defaultdict(lambda:{"n":0,"relevant":0})
    for row in scored:
        s=summary[row["method"]]
        s["n"]+=1
        s["relevant"]+=int(row["blind_relevant"])
    summary={k:{**v,"accuracy":v["relevant"]/v["n"]} for k,v in summary.items()}
    return scored,summary
