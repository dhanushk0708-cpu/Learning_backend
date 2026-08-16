"""
=========================================================

PHASE 4

TOPIC : PAGINATION

=========================================================

REAL PROJECT FILE

app/repositories/complaint_repository.py

Reason:
Used when returning large amounts of data.
Instead of returning all rows,
return only the required rows.

=========================================================
"""

# ==========================================================
# WHY?
# ==========================================================

# Pagination returns data in small chunks.
#
# Instead of:
# 100000 complaints
#
# Return:
# First 20 complaints


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT : OFFSET
    #
    # Skip previous records.
    #
    # Example:
    # Page 3
    #
    # Skip first 40 records.
    # ------------------------------------------------------
    .offset(40)
    # ------------------------------------------------------
    # CONCEPT : LIMIT
    #
    # Return only 20 records.
    # ------------------------------------------------------
    .limit(20)
    .all()
)

# ==========================================================
# CURSOR PAGINATION
# ==========================================================

complaints = (
    db.query(ComplaintModel)
    # ------------------------------------------------------
    # CONCEPT : Cursor Pagination
    #
    # Instead of skipping rows,
    # continue after the last record.
    #
    # Example:
    # Last Complaint ID = 500
    #
    # Return complaints after ID 500.
    # ------------------------------------------------------
    .filter(ComplaintModel.id > 500)
    .limit(20)
    .all()
)

# ----------------------------------------------------------
# CONCEPT
#
# Cursor Pagination doesn't skip
# millions of rows like OFFSET.
#
# It continues from the last record.
#
# Better Performance for
# Infinite Scrolling.
# ----------------------------------------------------------


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Why do we use Pagination?
#
# A:
# Pagination improves performance by
# returning only the required records
# instead of the entire dataset.

# ==========================================================
# INTERNAL FLOW
# ==========================================================

# OFFSET PAGINATION
#
# Browser
#    ↓
# GET /complaints?page=3
#    ↓
# OFFSET 40
# LIMIT 20
#    ↓
# Database
#    ↓
# Return 20 Rows


# CURSOR PAGINATION
#
# Browser
#    ↓
# GET /complaints?last_id=500
#    ↓
# WHERE id > 500
# LIMIT 20
#    ↓
# Database
#    ↓
# Return Next 20 Rows


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ LIMIT -> Number of rows
# ✔ OFFSET -> Skip previous rows
# ✔ Best for Admin Dashboards
# ✔ Cursor Pagination is better for Infinite Scroll
# ==========================================================
# INTERVIEW
# ==========================================================

# Q: Difference between OFFSET and Cursor Pagination?
#
# A:
# OFFSET Pagination skips previous rows
# using OFFSET and LIMIT.
#
# Cursor Pagination continues from the
# last retrieved record using a cursor
# like id or created_at.
#
# Cursor Pagination is more efficient
# for very large datasets and
# Infinite Scrolling.

# ==========================================================
# REMEMBER
# ==========================================================

# OFFSET Pagination
#
# ✔ Easy to Implement
# ✔ Good for Admin Dashboards
# ❌ Slower on Large Datasets


# Cursor Pagination
#
# ✔ Very Fast
# ✔ Best for Infinite Scroll
# ✔ Doesn't Skip Millions of Rows
# ✔ Uses id or created_at as Cursor
