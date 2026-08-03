"""
=========================================================

PHASE 4

TOPIC : AGGREGATION

=========================================================

REAL PROJECT FILE

app/repositories/dashboard_repository.py

Reason:
Dashboards and analytics need counts,
averages and summaries.

=========================================================
"""

from sqlalchemy import func

# ==========================================================
# WHY?
# ==========================================================

# Aggregation summarizes data.

# Instead of returning every complaint,
# return useful information like:

# Total Complaints
# Pending Complaints
# Resolved Complaints


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

complaint_count = db.query(func.count(ComplaintModel.id)).scalar()

# ----------------------------------------------------------
# CONCEPT : COUNT()
#
# Database counts records.
#
# No need to count manually in Python.
# ----------------------------------------------------------


# ==========================================================
# GROUP BY EXAMPLE
# ==========================================================

ward_counts = (
    db.query(ComplaintModel.ward_id, func.count(ComplaintModel.id))
    .group_by(ComplaintModel.ward_id)
    .all()
)

# ----------------------------------------------------------
# CONCEPT : GROUP BY
#
# Group complaints by ward.
#
# Count complaints in each ward.
# ----------------------------------------------------------


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Mayor Dashboard
#      ↓
# Repository
#      ↓
# COUNT()
# GROUP BY
#      ↓
# Database
#      ↓
# Dashboard Statistics


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: What is Aggregation?
#
# A:
# Aggregation combines multiple rows into
# summary values using functions like
# COUNT(), SUM(), AVG(), MIN() and MAX().


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ COUNT() → Total Records
# ✔ SUM() → Total Values
# ✔ AVG() → Average
# ✔ GROUP BY → Group Similar Records
# ✔ Let the database perform aggregation.
