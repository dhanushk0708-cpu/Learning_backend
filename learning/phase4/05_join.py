"""
=========================================================

PHASE 4

TOPIC : JOIN

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
JOIN is used whenever data comes from
multiple database tables.

Example:
Complaint + Citizen + Ward

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# JOIN combines data from multiple tables
# into a single query.

# Without JOIN
# Complaint -> User -> Ward
# Multiple Queries

# With JOIN
# One Optimized Query


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

complaints = (
    db.query(ComplaintModel.title, UserModel.name, WardModel.name)
    # ------------------------------------------------------
    # CONCEPT : JOIN
    #
    # Join Complaint table with User table.
    #
    # complaint.citizen_id == user.id
    # ------------------------------------------------------
    .join(UserModel, ComplaintModel.citizen_id == UserModel.id)
    # ------------------------------------------------------
    # CONCEPT : JOIN
    #
    # Join Complaint table with Ward table.
    #
    # complaint.ward_id == ward.id
    # ------------------------------------------------------
    .join(WardModel, ComplaintModel.ward_id == WardModel.id)
    .all()
)

# ==========================================================
# INTERNAL FLOW
# ==========================================================

# React
#    ↓
# GET /complaints
#    ↓
# Repository
#    ↓
# JOIN Complaint + User + Ward
#    ↓
# Database
#    ↓
# One Query
#    ↓
# JSON Response


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why do we use JOIN?
#
# A:
# JOIN combines related data from multiple
# tables using Primary Key and Foreign Key
# relationships in a single query.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ One Query
# ✔ Better Performance
# ✔ Avoid N+1 Problem
# ✔ Uses Primary Key & Foreign Key
