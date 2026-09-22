"""Independent external-style causal benchmark cases.

These are structured abstractions of documented evolution scenarios already in
the external corpus.  They test transfer of the causal-separator logic across
domains without changing the algorithm.
"""
from src.causal_observation_synthesis import causal_separator

def oneuptime_case():
    left = {
        "telemetry_semantics": "healthy",
        "table_schema": "legacy",
        "migrated_query": "stale",
        "monitor_result": "empty",
    }
    right = {
        "telemetry_semantics": "healthy",
        "table_schema": "v11",
        "migrated_query": "updated",
        "monitor_result": "empty",
    }
    graph = {
        "telemetry_semantics": ["monitor_result"],
        "table_schema": ["migrated_query"],
        "migrated_query": ["monitor_result"],
    }
    obs={"telemetry_semantics","table_schema","migrated_query","monitor_result"}
    return left,right,graph,obs,"monitor_result"

def confluence_audit_case():
    left = {
        "event_semantics": "same_event",
        "audit_format": "legacy",
        "migration_state": "not_migrated",
        "audit_view": "missing",
    }
    right = {
        "event_semantics": "same_event",
        "audit_format": "advanced",
        "migration_state": "migrated",
        "audit_view": "missing",
    }
    graph = {
        "event_semantics": ["audit_view"],
        "audit_format": ["migration_state"],
        "migration_state": ["audit_view"],
    }
    obs={"event_semantics","audit_format","migration_state","audit_view"}
    return left,right,graph,obs,"audit_view"

def run_external_cases():
    cases={}
    for name, factory in [("oneuptime_v11",oneuptime_case),("confluence_audit",confluence_audit_case),("gcp_datafusion_v3",gcp_datafusion_case)]:
        left,right,graph,obs,symptom=factory()
        s=causal_separator(left,right,graph,symptom,obs)
        cases[name]={
            "status":"CAUSAL_SEPARATOR_FOUND" if s else "NO_CAUSAL_SEPARATOR",
            "node":s.node if s else None,
            "distance":s.distance_to_symptom if s else None,
            "left":s.left_value if s else None,
            "right":s.right_value if s else None,
        }
    return cases


def gcp_datafusion_case():
    left = {
        "metric_semantics": "same_pipeline_state",
        "resource_metric_schema": "InstanceV2",
        "migrated_query": "legacy_query",
        "dashboard_result": "empty",
    }
    right = {
        "metric_semantics": "same_pipeline_state",
        "resource_metric_schema": "InstanceV3",
        "migrated_query": "updated_query",
        "dashboard_result": "empty",
    }
    graph = {
        "metric_semantics": ["dashboard_result"],
        "resource_metric_schema": ["migrated_query"],
        "migrated_query": ["dashboard_result"],
    }
    obs={"metric_semantics","resource_metric_schema","migrated_query","dashboard_result"}
    return left,right,graph,obs,"dashboard_result"
