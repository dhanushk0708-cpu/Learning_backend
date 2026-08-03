"""
=========================================
PHASE 2

TOPIC : VALIDATION
=========================================

USED IN

app/schemas/
app/routers/

"""

# WHY?
# Validation checks whether
# incoming data is correct
# before executing the API.

# CIVIL AI IMPLEMENTATION


class ComplaintCreate(BaseModel):
    title: str
    ward_id: int


@router.post("/complaints")
def create_complaint(complaint: ComplaintCreate):
    return complaint


# CONCEPT

# title must be String

# ward_id must be Integer

# Invalid data

# ↓

# FastAPI returns Validation Error

# INTERNAL FLOW

# React

# ↓ JSON

# FastAPI

# ↓ Validation

# Valid ?
#
# YES → Router
#
# NO  → 422 Error

# INTERVIEW

# Q: Why do we use Validation?
#
# A:
# To ensure only valid data
# enters the application.

# COMMON BEGINNER MISTAKE

# ❌ Trusting user input.

# ✅ Always validate input.

# RELATED CONCEPTS

# JSON

# ↓

# Pydantic

# ↓

# Validation

# REMEMBER

# ✔ Prevents Invalid Data
# ✔ Runs Before Router
# ✔ Returns 422 if Validation Fails
