from src.external_causal_cases import oneuptime_case, confluence_audit_case, run_external_cases
from src.causal_observation_synthesis import causal_separator

def test_oneuptime_transfer_case():
    l,r,g,o,sym=oneuptime_case()
    s=causal_separator(l,r,g,sym,o)
    assert s is not None
    assert s.node in {"migrated_query","table_schema"}
    assert s.node != "monitor_result"

def test_confluence_transfer_case():
    l,r,g,o,sym=confluence_audit_case()
    s=causal_separator(l,r,g,sym,o)
    assert s is not None
    assert s.node in {"migration_state","audit_format"}
    assert s.node != "audit_view"

def test_external_cases_both_resolve():
    out=run_external_cases()
    assert all(v["status"]=="CAUSAL_SEPARATOR_FOUND" for v in out.values())
