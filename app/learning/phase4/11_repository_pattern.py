"""
=========================================================

PHASE 4

TOPIC : REPOSITORY PATTERN

=========================================================

REAL PROJECT FILES

app/repositories/complaint_repository.py

app/routers/complaint_router.py

Reason:
Repository Pattern separates database logic
from Router logic.

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Router should handle HTTP Requests.
#
# Repository should handle Database Queries.
#
# This follows SRP (Single Responsibility Principle).


# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

# app/
#
# ├── routers/
# │      complaint_router.py
# │
# ├── repositories/
# │      complaint_repository.py
# │
# ├── models/
# │
# └── schemas/


# ==========================================================
# ROUTER
# File : app/routers/complaint_router.py
# ==========================================================


@router.get("/complaints")
def get_complaints(db: Session = Depends(get_db)):

    # ------------------------------------------------------
    # CONCEPT : Repository Pattern
    #
    # Router doesn't know SQLAlchemy.
    #
    # Router simply calls Repository.
    # ------------------------------------------------------

    return complaint_repository.get_all(db)


# ==========================================================
# REPOSITORY
# File : app/repositories/complaint_repository.py
# ==========================================================


def get_all(db: Session):

    return db.query(ComplaintModel).all()


# ------------------------------------------------------
# CONCEPT
#
# Repository is responsible for
# talking to the database.
#
# Router never writes SQL Queries.
# ------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Browser
#      ↓
# GET /complaints
#      ↓
# Router
#      ↓
# Repository
#      ↓
# SQLAlchemy
#      ↓
# Database
#      ↓
# Repository
#      ↓
# Router
#      ↓
# JSON Response


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why do we use Repository Pattern?
#
# A:
# Repository Pattern separates database
# logic from request handling.
#
# It improves maintainability,
# reusability and scalability.


# ==========================================================
# COMMON BEGINNER MISTAKE
# ==========================================================

# ❌ Writing SQL Queries inside Router.
#
# @router.get("/complaints")
#
#     db.query(...)
#
# -----------------------------
#
# ✅ Router
#
#     complaint_repository.get_all(db)
#
# Repository
#
#     db.query(...)


# ==========================================================
# RELATED CONCEPTS
# ==========================================================

# Router
#
# ↓ Calls
#
# Repository
#
# ↓ Uses
#
# SQLAlchemy
#
# ↓ Talks To
#
# Database


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Router handles HTTP Requests.
#
# ✔ Repository handles Database Queries.
#
# ✔ Better Code Organization.
#
# ✔ Easy to Maintain.
#
# ✔ Easy to Reuse.
