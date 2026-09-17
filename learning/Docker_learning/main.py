import os

import redis
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True,
)

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)


@app.get("/")
def home():
    return {"message": "FastAPI + Redis + PostgreSQL"}


@app.get("/redis-test")
def redis_test():
    redis_client.set("message", "Hello from Redis!")

    return {
        "redis_value": redis_client.get("message")
    }


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database()"))
        database_name = result.scalar()

    return {
        "database": database_name
    }