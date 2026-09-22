from src.external_label_evaluation import load_labels, evaluate_against_external_labels

def test_labels_are_externalized():
    labels=load_labels()
    assert set(labels)=={"opentelemetry","oneuptime_v11","confluence_audit"}

def test_external_label_evaluation_scores_all_methods():
    rows,summary=evaluate_against_external_labels()
    assert len(rows)==12
    assert "causal_nearest_upstream" in summary
    assert summary["causal_nearest_upstream"]["n"]==3
