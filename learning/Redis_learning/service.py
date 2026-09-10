import json

from redis_client import redis_client


class ComplaintService:
    def __init__(self, repository):
        self.repository = repository

    def get_complaint(self, complaint_id: int):
        key = f"complaint:{complaint_id}"

        # 1. Check Redis
        cached_data = redis_client.get(key)

        if cached_data is not None:
            print("CACHE HIT")
            return json.loads(cached_data)

        # 2. Cache miss → PostgreSQL
        print("CACHE MISS")

        complaint = self.repository.get_by_id(complaint_id)

        if complaint is None:
            return None

        # 3. Convert database object to dictionary
        data = {
            "id": complaint.id,
            "title": complaint.title,
            "owner_id": complaint.owner_id
        }

        # 4. Store in Redis for 60 seconds
        redis_client.set(
            key,
            json.dumps(data),
            ex=60
        )

        return data

    def update_complaint(self, complaint_id: int, new_title: str):
        complaint = self.repository.update_title(
            complaint_id,
            new_title
        )

        if complaint is None:
            return None

        key = f"complaint:{complaint_id}"

        # Invalidate stale cache
        redis_client.delete(key)

        return {
            "id": complaint.id,
            "title": complaint.title,
            "owner_id": complaint.owner_id
        }