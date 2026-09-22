"""Run the certification-to-measurement bridge example."""
import csv, json
from pathlib import Path
from src.measurement_bridge import cheapest_separator, opentelemetry_demo_case

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    left,right,ms=opentelemetry_demo_case()
    rows=[]
    for m in sorted(ms,key=lambda z:(z.cost,z.name)):
        lv,rv=m.observe(left),m.observe(right)
        rows.append({"measurement":m.name,"cost":m.cost,"left":repr(lv),"right":repr(rv),"separates":lv!=rv})
    result=cheapest_separator(left,right,ms)
    with (out/"measurement_bridge.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (out/"measurement_bridge_summary.json").write_text(json.dumps({
        "status":result.status,"measurement":result.measurement,"cost":result.cost,
        "coarse_observation_separates":rows[0]["separates"]
    },indent=2))
    print(result)

if __name__=="__main__": main()
