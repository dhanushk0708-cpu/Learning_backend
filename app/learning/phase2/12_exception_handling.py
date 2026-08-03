"""
=========================================
PHASE 2

TOPIC : EXCEPTION HANDLING
=========================================

USED IN

app/routers/

"""

from fastapi import HTTPException

# WHY?
# Return meaningful errors
# instead of crashing.

# CIVIL AI IMPLEMENTATION


@router.get("/complaints/{id}")
def get_complaint(id: int):

    if id != 1:
        raise HTTPException(status_code=404, detail="Complaint not found")

    return {"id": id}


# CONCEPT

# raise HTTPException()

# ↓

# FastAPI

# ↓

# JSON Error Response

# INTERNAL FLOW

# Request

# ↓

# Router

# ↓

# Exception ?

# YES → Error Response

# NO  → Success Response

# INTERVIEW

# Q: Why use HTTPException?
#
# A:
# To return proper HTTP Status Codes
# and meaningful error messages.

# COMMON BEGINNER MISTAKE

# ❌ return "Error"

# ✅ raise HTTPException()

# RELATED CONCEPTS

# Status Codes

# ↓

# HTTPException

# ↓

# JSON Error

# REMEMBER

# ✔ Use HTTPException
# ✔ Return Proper Status Codes
# ✔ Never return plain "Error"

# NOTE

# Advanced Exception Handling
# is covered in Phase 4.
