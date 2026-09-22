"""Causal separating-observation synthesis for finite dependency graphs.

Given two explanation states, an observed symptom node, and a directed acyclic
dependency graph (cause -> effect), return the nearest upstream observable node
whose values differ across the explanations.

This is a diagnostic ranking layer, not a claim of general causal discovery.
The graph is supplied by the model/domain specification.
"""
from dataclasses import dataclass
from collections import deque
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Tuple

@dataclass(frozen=True)
class CausalSeparator:
    node: str
    distance_to_symptom: int
    left_value: Any
    right_value: Any

def _reverse_graph(graph: Mapping[str, Sequence[str]]) -> Dict[str, list[str]]:
    rev: Dict[str, list[str]] = {}
    for u, vs in graph.items():
        rev.setdefault(u, [])
        for v in vs:
            rev.setdefault(v, []).append(u)
    for v in rev:
        rev[v] = sorted(rev[v])
    return rev

def causal_separator(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
    graph: Mapping[str, Sequence[str]],
    symptom: str,
    observable: Optional[Iterable[str]] = None,
) -> Optional[CausalSeparator]:
    """Return nearest upstream observable differing node.

    Search is reverse-BFS from symptom. The symptom itself is excluded so that
    a shared downstream consequence cannot be returned as its own explanation.
    """
    allowed = set(observable) if observable is not None else set(left).intersection(right)
    rev = _reverse_graph(graph)
    q = deque([(symptom, 0)])
    seen = {symptom}
    candidates = []
    while q:
        node, dist = q.popleft()
        for parent in rev.get(node, []):
            if parent in seen:
                continue
            seen.add(parent)
            nd = dist + 1
            if parent in allowed and parent in left and parent in right and left[parent] != right[parent]:
                candidates.append(CausalSeparator(parent, nd, left[parent], right[parent]))
            q.append((parent, nd))
    if not candidates:
        return None
    return sorted(candidates, key=lambda c: (c.distance_to_symptom, c.node))[0]

def opentelemetry_causal_case():
    # Both explanations lead to the same observed dashboard symptom.
    left = {
        "source_behavior": "failed",
        "raw_signal": "absent",
        "service_identity": "checkout",
        "attribute_mapping": "legacy",
        "query_result": "empty",
        "dashboard": "empty",
    }
    right = {
        "source_behavior": "healthy",
        "raw_signal": "present",
        "service_identity": "checkout-v3",
        "attribute_mapping": "migrated",
        "query_result": "empty",
        "dashboard": "empty",
    }

    # Domain model: system behavior influences raw telemetry; upgrade-induced
    # identity/mapping changes influence query interpretation; query drives dashboard.
    graph = {
        "source_behavior": ["raw_signal"],
        "raw_signal": ["query_result"],
        "service_identity": ["query_result"],
        "attribute_mapping": ["query_result"],
        "query_result": ["dashboard"],
    }
    observable = {
        "raw_signal",
        "service_identity",
        "attribute_mapping",
        "query_result",
        "dashboard",
    }
    return left, right, graph, observable
