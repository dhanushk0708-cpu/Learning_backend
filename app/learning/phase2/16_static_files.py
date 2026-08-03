"""
=========================================
PHASE 2

TOPIC : STATIC FILES
=========================================

USED IN

app/main.py

"""

from fastapi.staticfiles import StaticFiles

# WHY?
# Serve static files like

# Images
# CSS
# JavaScript

# CIVIL AI IMPLEMENTATION

app.mount("/static", StaticFiles(directory="static"), name="static")

# CONCEPT

# Browser

# ↓

# /static/logo.png

# ↓

# FastAPI

# ↓

# Returns File

# INTERNAL FLOW

# Browser

# ↓

# Static Request

# ↓

# FastAPI

# ↓

# Static Folder

# ↓

# Response

# INTERVIEW

# Q: What are Static Files?
#
# A:
# Files served directly by
# the server without processing.

# COMMON BEGINNER MISTAKE

# ❌ Returning images
# from API code.

# ✅ Serve them
# using StaticFiles.

# RELATED CONCEPTS

# Browser

# ↓

# StaticFiles

# ↓

# Image / CSS / JS

# REMEMBER

# ✔ app.mount()
# ✔ StaticFiles
# ✔ Used for Images & Assets
