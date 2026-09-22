from src.measurement_bridge import cheapest_separator, opentelemetry_demo_case, CandidateMeasurement

def test_dashboard_does_not_separate_but_raw_telemetry_does():
    left, right, ms = opentelemetry_demo_case()
    assert ms[0].observe(left) == ms[0].observe(right)
    r = cheapest_separator(left, right, ms)
    assert r.status == "SEPARATED"
    assert r.measurement == "raw_collector_signal"
    assert r.cost == 1.0

def test_no_separator_in_declared_closure():
    left = {"x": 1}
    right = {"x": 1}
    ms = [CandidateMeasurement("x", 0.0, lambda h: h["x"])]
    r = cheapest_separator(left, right, ms)
    assert r.status == "UNRESOLVED_IN_DECLARED_CLOSURE"
