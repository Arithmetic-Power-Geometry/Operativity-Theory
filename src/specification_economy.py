from __future__ import annotations
import json
from pathlib import Path

OUT=Path("artifacts")

TASKS=[
 ("api_provenance",2,1),("auth_delegation",2,1),("instrument_timing",2,1),
 ("schema_constraint",3,1),("sensor_upgrade",3,1),("audit_lineage",3,1),
 ("feature_subgroup",3,1),("protocol_observer",3,1),("logging_context",3,1),
 ("cache_consistency",3,1),("migration_history",3,1),("replica_metadata",3,1)
]

# Counts are syntactic obligations in a transparent canonical encoding,
# not human-time measurements. They make no claim of usability superiority.
def manual_product_atoms(n_present,n_future):
    # reference + transformed values, availability guards, equality clauses
    return 2*(n_present+n_future)+n_future+(n_present+n_future)

def operativity_atoms(n_present,n_future):
    # verifier declarations + generator availability + one preservation declaration
    return (n_present+n_future)+n_future+1

def main():
    OUT.mkdir(exist_ok=True)
    rows=[]
    for name,p,f in TASKS:
        m=manual_product_atoms(p,f); o=operativity_atoms(p,f)
        rows.append({"task":name,"present_verifiers":p,"future_verifiers":f,
                     "manual_canonical_atoms":m,"pattern_atoms":o,
                     "syntactic_reduction":m-o,
                     "ratio":round(o/m,4)})
    summary={"tasks":len(rows),
             "manual_atoms":sum(r["manual_canonical_atoms"] for r in rows),
             "pattern_atoms":sum(r["pattern_atoms"] for r in rows)}
    summary["ratio"]=round(summary["pattern_atoms"]/summary["manual_atoms"],4)
    (OUT/"specification_economy.json").write_text(json.dumps({"summary":summary,"cases":rows},indent=2),encoding="utf-8")
    print(json.dumps({"summary":summary,"cases":rows},indent=2))

if __name__=="__main__": main()
