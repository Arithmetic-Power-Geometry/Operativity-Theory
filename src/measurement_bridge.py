"""Bridge from an unresolved certification comparison to a separating measurement.

This module does not introduce a new verification algorithm.  It operationalizes
an interface: Operativity supplies a pair that needs distinguishing; a finite
Empirical-Reach-style search chooses the least-cost admissible observation that
separates the competing explanations.
"""
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Optional

@dataclass(frozen=True)
class CandidateMeasurement:
    name: str
    cost: float
    observe: Callable[[Any], Any]
    admissible: bool = True

@dataclass(frozen=True)
class SeparationResult:
    status: str
    measurement: Optional[str]
    cost: Optional[float]
    left_value: Any = None
    right_value: Any = None

def cheapest_separator(left: Any, right: Any,
                       measurements: Iterable[CandidateMeasurement]) -> SeparationResult:
    """Return the least-cost admissible measurement whose outputs differ."""
    candidates = sorted(
        (m for m in measurements if m.admissible),
        key=lambda m: (m.cost, m.name),
    )
    for m in candidates:
        lv, rv = m.observe(left), m.observe(right)
        if lv != rv:
            return SeparationResult("SEPARATED", m.name, m.cost, lv, rv)
    return SeparationResult("UNRESOLVED_IN_DECLARED_CLOSURE", None, None)

def opentelemetry_demo_case():
    # Same derived symptom: an empty legacy dashboard.
    h_system = {
        "dashboard": "empty",
        "raw_signal": None,
        "service": "checkout",
        "attrs": frozenset(),
        "semantic_mapping_ok": False,
    }
    h_contract = {
        "dashboard": "empty",
        "raw_signal": "healthy",
        "service": "checkout-v3",
        "attrs": frozenset({"service.name", "http.request.method"}),
        "semantic_mapping_ok": True,
    }
    measurements = [
        CandidateMeasurement("legacy_dashboard", 0.0, lambda h: h["dashboard"]),
        CandidateMeasurement("raw_collector_signal", 1.0, lambda h: h["raw_signal"]),
        CandidateMeasurement("service_identity", 1.2, lambda h: h["service"]),
        CandidateMeasurement("attribute_key_set", 1.5, lambda h: h["attrs"]),
        CandidateMeasurement("semantic_mapping_check", 2.0, lambda h: h["semantic_mapping_ok"]),
    ]
    return h_system, h_contract, measurements
