"""
=========================================
PHASE 2

TOPIC : ROUTING
=========================================

USED IN

app/routers/

"""

# WHY?
# Routing connects a URL
# to a Python Function.

# CIVIL AI IMPLEMENTATION


@router.get("/complaints")
def get_complaints():
    return {"message": "Success"}


# CONCEPT

# @router.get()
# Registers a GET Endpoint.

# "/complaints"
# URL Path

# get_complaints()
# Executes when endpoint is called.

# INTERNAL FLOW

# Browser

# ↓

# GET /complaints

# ↓

# Router

# ↓

# Python Function

# ↓

# Response

# INTERVIEW

# Q: What is Routing?
#
# A:
# Routing maps an incoming HTTP request
# to the appropriate function.

# COMMON BEGINNER MISTAKE

# ❌ Writing all APIs in one file.

# ✅ Split APIs into routers.

# RELATED CONCEPTS

# Client
#
# ↓
#
# HTTP Request
#
# ↓
#
# Router
#
# ↓
#
# Function

# REMEMBER

# ✔ URL → Function
# ✔ Router handles HTTP Requests
# ✔ Organize APIs using routers
