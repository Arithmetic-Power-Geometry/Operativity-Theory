from src.observation_synthesis import synthesize_separator, synthesize_all_minimal_separators
from src.measurement_bridge import opentelemetry_demo_case

def test_synthesizes_separator_without_measurement_list():
    left,right,_ = opentelemetry_demo_case()
    s=synthesize_separator(left,right)
    assert s is not None
    assert s.left_value != s.right_value
    assert s.path in {("raw_signal",),("service",),("attrs",),("semantic_mapping_ok",)}

def test_dashboard_is_not_returned_as_separator():
    left,right,_ = opentelemetry_demo_case()
    s=synthesize_separator(left,right)
    assert s.path != ("dashboard",)

def test_unresolved_when_structures_equal():
    x={"a":{"b":1}}
    assert synthesize_separator(x,x) is None
    assert synthesize_all_minimal_separators(x,x)==[]

def test_nested_path_generation():
    left={"telemetry":{"raw":{"status":"missing"}}}
    right={"telemetry":{"raw":{"status":"healthy"}}}
    s=synthesize_separator(left,right)
    assert s is not None
    assert s.path == ("telemetry",)
