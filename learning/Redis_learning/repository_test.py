from database import SessionLocal
from repository import ComplaintRepository


db = SessionLocal()

repository = ComplaintRepository(db)

complaint = repository.get_by_id(1)

print(complaint.title)
print(complaint.owner_id)

db.close()