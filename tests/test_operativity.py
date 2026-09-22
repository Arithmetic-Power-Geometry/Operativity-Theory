import math
from src.examples import immediate_invalid, latent_invalid, absolutely_stable, same_present_different_future

def test_immediate_invalid():
    s,b,a = immediate_invalid()
    assert s.pc(b,a) is False
    assert s.aps(b,a) is False
    assert s.invalidation_latency(b,a) == 0

def test_latent_invalid():
    s,b,a = latent_invalid()
    assert s.pc(b,a) is True
    assert s.aps(b,a) is False
    assert s.sip(b,a) is True
    assert s.invalidation_latency(b,a) == 1

def test_absolute_stability():
    s,b,a = absolutely_stable()
    assert s.pc(b,a) is True
    assert s.aps(b,a) is True
    assert s.sip(b,a) is False
    assert math.isinf(s.invalidation_latency(b,a))

def test_same_present_different_future():
    s,b,a1,a2 = same_present_different_future()
    assert s.states[a1].x == s.states[a2].x
    assert s.pc(b,a1) and s.pc(b,a2)
    assert s.aps(b,a1) is True
    assert s.aps(b,a2) is False
