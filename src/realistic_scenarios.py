from __future__ import annotations
import json
from pathlib import Path
from .model import State, System

OUT=Path("artifacts")

def api_migration():
    # Legacy/new API agree on public response. A later diagnostic endpoint
    # exposes changed error provenance.
    states={
      "legacy":State("legacy",(200,0),frozenset({"status"})),
      "migrated":State("migrated",(200,1),frozenset({"status"})),
      "diag_enabled":State("diag_enabled",(200,1),frozenset({"status","provenance"})),
    }
    return System(states,{"migrated":("diag_enabled",),"diag_enabled":()},{
      "status":lambda x:x[0],"provenance":lambda x:x[1]}),"legacy","migrated"

def authorization_upgrade():
    # Immediate allowed/denied decision is preserved, but later audit capability
    # reveals a changed authority source/delegation path.
    states={
      "old":State("old",(1,0),frozenset({"decision"})),
      "new":State("new",(1,1),frozenset({"decision"})),
      "audit":State("audit",(1,1),frozenset({"decision","authority_source"})),
    }
    return System(states,{"new":("audit",),"audit":()},{
      "decision":lambda x:x[0],"authority_source":lambda x:x[1]}),"old","new"

def instrumentation_upgrade():
    # Application output is preserved, while a later high-resolution timing
    # observer reveals instrumentation-induced timing-class change.
    states={
      "plain":State("plain",(0,0),frozenset({"output"})),
      "instrumented":State("instrumented",(0,1),frozenset({"output"})),
      "hires":State("hires",(0,1),frozenset({"output","timing_class"})),
    }
    return System(states,{"instrumented":("hires",),"hires":()},{
      "output":lambda x:x[0],"timing_class":lambda x:x[1]}),"plain","instrumented"

def stable_control():
    states={
      "old":State("old",(1,0),frozenset({"decision"})),
      "new":State("new",(1,0),frozenset({"decision"})),
      "audit":State("audit",(1,0),frozenset({"decision","authority_source"})),
    }
    return System(states,{"new":("audit",),"audit":()},{
      "decision":lambda x:x[0],"authority_source":lambda x:x[1]}),"old","new"

def analyze(name,builder):
    s,b,a=builder()
    d=sorted(s.distinguishing(b,a))
    return {"scenario":name,"pc":s.pc(b,a),"aps":s.aps(b,a),
            "sip":s.sip(b,a),"invalidation_latency":s.invalidation_latency(b,a),
            "distinguishing_verifiers":d,
            "future_verifiers":sorted(s.future_verifiers(a)[0])}

def main():
    OUT.mkdir(exist_ok=True)
    rows=[analyze("api_migration",api_migration),
          analyze("authorization_upgrade",authorization_upgrade),
          analyze("instrumentation_upgrade",instrumentation_upgrade),
          analyze("stable_control",stable_control)]
    summary={
      "scenarios":len(rows),
      "latent_invalid":sum(r["pc"] and not r["aps"] for r in rows),
      "stable":sum(r["aps"] for r in rows),
      "all_latent_have_named_witness":all(r["distinguishing_verifiers"] for r in rows if r["pc"] and not r["aps"]),
    }
    (OUT/"realistic_scenarios.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    (OUT/"realistic_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps({"summary":summary,"cases":rows},indent=2))

if __name__=="__main__": main()
