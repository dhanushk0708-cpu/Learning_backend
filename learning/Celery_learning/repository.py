from sqlalchemy import select

from model import Complaint


class ComplaintRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, complaint_id):
        statement = select(Complaint).where(Complaint.id == complaint_id)
        return self.db.scalars(statement).first()

    def update_analysis(self, complaint_id, category, priority):
        complaint = self.get_by_id(complaint_id)

        if complaint is None:
            return None

        complaint.category = category
        complaint.priority = priority

        self.db.commit()
        self.db.refresh(complaint)

        return complaint