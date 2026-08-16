"""
=========================================
PHASE 2

TOPIC : PROJECT STRUCTURE
=========================================

USED IN

Entire FastAPI Project

"""

# WHY?
# Organize code into separate folders.
# Easy to maintain and scale.

# PROJECT STRUCTURE

# app/
#
# ├── routers/
# ├── models/
# ├── schemas/
# ├── repositories/
# ├── database.py
# └── main.py

# CONCEPT

# routers      -> API Endpoints
# models       -> Database Tables
# schemas      -> Request & Response Validation
# repositories -> Database Queries
# main.py      -> Starts FastAPI Application

# INTERVIEW

# Q: Why do we organize a project into folders?
#
# A:
# To improve maintainability,
# scalability and readability.

# COMMON BEGINNER MISTAKE

# ❌ Keeping every file inside main.py

# ✅ Separate responsibilities into
# different folders.

# RELATED CONCEPTS

# Project Structure
#
# ↓
#
# Repository Pattern (Phase 4)

# REMEMBER

# ✔ One Responsibility per Folder
# ✔ Easy to Maintain
# ✔ Easy to Scale
