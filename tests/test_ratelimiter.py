import pytest
import time
from allspice.ratelimiter import RateLimiter

def test_rate_limiter_exceed_max_calls():
    @RateLimiter(max_calls=10, period=1)
    def dummy_func(x):
        return x

    for i in range(10):
        dummy_func(i)

    start = time.time()
    dummy_func(0)
    assert (time.time() - start) >= 1

def test_rate_limiter_reset_period():
    @RateLimiter(max_calls=5, period=1)
    def dummy_func(x):
        return x

    for i in range(5):
        dummy_func(i)

    time.sleep(1)

    start = time.time()
    dummy_func(0)
    assert (time.time() - start) < 0.1

def test_rate_limiter_sleep():
    @RateLimiter(max_calls=1, period=2)
    def dummy_func(x):
        return x

    dummy_func(0)

    start = time.time()
    dummy_func(0)
    assert (time.time() - start) >= 2
