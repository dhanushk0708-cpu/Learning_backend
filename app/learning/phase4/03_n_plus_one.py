"""
=========================================================

PHASE 4

TOPIC : N+1 PROBLEM

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
N+1 occurs while fetching related data
(User, Ward, Officer, etc.) inside Repository queries.

=========================================================
"""

from sqlalchemy.orm import joinedload

# ==========================================================
# WHY?
# ==========================================================

# N+1 Problem happens when we fetch a list of records
# and then execute one extra query for each record.

# 1 Query + N Queries = N+1 Problem


# ==========================================================
# BAD WAY
# ==========================================================

complaints = db.query(ComplaintModel).all()

for complaint in complaints:
    print(complaint.user.name)

# ----------------------------------------------------------
# CONCEPT : N+1 Problem
#
# Query 1 -> Fetch Complaints
#
# Query 2 -> User for Complaint 1
# Query 3 -> User for Complaint 2
# Query 4 -> User for Complaint 3
#
# 1000 complaints = 1001 queries
# ----------------------------------------------------------


# ==========================================================
# GOOD WAY
# ==========================================================

complaints = db.query(ComplaintModel).options(joinedload(ComplaintModel.user)).all()

# ----------------------------------------------------------
# CONCEPT : joinedload()
#
# Load Complaint and User together.
#
# Prevents N+1 Problem.
#
# Fewer database queries.
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
# JOIN Complaint + User
#   ↓
# One Optimized Query
#   ↓
# JSON Response


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: What is the N+1 Problem?
#
# A:
# N+1 happens when one query fetches a list
# and another query runs for every item in that list.
# It is solved using JOINs or Eager Loading.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Avoid querying inside loops.
# ✔ Use joinedload() when related data is needed.
# ✔ Reduces database round trips.
