from __future__ import annotations
from .model import State, System

VERIFIERS = {
    "v1": lambda x: x[0],
    "v2": lambda x: x[1],
}

def immediate_invalid() -> tuple[System, str, str]:
    states = {
        "s0": State("s0", (0, 0), frozenset({"v1"})),
        "s1": State("s1", (1, 0), frozenset({"v1"})),
    }
    return System(states, {"s1": ()}, VERIFIERS), "s0", "s1"

def latent_invalid() -> tuple[System, str, str]:
    states = {
        "s0": State("s0", (0, 0), frozenset({"v1"})),
        "s1": State("s1", (0, 1), frozenset({"v1"})),
        "s2": State("s2", (0, 1), frozenset({"v1", "v2"})),
    }
    return System(states, {"s1": ("s2",), "s2": ()}, VERIFIERS), "s0", "s1"

def absolutely_stable() -> tuple[System, str, str]:
    states = {
        "s0": State("s0", (0, 0), frozenset({"v1"})),
        "s1": State("s1", (0, 1), frozenset({"v1"})),
        "s2": State("s2", (0, 1), frozenset({"v1"})),
    }
    return System(states, {"s1": ("s2",), "s2": ()}, VERIFIERS), "s0", "s1"

def same_present_different_future():
    # Same ordinary transformed configuration, different complete states / verifier-generating structures.
    states = {
        "s0": State("s0", (0, 0), frozenset({"v1"})),
        "a1": State("a1", (0, 1), frozenset({"v1"})),
        "a2": State("a2", (0, 1), frozenset({"v1"})),
        "a2_future": State("a2_future", (0, 1), frozenset({"v1", "v2"})),
    }
    sys = System(
        states,
        {
            "a1": (),
            "a2": ("a2_future",),
            "a2_future": (),
        },
        VERIFIERS,
    )
    return sys, "s0", "a1", "a2"
