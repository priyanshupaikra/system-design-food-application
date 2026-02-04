# Token Bucket (Simplified)
import time
class RateLimiter:
    def __init__(self, max_requests, window_sec):
        self.max_requests = max_requests
        self.window_sec = window_sec
        self.requests = {}

    def allow_request(self, user_id):
        now = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = []

        self.requests[user_id] = [
            t for t in self.requests[user_id]
            if now - t < self.window_sec
        ]

        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(now)
            return True
        return False

# Usage
rate_limiter = RateLimiter(3, 10)

if rate_limiter.allow_request(user.user_id):
    order_service.place_order(user, restaurant, foods)
else:
    print("Too many requests")

# Sliding window rate limiting
