"""Generate causal-vs-baseline comparison artifacts."""
import csv, json
from pathlib import Path
from collections import defaultdict
from src.causal_baseline_comparison import evaluate_baselines

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows=evaluate_baselines()
    data=[{
        "case":r.case,
        "method":r.method,
        "node":r.node,
        "diagnostic_relevant":r.diagnostic_relevant,
    } for r in rows]
    with (out/"causal_baseline_comparison.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=data[0].keys()); w.writeheader(); w.writerows(data)
    summary=defaultdict(lambda:{"n":0,"relevant":0})
    for r in rows:
        summary[r.method]["n"]+=1
        summary[r.method]["relevant"]+=int(r.diagnostic_relevant)
    summary={k:{**v,"accuracy":v["relevant"]/v["n"]} for k,v in summary.items()}
    (out/"causal_baseline_comparison_summary.json").write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
