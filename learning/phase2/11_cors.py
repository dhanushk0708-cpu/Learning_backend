"""
=========================================
PHASE 2

TOPIC : CORS
=========================================

USED IN

app/main.py

"""

# WHY?
# Allows React Frontend
# to communicate with
# FastAPI Backend.

# CIVIL AI IMPLEMENTATION

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CONCEPT

# Browser

# ↓

# Checks CORS Policy

# ↓

# Allowed ?

# YES → Request Continues

# NO  → Browser Blocks Request

# INTERVIEW

# Q: What is CORS?
#
# A:
# CORS (Cross-Origin Resource Sharing)
# allows or blocks requests between
# different origins.

# COMMON BEGINNER MISTAKE

# ❌ Thinking FastAPI blocked the request.

# ✅ Browser blocks the request
# if CORS isn't configured.

# RELATED CONCEPTS

# React

# ↓ HTTP Request

# FastAPI

# REMEMBER

# ✔ Configured in main.py
# ✔ Required for React + FastAPI
# ✔ Browser enforces CORS
