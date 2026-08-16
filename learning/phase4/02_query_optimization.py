"""
=========================================================

PHASE 4

TOPIC : QUERY OPTIMIZATION

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
Database queries are written inside the Repository.
Query optimization is applied here.

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Fetch only the data the frontend needs.
# Don't fetch unnecessary columns from the database.


# ==========================================================
# CIVIL AI IMPLEMENTATION
# File: app/repositories/complaint_repository.py
# ==========================================================

complaints = db.query(
    ComplaintModel.title, ComplaintModel.status, ComplaintModel.created_at
).all()

# ----------------------------------------------------------
# CONCEPT : Query Optimization
#
# Fetch only required columns.
#
# Don't use:
# db.query(ComplaintModel)
#
# if the frontend only needs
# title, status and created_at.
#
# Benefits:
# ✔ Less Memory
# ✔ Less Network Transfer
# ✔ Faster API
# ----------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# React
#   ↓
# GET /complaints
#   ↓
# Repository
#   ↓
# Fetch only:
# title
# status
# created_at
#   ↓
# JSON Response
#   ↓
# React


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: What is Query Optimization?
#
# A:
# Query Optimization means retrieving only the
# required data in the most efficient way
# to improve API performance.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Fetch only required columns.
# ✔ Avoid SELECT * in production.
# ✔ Less Data = Faster Response.
