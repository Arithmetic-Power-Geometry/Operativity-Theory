"""Generate artifact for finite causal separator synthesis."""
import csv, json
from pathlib import Path
from src.causal_observation_synthesis import causal_separator, opentelemetry_causal_case

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    left,right,graph,obs=opentelemetry_causal_case()
    s=causal_separator(left,right,graph,"dashboard",obs)
    row={
        "status":"CAUSAL_SEPARATOR_FOUND" if s else "NO_CAUSAL_SEPARATOR",
        "node":s.node if s else "",
        "distance_to_symptom":s.distance_to_symptom if s else "",
        "left":repr(s.left_value) if s else "",
        "right":repr(s.right_value) if s else "",
        "shared_dashboard":left["dashboard"]==right["dashboard"],
    }
    with (out/"causal_observation_synthesis.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=row.keys()); w.writeheader(); w.writerow(row)
    (out/"causal_observation_synthesis_summary.json").write_text(json.dumps(row,indent=2))
    print(row)

if __name__=="__main__": main()
