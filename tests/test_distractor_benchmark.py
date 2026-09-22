from src.distractor_benchmark import evaluate_hard

def test_hard_benchmark_shape():
    rows=evaluate_hard()
    assert len(rows)==4*5*4

def test_causal_robust_to_distractors():
    rows=evaluate_hard()
    causal=[r for r in rows if r.method=="causal_nearest_upstream"]
    assert all(r.relevant for r in causal)

def test_cheapest_baseline_degrades_with_distractors():
    rows=evaluate_hard()
    hard=[r for r in rows if r.method=="cheapest_differing_field" and r.distractors>0]
    assert any(not r.relevant for r in hard)
