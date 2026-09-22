from __future__ import annotations
import csv, json, math
from pathlib import Path
from .examples import immediate_invalid, latent_invalid, absolutely_stable, same_present_different_future

OUT = Path("artifacts")

def row(name, sys, before, after):
    future, _ = sys.future_verifiers(after)
    current = set(sys.states[before].available)
    il = sys.invalidation_latency(before, after)
    all_states = tuple(sys.states)
    return {
        "case": name,
        "before": before,
        "after": after,
        "pc": sys.pc(before, after),
        "aps": sys.aps(before, after),
        "sip": sys.sip(before, after),
        "invalidation_latency": "inf" if math.isinf(il) else int(il),
        "current_verifiers": sorted(current),
        "future_verifiers": sorted(future),
        "emergent_verifiers": sorted(future - current),
        "distinguishing_verifiers": sorted(sys.distinguishing(before, after)),
        "present_partition": sys.partition(all_states, current),
        "future_partition": sys.partition(all_states, future),
    }

def main():
    OUT.mkdir(exist_ok=True)
    rows = []
    for name, maker in [
        ("immediate_invalid", immediate_invalid),
        ("latent_invalid", latent_invalid),
        ("absolutely_stable", absolutely_stable),
    ]:
        sys, before, after = maker()
        rows.append(row(name, sys, before, after))

    sys, before, a1, a2 = same_present_different_future()
    rows.append(row("same_present_future_stable", sys, before, a1))
    rows.append(row("same_present_future_invalid", sys, before, a2))

    with (OUT / "results.json").open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    fields = [
        "case","before","after","pc","aps","sip","invalidation_latency",
        "current_verifiers","future_verifiers","emergent_verifiers",
        "distinguishing_verifiers","present_partition","future_partition"
    ]
    with (OUT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            rr = r.copy()
            for k in fields:
                if isinstance(rr[k], (list, tuple)):
                    rr[k] = json.dumps(rr[k])
            w.writerow(rr)

    summary = {
        "n_cases": len(rows),
        "pc_true": sum(bool(r["pc"]) for r in rows),
        "aps_true": sum(bool(r["aps"]) for r in rows),
        "sip_true": sum(bool(r["sip"]) for r in rows),
        "separation_observed": any(r["pc"] and not r["aps"] for r in rows),
        "same_present_different_future_status": (
            next(r for r in rows if r["case"]=="same_present_future_stable")["aps"],
            next(r for r in rows if r["case"]=="same_present_future_invalid")["aps"],
        ),
    }
    with (OUT / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
