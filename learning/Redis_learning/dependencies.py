from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from repository import ComplaintRepository
from service import ComplaintService


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_complaint_repository(
    db: Session = Depends(get_db)
):
    return ComplaintRepository(db)


def get_complaint_service(
    repository: ComplaintRepository = Depends(get_complaint_repository)
):
    return ComplaintService(repository)