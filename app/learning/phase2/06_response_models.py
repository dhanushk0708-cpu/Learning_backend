"""
=========================================
PHASE 2

TOPIC : RESPONSE MODELS
=========================================

USED IN

app/schemas/
app/routers/

"""

# WHY?
# Controls what data is returned
# to the client.

# CIVIL AI IMPLEMENTATION


class ComplaintResponse(BaseModel):
    id: int
    title: str
    status: str


@router.get("/complaints/{id}", response_model=ComplaintResponse)
def get_complaint(): ...


# CONCEPT

# response_model
# Filters the API Response.

# Only fields inside
# ComplaintResponse
# are returned.

# INTERNAL FLOW

# Database

# ↓

# Router

# ↓

# Response Model

# ↓

# JSON

# ↓

# React

# INTERVIEW

# Q: Why use Response Models?
#
# A:
# To return only required data
# and hide internal fields.

# COMMON BEGINNER MISTAKE

# ❌ Returning Database Model
# directly.

# ✅ Return Response Model.

# RELATED CONCEPTS

# Database Model

# ↓

# Response Model

# ↓

# JSON Response

# REMEMBER

# ✔ Controls API Output
# ✔ Improves Security
# ✔ Keeps Responses Consistent
