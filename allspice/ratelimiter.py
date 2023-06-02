import functools
import time

import requests


class RateLimiter:
    """
    A decorator to rate limit a function call.

    :param max_calls: Maximum number of calls per period
    :param period: Time period in seconds

    Example:

        @RateLimiter(max_calls=10, period=1)  # 10 requests per second
        def make_request(url):
            pass
    """

    def __init__(self, max_calls, period=1.0):
        assert period > 0, "Period should be a positive number"
        assert max_calls >= 1, "max_calls should be at least one"
        self.max_calls = int(max_calls)
        self.period = float(period)
        self.calls = 0
        self.reset_time = time.time()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if time.time() - self.reset_time > self.period:
                self.calls = 0
                self.reset_time = time.time()

            if self.calls < self.max_calls:
                self.calls += 1
            else:
                time.sleep(self.period - (time.time() - self.reset_time))
                return wrapper(*args, **kwargs)

            return func(*args, **kwargs)

        return wrapper


class RateLimitedSession(requests.Session):
    def __init__(self, max_calls, period=1.0):
        super().__init__()
        self.rate_limiter = RateLimiter(max_calls, period)
        self.request = self.rate_limiter(self.request)

    def request(self, *args, **kwargs):
        return super().request(*args, **kwargs)
