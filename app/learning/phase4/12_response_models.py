"""
=========================================================

PHASE 4

TOPIC : RESPONSE MODELS

=========================================================

REAL PROJECT FILES

app/models/complaint_model.py

app/schemas/complaint_schema.py

app/routers/complaint_router.py

Reason:
Response Models control what data is
sent back to the frontend.

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Never expose Database Models directly.
#
# Return only the fields the frontend needs.
#
# This improves:
# ✔ Security
# ✔ API Consistency
# ✔ Maintainability


# ==========================================================
# DATABASE MODEL
# File : app/models/complaint_model.py
# ==========================================================

class ComplaintModel(Base):

    id = Column(Integer, primary_key=True)

    title = Column(String)

    description = Column(String)

    citizen_phone = Column(String)

    internal_notes = Column(String)

# ------------------------------------------------------
# CONCEPT
#
# Database Model contains ALL columns.
#
# Internal fields should NOT be exposed
# to the frontend.
# ------------------------------------------------------


# ==========================================================
# RESPONSE MODEL
# File : app/schemas/complaint_schema.py
# ==========================================================

class ComplaintResponse(BaseModel):

    id: int

    title: str

    description: str

# ------------------------------------------------------
# CONCEPT
#
# Response Model contains only
# the fields we want to return.
# ------------------------------------------------------


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

# ------------------------------------------------------
# CONCEPT : response_model
#
# FastAPI automatically converts
# the returned data into the
# ComplaintResponse schema.
#
# Extra fields are not included
# in the API response.
# ------------------------------------------------------


# ==========================================================
# REAL PROJECT FLOW
# ==========================================================

# Database
#
# ComplaintModel
#
#        ↓
#
# Repository
#
#        ↓
#
# Router
#
#        ↓
#
# response_model=ComplaintResponse
#
#        ↓
#
# JSON
#
#        ↓
#
# React


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why use Response Models?
#
# A:
# Response Models control the data
# returned to clients.
#
# They hide internal database fields,
# improve security and keep API
# responses consistent.


# ==========================================================
# COMMON BEGINNER MISTAKE
# ==========================================================

# ❌ Returning ComplaintModel directly.
#
# This may expose sensitive or
# unnecessary database fields.
#
# -----------------------------
#
# ✅ Return ComplaintResponse
#
# Only required fields are sent
# to the frontend.


# ==========================================================
# RELATED CONCEPTS
# ==========================================================

# ComplaintModel
#
#        ↓
#
# Repository
#
#        ↓
#
# Router
#
#        ↓
#
# ComplaintResponse
#
#        ↓
#
# JSON Response


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Model = Database Table
#
# ✔ Response Model = API Output
#
# ✔ response_model filters output
#
# ✔ Never expose Database Model directly.
#
# ✔ Return only required fields.