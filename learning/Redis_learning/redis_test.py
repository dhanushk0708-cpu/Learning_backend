import redis

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def get_complaint(complaint_id):
    key = f"complaint:{complaint_id}"

    # 1. Check Redis
    cached_data = client.get(key)

    if cached_data:
        print("CACHE HIT")
        return cached_data

    # 2. Redis miss → pretend to query PostgreSQL
    print("CACHE MISS")
    complaint = "Broken road"

    # 3. Store result in Redis
    client.set(key, complaint, ex=60)

    return complaint


result = get_complaint(1)

print("Result:", result)