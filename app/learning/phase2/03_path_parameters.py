"""
=========================================
PHASE 2

TOPIC : PATH PARAMETERS
=========================================

USED IN

app/routers/

"""

# WHY?
# Used to identify a specific resource.

# CIVIL AI IMPLEMENTATION


@router.get("/complaints/{complaint_id}")
def get_complaint(complaint_id: int):
    return {"id": complaint_id}


# CONCEPT

# {complaint_id}
# Dynamic value from URL.

# complaint_id: int
# FastAPI converts URL value
# into Integer.

# INTERNAL FLOW

# GET /complaints/10

# ↓

# complaint_id = 10

# ↓

# Python Function

# INTERVIEW

# Q: When do we use Path Parameters?
#
# A:
# To identify a specific resource.

# COMMON BEGINNER MISTAKE

# ❌ Using Query Parameters
# for Resource ID.

# ✅ Use Path Parameters
# for Resource IDs.

# RELATED CONCEPTS

# REST API

# ↓

# GET /complaints/{id}

# REMEMBER

# ✔ Used for IDs
# ✔ Required Value
# ✔ Part of URL Path
