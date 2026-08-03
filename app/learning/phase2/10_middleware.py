"""
=========================================
PHASE 2

TOPIC : MIDDLEWARE
=========================================

USED IN

app/main.py

"""

# WHY?
# Middleware runs before and
# after every request.

# CIVIL AI IMPLEMENTATION


@app.middleware("http")
async def log_requests(request, call_next):

    response = await call_next(request)

    return response


# CONCEPT

# Request

# ↓

# Middleware

# ↓

# Router

# ↓

# Response

# ↓

# Middleware

# ↓

# Client

# INTERNAL FLOW

# Browser

# ↓

# Middleware

# ↓

# Router

# ↓

# Database

# ↓

# Router

# ↓

# Middleware

# ↓

# Browser

# INTERVIEW

# Q: What is Middleware?
#
# A:
# Middleware intercepts every
# request and response to perform
# common tasks.

# COMMON USES

# ✔ Logging
# ✔ Authentication
# ✔ CORS
# ✔ Request Timing

# COMMON BEGINNER MISTAKE

# ❌ Writing the same logging code
# in every API.

# ✅ Use Middleware once.

# RELATED CONCEPTS

# Request

# ↓

# Middleware

# ↓

# Router

# REMEMBER

# ✔ Runs Before Router
# ✔ Runs After Router
# ✔ Executes for Every Request
