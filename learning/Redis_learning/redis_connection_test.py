from redis_client import redis_client


redis_client.set("test_key", "Redis is working")

value = redis_client.get("test_key")

print(value)