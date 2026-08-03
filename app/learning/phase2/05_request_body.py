"""
=========================================
PHASE 2

TOPIC : REQUEST BODY
=========================================

USED IN

app/schemas/
app/routers/

"""

# WHY?
# Used to send data from
# Client to Server.

# CIVIL AI IMPLEMENTATION


class ComplaintCreate(BaseModel):
    title: str
    description: str


@router.post("/complaints")
def create_complaint(complaint: ComplaintCreate):
    return complaint


# CONCEPT

# ComplaintCreate
# Defines the expected JSON Body.

# complaint
# Automatically contains
# validated request data.

# INTERNAL FLOW

# React

# ↓ JSON

# FastAPI

# ↓ Pydantic Validation

# Router

# ↓

# Response

# INTERVIEW

# Q: What is Request Body?
#
# A:
# Request Body contains the data
# sent by the client to the server.

# COMMON BEGINNER MISTAKE

# ❌ Receiving many individual
# parameters.

# ✅ Use a Pydantic Schema.

# RELATED CONCEPTS

# JSON

# ↓

# Pydantic

# ↓

# Validation

# REMEMBER

# ✔ Used in POST
# ✔ Uses Pydantic Schema
# ✔ Receives JSON Data
