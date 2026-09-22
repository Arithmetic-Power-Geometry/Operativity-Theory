from src.causal_observation_synthesis import causal_separator, opentelemetry_causal_case

def test_causal_separator_excludes_shared_symptom():
    left,right,graph,obs = opentelemetry_causal_case()
    s = causal_separator(left,right,graph,"dashboard",obs)
    assert s is not None
    assert s.node != "dashboard"
    assert s.left_value != s.right_value

def test_returns_nearest_upstream_divergence():
    left,right,graph,obs = opentelemetry_causal_case()
    s = causal_separator(left,right,graph,"dashboard",obs)
    # query_result is shared; nearest differing observable parents are distance 2.
    assert s.distance_to_symptom == 2
    assert s.node in {"attribute_mapping","raw_signal","service_identity"}

def test_no_causal_separator_when_upstream_observables_same():
    left={"cause":1,"symptom":"x"}
    right={"cause":1,"symptom":"x"}
    graph={"cause":["symptom"]}
    assert causal_separator(left,right,graph,"symptom",{"cause","symptom"}) is None

def test_prefers_closer_divergence():
    left={"root":0,"mid":0,"symptom":"same"}
    right={"root":1,"mid":1,"symptom":"same"}
    graph={"root":["mid"],"mid":["symptom"]}
    s=causal_separator(left,right,graph,"symptom",{"root","mid","symptom"})
    assert s.node=="mid"
    assert s.distance_to_symptom==1
