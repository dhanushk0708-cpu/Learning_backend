from celery_app import celery
from database import SessionLocal
from repository import ComplaintRepository


@celery.task
def analyze_complaint(complaint_id, title):
    print(f"Analyzing complaint {complaint_id}")
    print(f"Title: {title}")

    category = "Road"
    priority = "HIGH"

    db = SessionLocal()

    try:
        repository = ComplaintRepository(db)

        complaint = repository.update_analysis(
            complaint_id,
            category,
            priority
        )

        if complaint is None:
            return "Complaint not found"

        return "Analysis complete"

    finally:
        db.close()