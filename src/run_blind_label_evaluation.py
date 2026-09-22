"""Generate blind-source diagnostic evaluation artifacts."""
import csv, json
from pathlib import Path
from src.blind_label_evaluation import evaluate_blind

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows,summary=evaluate_blind()
    with (out/"blind_label_evaluation.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (out/"blind_label_evaluation_summary.json").write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
