import json
import src.generated_verifiers as g

def test_generated_verifier_pair_semantic_quotient(tmp_path, monkeypatch):
    monkeypatch.setattr(g,"OUT",tmp_path)
    g.main()
    s=json.loads((tmp_path/"generated_verifier_summary.json").read_text())
    assert s["syntactic_verifiers"] > s["max_pair_semantic_classes"]
    assert s["quotient_equivalence_violations"] == 0
    assert s["all_pair_semantic_checks_pass"] is True
