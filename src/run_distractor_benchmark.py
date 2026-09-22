"""Generate distractor-robustness benchmark artifacts."""
import csv, json
from pathlib import Path
from collections import defaultdict
from src.distractor_benchmark import evaluate_hard

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows=evaluate_hard()
    data=[{
        "case":r.case,"distractors":r.distractors,"method":r.method,
        "node":r.node,"relevant":r.relevant
    } for r in rows]
    with (out/"distractor_benchmark.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=data[0].keys()); w.writeheader(); w.writerows(data)

    agg=defaultdict(lambda:{"n":0,"correct":0})
    for r in rows:
        k=f"{r.method}|d={r.distractors}"
        agg[k]["n"]+=1; agg[k]["correct"]+=int(r.relevant)
    summary={k:{**v,"accuracy":v["correct"]/v["n"]} for k,v in agg.items()}
    (out/"distractor_benchmark_summary.json").write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
