"""
=========================================
PHASE 1

TOPIC : JSON
=========================================

USED IN

React ↔ FastAPI

API Request & Response

"""

# WHY?
# JSON is the standard format used
# to exchange data between
# Client and Server.

# JSON EXAMPLE

# Request

{"title": "Road Damage", "ward_id": 152}

# Response

{"id": 1, "title": "Road Damage", "status": "Pending"}

# CIVIL AI FLOW

# React

# ↓ JSON Request

# FastAPI

# ↓ Python Object

# Process Request

# ↓ Python Object

# JSON Response

# ↓

# React

# INTERVIEW

# Q: What is JSON?
#
# A:
# JSON (JavaScript Object Notation)
# is a lightweight format used
# to exchange data between
# Client and Server.

# REMEMBER

# ✔ JSON = Data Exchange Format
# ✔ Request Body is usually JSON
# ✔ Response Body is usually JSON
# ✔ FastAPI automatically converts
#    JSON ↔ Python Objects
