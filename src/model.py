from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from math import inf
from typing import Callable, Dict, FrozenSet, Iterable, Mapping, Sequence, Set, Tuple

Config = Tuple[int, ...]
VerifierFn = Callable[[Config], object]

@dataclass(frozen=True)
class State:
    name: str
    x: Config
    available: FrozenSet[str]

@dataclass
class System:
    states: Dict[str, State]
    transitions: Dict[str, Tuple[str, ...]]
    verifiers: Dict[str, VerifierFn]

    def reachable(self, start: str) -> Dict[str, int]:
        dist = {start: 0}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in self.transitions.get(u, ()):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    def future_verifiers(self, start: str) -> Tuple[Set[str], Mapping[str, int]]:
        dist = self.reachable(start)
        out: Set[str] = set()
        first: Dict[str, int] = {}
        for s, d in dist.items():
            for v in self.states[s].available:
                out.add(v)
                first[v] = min(first.get(v, d), d)
        return out, first

    def pc(self, before: str, after: str) -> bool:
        b = self.states[before]
        a = self.states[after]
        return all(self.verifiers[v](b.x) == self.verifiers[v](a.x) for v in b.available)

    def aps(self, before: str, after: str) -> bool:
        b = self.states[before]
        a = self.states[after]
        future, _ = self.future_verifiers(after)
        return all(self.verifiers[v](b.x) == self.verifiers[v](a.x) for v in future)

    def distinguishing(self, before: str, after: str) -> Set[str]:
        b = self.states[before]
        a = self.states[after]
        return {v for v, fn in self.verifiers.items() if fn(b.x) != fn(a.x)}

    def sip(self, before: str, after: str) -> bool:
        return self.pc(before, after) and not self.aps(before, after)

    def invalidation_latency(self, before: str, after: str):
        if not self.pc(before, after):
            return 0
        b = self.states[before]
        a = self.states[after]
        _, first = self.future_verifiers(after)
        hits = [first[v] for v, fn in self.verifiers.items()
                if v in first and fn(b.x) != fn(a.x)]
        return min(hits) if hits else inf

    def partition(self, state_names: Sequence[str], verifier_names: Iterable[str]):
        verifier_names = tuple(sorted(verifier_names))
        groups: Dict[Tuple[object, ...], list[str]] = {}
        for name in state_names:
            x = self.states[name].x
            key = tuple(self.verifiers[v](x) for v in verifier_names)
            groups.setdefault(key, []).append(name)
        return tuple(sorted(tuple(sorted(g)) for g in groups.values()))
