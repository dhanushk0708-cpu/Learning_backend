"""
=========================================
PHASE 1

TOPIC : HTTP STATUS CODES
=========================================

USED IN

Every API Response

"""

# WHY?
# Status Codes tell the client
# whether the request was successful
# or failed.

# COMMON STATUS CODES

# 200 -> OK
# 201 -> Created
# 400 -> Bad Request
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Not Found
# 500 -> Internal Server Error

# CIVIL AI FLOW

# React
#
# ↓ Request
#
# FastAPI
#
# ↓
#
# 200 / 404 / 500
#
# ↓
#
# React

# INTERVIEW

# Q: Why are Status Codes important?
#
# A:
# They tell the client the result
# of the request.

# REMEMBER

# ✔ 2xx -> Success
# ✔ 4xx -> Client Error
# ✔ 5xx -> Server Error
