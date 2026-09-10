import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


complaint = {
    "id": 101,
    "title": "Large pothole near school"
}

job = f"{complaint['id']}|{complaint['title']}"

redis_client.rpush("complaint_jobs", job)

print("Complaint analysis job added")