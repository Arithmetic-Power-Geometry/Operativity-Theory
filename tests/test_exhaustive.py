from src.exhaustive import main

def test_exhaustive_exact_characterization(tmp_path, monkeypatch):
    import src.exhaustive as e
    monkeypatch.setattr(e,"OUT",tmp_path)
    e.main()
    import json
    s=json.loads((tmp_path/"exhaustive_summary.json").read_text())
    assert s["enumerated_systems"] > 0
    assert s["pc_implies_aps_counterexamples"] > 0
    assert s["t2_characterization_violations"] == 0
    assert s["all_exact_checks_pass"] is True
