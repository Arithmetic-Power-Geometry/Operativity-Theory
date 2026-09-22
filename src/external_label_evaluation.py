"""Evaluate diagnostic methods against labels stored separately from the algorithms."""
import json
from pathlib import Path
from collections import defaultdict

from src.causal_baseline_comparison import evaluate_baselines

LABEL_PATH=Path("external_ground_truth_labels.json")

def load_labels():
    return json.loads(LABEL_PATH.read_text())

def evaluate_against_external_labels():
    labels=load_labels()
    rows=evaluate_baselines()
    scored=[]
    for r in rows:
        rel=set(labels[r.case]["relevant_nodes"])
        scored.append({
            "case":r.case,
            "method":r.method,
            "node":r.node,
            "relevant": bool(r.node in rel if r.node else False),
            "label_basis": labels[r.case]["basis"],
        })
    summary=defaultdict(lambda:{"n":0,"relevant":0})
    for row in scored:
        s=summary[row["method"]]
        s["n"]+=1
        s["relevant"]+=int(row["relevant"])
    summary={k:{**v,"accuracy":v["relevant"]/v["n"]} for k,v in summary.items()}
    return scored,summary
