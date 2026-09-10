from database import SessionLocal
from repository import ComplaintRepository
from service import ComplaintService


db = SessionLocal()

repository = ComplaintRepository(db)
service = ComplaintService(repository)

complaint = service.get_complaint(1)

print(complaint)

db.close()