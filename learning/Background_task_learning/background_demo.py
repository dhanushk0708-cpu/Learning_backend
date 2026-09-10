from fastapi import FastAPI, BackgroundTasks
import time


app = FastAPI()


def process_complaint():
    print("Background task started")

    time.sleep(5)

    print("Background task finished")


@app.post("/complaints")
def create_complaint(background_tasks: BackgroundTasks):

    print("Complaint created")

    background_tasks.add_task(process_complaint)

    return {
        "message": "Complaint created"
    }