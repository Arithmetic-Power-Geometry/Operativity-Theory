"""Generate artifacts for independent external causal-transfer cases."""
import csv, json
from pathlib import Path
from src.external_causal_cases import run_external_cases

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    cases=run_external_cases()
    rows=[]
    for name,v in cases.items():
        rows.append({"case":name, **v})
    with (out/"external_causal_cases.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (out/"external_causal_cases_summary.json").write_text(json.dumps(cases,indent=2))
    print(json.dumps(cases,indent=2))

if __name__=="__main__": main()
