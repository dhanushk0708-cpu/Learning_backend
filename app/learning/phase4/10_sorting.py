"""
=========================================================

PHASE 4

TOPIC : SORTING

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
Sorting arranges the data before
sending it to the frontend.

Examples

Newest Complaints

Highest Priority

Oldest Complaints

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Sorting arranges records
# in a specific order.

# Database performs sorting.
# Not Python.


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT : DESCENDING ORDER
    #
    # created_at.desc()
    #
    # Returns
    # Newest Complaints First
    # ------------------------------------------------------
    .order_by(ComplaintModel.created_at.desc())
    .all()
)

# ==========================================================
# ASCENDING ORDER
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT : ASCENDING ORDER
    #
    # Returns
    # Oldest Complaints First
    # ------------------------------------------------------
    .order_by(ComplaintModel.created_at.asc())
    .all()
)


# ==========================================================
# FILTER + SORT + PAGINATION
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # Filter first
    .filter(ComplaintModel.ward_id == 152, ComplaintModel.status == "Pending")
    # Then Sort
    .order_by(ComplaintModel.created_at.desc())
    # Finally Pagination
    .limit(20)
    .offset(0)
    .all()
)

# ------------------------------------------------------
# CONCEPT
#
# Production APIs usually combine
#
# Filtering
# +
# Sorting
# +
# Pagination
#
# in ONE query.
# ------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Browser
#      ↓
# GET /complaints
# ?ward=152
# &status=Pending
# &sort=-created_at
# &page=1
#
#      ↓
#
# Repository
#
#      ↓
#
# Filter
#
#      ↓
#
# Sort
#
#      ↓
#
# Pagination
#
#      ↓
#
# Database
#
#      ↓
#
# JSON Response


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why should sorting happen
# inside the database?
#
# A:
# Databases are optimized to sort
# large datasets efficiently.
#
# Sorting inside Python increases
# memory usage and processing time.


# ==========================================================
# RELATED CONCEPTS
# ==========================================================

# Sorting
#
# ↓ Uses
#
# Indexes
#
# ↓ Combined With
#
# Filtering
#
# ↓ Combined With
#
# Pagination
#
# ↓ Result
#
# Faster API


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ asc()  -> Oldest First
#
# ✔ desc() -> Newest First
#
# ✔ Sort in Database
#
# ✔ Filter before Sorting
#
# ✔ Pagination after Sorting
#
# ✔ Frequently sorted columns
#    should have Indexes.
