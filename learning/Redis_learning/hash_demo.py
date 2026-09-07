import redis

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

client.hset(
    "complaint:20",
    mapping={
        "title": "Pothole road",
        "status": "open",
        "priority": "high"
    }
)

complaint = client.hgetall("complaint:20")

print(complaint)