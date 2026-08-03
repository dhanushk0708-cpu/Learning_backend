"""
=========================================================

PHASE 4

TOPIC : FILTERING

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
Filtering is used whenever the frontend
needs only specific data from the database.

Example:
Ward = 152
Status = Pending

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Instead of loading every complaint,
# let the database return only
# the required complaints.

# Database does the filtering.
# Not Python.


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT : FILTERING
    #
    # Return only complaints
    # from Ward 152.
    # ------------------------------------------------------
    .filter(ComplaintModel.ward_id == 152)
    .all()
)

# ==========================================================
# MULTIPLE FILTERS
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT :
    #
    # Multiple filters can be
    # applied together.
    # ------------------------------------------------------
    .filter(ComplaintModel.ward_id == 152, ComplaintModel.status == "Pending")
    .all()
)

# ----------------------------------------------------------
# SQL Equivalent
#
# WHERE ward_id = 152
# AND status = 'Pending'
# ----------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Browser
#     ↓
# GET /complaints?ward=152&status=Pending
#     ↓
# Repository
#     ↓
# WHERE ward_id = 152
# AND status = Pending
#     ↓
# Database
#     ↓
# Return Matching Complaints


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why should filtering happen
# in the database instead of Python?
#
# A:
# Databases are optimized for filtering.
# It reduces memory usage,
# network transfer and API response time.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Filter in Database
# ✔ Not in Python
# ✔ Frequently filtered columns
#    should have Indexes
# ✔ Filtering usually happens
#    before Sorting and Pagination
