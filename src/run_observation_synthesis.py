"""Generate artifacts for automatic separating-observation synthesis."""
import csv, json
from pathlib import Path
from src.measurement_bridge import opentelemetry_demo_case
from src.observation_synthesis import synthesize_separator, synthesize_all_minimal_separators

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    left,right,_=opentelemetry_demo_case()
    best=synthesize_separator(left,right)
    mins=synthesize_all_minimal_separators(left,right)
    rows=[{
        "path":".".join(map(str,s.path)),
        "cost":s.cost,
        "left":repr(s.left_value),
        "right":repr(s.right_value),
    } for s in mins]
    with (out/"observation_synthesis.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["path","cost","left","right"])
        w.writeheader(); w.writerows(rows)
    (out/"observation_synthesis_summary.json").write_text(json.dumps({
        "status":"SEPARATOR_SYNTHESIZED" if best else "UNRESOLVED_IN_DECLARED_STRUCTURE",
        "best_path": list(best.path) if best else None,
        "cost": best.cost if best else None,
        "n_minimal_separators": len(mins),
        "legacy_dashboard_separates": left["dashboard"] != right["dashboard"],
    },indent=2))
    print(best)

if __name__=="__main__": main()
