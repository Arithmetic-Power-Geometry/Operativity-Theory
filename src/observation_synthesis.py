"""Automatic synthesis of finite separating observations.

Given two structured explanation states, derive candidate path observations from
their structure and return the least-cost path whose values differ.

This is intentionally finite and transparent.  It does not claim novelty over
general feature selection or experiment design; it operationalizes the bridge
from an unresolved certification comparison to a concrete observation request.
"""
from dataclasses import dataclass
from typing import Any, Iterable, Optional, Tuple

@dataclass(frozen=True)
class SynthesizedObservation:
    path: Tuple[Any, ...]
    cost: float
    left_value: Any
    right_value: Any

def _is_mapping(x: Any) -> bool:
    return isinstance(x, dict)

def _is_sequence(x: Any) -> bool:
    return isinstance(x, (list, tuple))

def _children(x: Any):
    if _is_mapping(x):
        for k in sorted(x, key=lambda z: repr(z)):
            yield k, x[k]
    elif _is_sequence(x):
        for i, v in enumerate(x):
            yield i, v

def _get(root: Any, path: Tuple[Any, ...]) -> Any:
    cur = root
    for p in path:
        if isinstance(cur, dict):
            cur = cur[p]
        else:
            cur = cur[p]
    return cur

def enumerate_observation_paths(left: Any, right: Any) -> Iterable[Tuple[Any, ...]]:
    """Enumerate common finite paths present in both structured states."""
    stack=[((), left, right)]
    while stack:
        path,l,r=stack.pop()
        # leaf/common node itself is an observable candidate
        if path:
            yield path
        if isinstance(l, dict) and isinstance(r, dict):
            keys=sorted(set(l).intersection(r), key=lambda z: repr(z), reverse=True)
            for k in keys:
                stack.append((path+(k,), l[k], r[k]))
        elif isinstance(l,(list,tuple)) and isinstance(r,(list,tuple)):
            for i in reversed(range(min(len(l),len(r)))):
                stack.append((path+(i,), l[i], r[i]))

def path_cost(path: Tuple[Any, ...]) -> float:
    """Simple transparent structural cost: one unit per dereference."""
    return float(len(path))

def synthesize_separator(left: Any, right: Any) -> Optional[SynthesizedObservation]:
    """Infer the least-cost common observation path that distinguishes states."""
    best=None
    for path in enumerate_observation_paths(left,right):
        lv=_get(left,path)
        rv=_get(right,path)
        if lv != rv:
            cand=SynthesizedObservation(path,path_cost(path),lv,rv)
            if best is None or (cand.cost, tuple(map(repr,cand.path))) < (best.cost, tuple(map(repr,best.path))):
                best=cand
    return best

def synthesize_all_minimal_separators(left: Any, right: Any):
    """Return all distinguishing paths with minimum structural cost."""
    seps=[]
    for path in enumerate_observation_paths(left,right):
        lv=_get(left,path); rv=_get(right,path)
        if lv != rv:
            seps.append(SynthesizedObservation(path,path_cost(path),lv,rv))
    if not seps:
        return []
    m=min(s.cost for s in seps)
    return sorted((s for s in seps if s.cost==m), key=lambda s: tuple(map(repr,s.path)))
