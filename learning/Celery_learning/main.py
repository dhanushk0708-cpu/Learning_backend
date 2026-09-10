from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import analyze_complaint

app = FastAPI()


@app.post("/complaints/{complaint_id}/analyze")
def analyze(complaint_id: int, title: str):
    task = analyze_complaint.delay(complaint_id, title)

    return {
        "message": "Analysis started",
        "task_id": task.id
    }


@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task = AsyncResult(task_id)

    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result
    }