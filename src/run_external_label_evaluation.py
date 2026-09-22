"""Generate artifacts scored against externalized labels."""
import csv, json
from pathlib import Path
from src.external_label_evaluation import evaluate_against_external_labels

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows,summary=evaluate_against_external_labels()
    with (out/"external_label_evaluation.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (out/"external_label_evaluation_summary.json").write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
