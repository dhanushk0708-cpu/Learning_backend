"""
=========================================================

PHASE 4

TOPIC : EXCEPTION HANDLING

=========================================================

REAL PROJECT FILES

app/routers/complaint_router.py

app/repositories/complaint_repository.py

Reason:
Exception Handling provides meaningful
error messages and correct HTTP Status Codes
when something goes wrong.

=========================================================
"""

from fastapi import HTTPException

# ==========================================================
# WHY?
# ==========================================================

# Instead of crashing the application,
# return meaningful errors to the frontend.

# Good APIs tell the client:
# What went wrong?
# Why?
# What is the status?


# ==========================================================
# CIVIL AI IMPLEMENTATION
# File : app/repositories/complaint_repository.py
# ==========================================================

def get_by_id(db: Session, complaint_id: int):

    complaint = (

        db.query(ComplaintModel)

        .filter(ComplaintModel.id == complaint_id)

        .first()

    )

    # ------------------------------------------------------
    # CONCEPT : Validation
    #
    # Check whether complaint exists.
    # ------------------------------------------------------

    if complaint is None:

        # --------------------------------------------------
        # CONCEPT : HTTPException
        #
        # Return proper HTTP Status Code
        # and meaningful error message.
        # --------------------------------------------------

        raise HTTPException(

            status_code=404,

            detail="Complaint not found."

        )

    return complaint


# ==========================================================
# ROUTER
# File : app/routers/complaint_router.py
# ==========================================================

@router.get(
    "/complaints/{complaint_id}",
    response_model=ComplaintResponse
)
def get_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    return complaint_repository.get_by_id(
        db,
        complaint_id
    )


# ==========================================================
# COMMON HTTP STATUS CODES
# ==========================================================

# 200 -> Success

# 201 -> Resource Created

# 400 -> Bad Request

# 401 -> Unauthorized

# 403 -> Forbidden

# 404 -> Not Found

# 500 -> Internal Server Error


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Browser
#      ↓
# GET /complaints/100
#      ↓
# Router
#      ↓
# Repository
#      ↓
# Search Complaint
#      ↓
#
# Exists?
#
#      ↓
#
# YES ----------------→ Return Complaint
#
# NO
#
# ↓
#
# Raise HTTPException(404)
#
# ↓
#
# FastAPI
#
# ↓
#
# JSON Error Response
#
# ↓
#
# React


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why do we use Exception Handling?
#
# A:
# Exception Handling returns meaningful
# HTTP Status Codes and error messages
# instead of crashing the application.
#
# It improves debugging, API reliability
# and user experience.


# ==========================================================
# COMMON BEGINNER MISTAKE
# ==========================================================

# ❌

# return "Error"

# or

# return None

# ------------------------------

# ✅

# raise HTTPException(
#     status_code=404,
#     detail="Complaint not found."
# )


# ==========================================================
# RELATED CONCEPTS
# ==========================================================

# Request
#
# ↓
#
# Router
#
# ↓
#
# Repository
#
# ↓
#
# Validation
#
# ↓
#
# Success
#      OR
#
# HTTPException
#
# ↓
#
# JSON Response


# ==========================================================
# WHERE WILL WE USE THIS IN CIVIL AI?
# ==========================================================

# Complaint APIs

# Officer APIs

# Citizen APIs

# Login APIs

# AI APIs

# Every API should return
# meaningful HTTP Status Codes
# and error messages.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Never return plain "Error"
#
# ✔ Use HTTPException
#
# ✔ Use correct Status Codes
#
# ✔ Give meaningful messages
#
# ✔ Handle expected errors gracefully
"""