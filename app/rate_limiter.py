import redis
from config import Config

class RateLimiter:
    def __init__(self):
        self.r = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            decode_responses=True
        )

    def is_over_limit(self, ip: str) -> bool:
        key = f"rate_limit:{ip}"
        current = self.r.incr(key)
        if current == 1:
            self.r.expire(key, 60)  # Reset counter every 60 seconds
        return current > Config.REQUEST_LIMIT
