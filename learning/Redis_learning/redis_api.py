from fastapi import FastAPI

from redis_client import redis_client


app = FastAPI()


@app.get("/cache/{key}")
def get_cache(key: str):
    value = redis_client.get(key)

    if value is None:
        return {"message": "Cache miss"}

    return {
        "message": "Cache hit",
        "value": value
    }

@app.post("/cache/{key}")
def set_cache(key: str, value: str, ttl: int = 60):
    redis_client.set(key, value, ex=ttl)

    return {
        "message": "Value cached",
        "key": key,
        "ttl": ttl
    }