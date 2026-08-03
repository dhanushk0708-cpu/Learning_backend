"""
=========================================
PHASE 2

TOPIC : BACKGROUND TASKS
=========================================

USED IN

app/routers/

"""

from fastapi import BackgroundTasks

# WHY?
# Run long tasks after
# sending the API response.

# CIVIL AI IMPLEMENTATION


@router.post("/complaints")
def create_complaint(background_tasks: BackgroundTasks):

    background_tasks.add_task(send_notification)

    return {"message": "Complaint Created"}


# CONCEPT

# API returns Response

# ↓

# Background Task Starts

# ↓

# Notification
# Email
# Logging

# INTERNAL FLOW

# Request

# ↓

# Router

# ↓

# Response Sent

# ↓

# Background Task Runs

# INTERVIEW

# Q: Why use Background Tasks?
#
# A:
# To execute time-consuming work
# after sending the response.

# COMMON BEGINNER MISTAKE

# ❌ Wait for Email to send
# before returning Response.

# ✅ Return Response first,
# then execute the task.

# RELATED CONCEPTS

# Request

# ↓

# Response

# ↓

# Background Task

# REMEMBER

# ✔ Faster User Experience
# ✔ Runs After Response
# ✔ Good for Email, Logging, Notifications
