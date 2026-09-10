from fastapi import FastAPI, Depends

from dependencies import get_complaint_service
from service import ComplaintService


app = FastAPI()


@app.get("/complaints/{complaint_id}")
def get_complaint(
    complaint_id: int,
    service: ComplaintService = Depends(get_complaint_service)
):
    return service.get_complaint(complaint_id)