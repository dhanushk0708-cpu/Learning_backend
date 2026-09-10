import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def analyze_complaint(title: str):
    title_lower = title.lower()

    if "pothole" in title_lower or "road" in title_lower:
        category = "Road"
        priority = "HIGH"

    elif "garbage" in title_lower or "waste" in title_lower:
        category = "Waste"
        priority = "MEDIUM"

    elif "water" in title_lower or "leak" in title_lower:
        category = "Water"
        priority = "HIGH"

    else:
        category = "Other"
        priority = "LOW"

    return category, priority


print("Worker started. Waiting for jobs...")


while True:
    job = redis_client.lpop("complaint_jobs")

    if job:
        complaint_id, title = job.split("|", 1)

        print(f"\nProcessing complaint {complaint_id}")
        print(f"Title: {title}")

        category, priority = analyze_complaint(title)

        print(f"Category: {category}")
        print(f"Priority: {priority}")
        print("Analysis complete")

    else:
        import time
        time.sleep(1)