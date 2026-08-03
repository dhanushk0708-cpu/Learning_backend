"""
PHASE 4

TOPIC : INDEXES
"""

# ==========================================================
# WHY?
# ==========================================================
# Index helps the database find rows faster.
# Without an index, the database scans every row
# (Full Table Scan).

# ==========================================================
# WHERE DO WE USE IT?
# ==========================================================
# Frequently searched columns
# Frequently sorted columns
# Foreign Keys

# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

from sqlalchemy import Column, Integer


class ComplaintModel(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)

    # ------------------------------------------------------
    # CONCEPT : INDEX
    # Citizens frequently search by ward.
    # SQLAlchemy tells the database to create an index.
    # Database uses it to find matching rows faster.
    # ------------------------------------------------------
    ward_id = Column(Integer, index=True)


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# GET /complaints?ward=152
#
# Browser
#   ↓
# FastAPI
#   ↓
# Repository
#   ↓
# SQLAlchemy
#   ↓
# Database
#   ↓
# Index
#   ↓
# Fast Result

# ==========================================================
# INTERVIEW
# ==========================================================

# Q: What is an Index?
#
# A:
# An Index is a database data structure that helps
# retrieve rows faster without scanning the entire table.

# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Good for WHERE
# ✔ Good for ORDER BY
# ✔ Good for JOIN
#
# ❌ Don't create indexes on every column.
