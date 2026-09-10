from sqlalchemy import select

from model import Complaint


class ComplaintRepository:
    def __init__(self, db):
        self.db = db

    def get_by_id(self, complaint_id: int):
        statement = select(Complaint).where(
            Complaint.id == complaint_id
        )

        return self.db.scalar(statement)

    def update_title(self, complaint_id: int, new_title: str):
        complaint = self.db.get(Complaint, complaint_id)

        if complaint is None:
            return None

        complaint.title = new_title

        self.db.commit()
        self.db.refresh(complaint)

        return complaint