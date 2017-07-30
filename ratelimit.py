import time


class NomatimRateLimitCache:
    """
    Keep a cache of results, and limit lookups to 1 per second.
    """
    def __init__(self, method):
        self.method = method
        self.cache = {}
        self.last_call = time.time() - 100

    def __call__(self, *args):
        return self.cache.get(args, self._really_call(args))

    def _really_call(self, args):
        since_last_call = time.time() - self.last_call
        if since_last_call < 1:
            time.sleep(since_last_call)
        result = self.method(args)
        self.cache[args] = result
        self.last_call = time.time()
        return result
