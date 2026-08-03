"""
=========================================================

PHASE 4

TOPIC : LAZY LOADING vs EAGER LOADING

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
Used while fetching related objects
(User, Ward, Officer).

=========================================================
"""

from sqlalchemy.orm import joinedload

# ==========================================================
# WHY?
# ==========================================================

# SQLAlchemy needs to know

# Should related data be loaded

# Immediately ?

# OR

# Only when requested ?


# ==========================================================
# LAZY LOADING
# ==========================================================

complaints = db.query(ComplaintModel).all()

# ------------------------------------------------------
# CONCEPT : Lazy Loading
#
# Only Complaint is loaded.
#
# User is NOT loaded yet.
# ------------------------------------------------------

for complaint in complaints:
    print(complaint.user.name)

# ------------------------------------------------------
# Accessing complaint.user
#
# SQLAlchemy sends another SQL query.
#
# This can create the N+1 Problem.
# ------------------------------------------------------


# ==========================================================
# EAGER LOADING
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # --------------------------------------------------
    # CONCEPT : joinedload()
    #
    # joinedload() is SQLAlchemy's
    # Eager Loading function.
    #
    # Complaint and User are loaded
    # together.
    # --------------------------------------------------
    .options(joinedload(ComplaintModel.user))
    .all()
)

# ------------------------------------------------------
# No extra query
#
# complaint.user.name
#
# already exists in memory.
# ------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Lazy

# Complaint
#     ↓
# Access User
#     ↓
# New Query


# Eager

# Complaint + User
#        ↓
# One Query
#        ↓
# Ready to Use


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Difference between Lazy and Eager Loading?
#
# A:
# Lazy Loading fetches related data only
# when accessed.
#
# Eager Loading fetches related data
# immediately, reducing database queries.


# ==========================================================
# REMEMBER
# ==========================================================

# Lazy
# ✔ Less Initial Data
# ❌ Can create N+1

# Eager
# ✔ Fewer Queries
# ✔ Better for Lists
# ❌ Don't use if related data isn't needed.
