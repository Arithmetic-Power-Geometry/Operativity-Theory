from src.blind_label_evaluation import load_blind_labels, evaluate_blind

def test_blind_labels_have_sources():
    labels=load_blind_labels()
    assert set(labels)=={"opentelemetry","oneuptime_v11","confluence_audit","gcp_datafusion_v3"}
    assert all(v["source"].startswith("https://") for v in labels.values())

def test_blind_eval_scores_four_methods():
    rows,summary=evaluate_blind()
    assert len(rows)==16
    assert len(summary)==4
    assert summary["causal_nearest_upstream"]["n"]==4
