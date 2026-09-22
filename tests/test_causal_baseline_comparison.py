from src.causal_baseline_comparison import evaluate_baselines

def test_all_cases_have_causal_relevant_separator():
    rows=evaluate_baselines()
    causal=[r for r in rows if r.method=="causal_nearest_upstream"]
    assert len(causal)==3
    assert all(r.diagnostic_relevant for r in causal)

def test_all_methods_return_or_none():
    rows=evaluate_baselines()
    assert len(rows)==12

def test_comparison_has_noncausal_baselines():
    rows=evaluate_baselines()
    assert {r.method for r in rows} == {
        "nearest_differing_field",
        "cheapest_differing_field",
        "random_differing_field",
        "causal_nearest_upstream",
    }
