"""
=========================================
PHASE 2

TOPIC : QUERY PARAMETERS
=========================================

USED IN

app/routers/

"""

# WHY?
# Used to Filter, Sort,
# Search and Paginate data.

# CIVIL AI IMPLEMENTATION


@router.get("/complaints")
def get_complaints(ward: int, status: str):
    return {}


# Example URL

# /complaints?ward=152&status=Pending

# CONCEPT

# ? starts Query Parameters

# ward=152

# status=Pending

# Used for filtering data.

# INTERNAL FLOW

# GET /complaints

# ?ward=152

# &status=Pending

# ↓

# Router

# ↓

# Filter Data

# ↓

# Response

# INTERVIEW

# Q: When do we use Query Parameters?
#
# A:
# To filter, search, sort,
# or paginate data.

# COMMON BEGINNER MISTAKE

# ❌ Using Path Parameters
# for Filtering.

# ✅ Use Query Parameters
# for Filters.

# RELATED CONCEPTS

# Filtering

# Sorting

# Pagination

# REMEMBER

# ✔ Optional Values
# ✔ Used for Filtering
# ✔ Used for Sorting
# ✔ Used for Pagination
