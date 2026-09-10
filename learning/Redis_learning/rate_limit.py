from fastapi import HTTPException

from redis_client import redis_client


def check_rate_limit(client_id: str, limit: int = 5):
    key = f"rate_limit:{client_id}"

    current_count = redis_client.incr(key)

    if current_count == 1:
        redis_client.expire(key, 60)

    if current_count > limit:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )