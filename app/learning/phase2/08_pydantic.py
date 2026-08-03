"""
=========================================
PHASE 2

TOPIC : PYDANTIC
=========================================

USED IN

app/schemas/

"""

# WHY?
# Pydantic validates
# Request and Response data.

# CIVIL AI IMPLEMENTATION

from pydantic import BaseModel


class ComplaintCreate(BaseModel):
    title: str

    description: str

    ward_id: int


# CONCEPT

# BaseModel

# ↓

# Creates a Schema

# ↓

# Validates JSON

# ↓

# Converts JSON
# into Python Object

# INTERNAL FLOW

# JSON

# ↓

# Pydantic

# ↓

# Python Object

# ↓

# Router

# INTERVIEW

# Q: What is Pydantic?
#
# A:
# Pydantic is a data validation
# library used by FastAPI
# to validate and convert data.

# COMMON BEGINNER MISTAKE

# ❌ Accepting raw JSON everywhere.

# ✅ Use Pydantic Schemas.

# RELATED CONCEPTS

# Request Body

# Response Model

# Validation

# REMEMBER

# ✔ Uses BaseModel
# ✔ Validates Data
# ✔ Converts JSON → Python Object

# NOTE

# Basic Concept -> Phase 2

# Advanced Response Models -> Phase 4
