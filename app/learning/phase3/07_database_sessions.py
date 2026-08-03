"""
=========================================
PHASE 3

TOPIC : DATABASE SESSIONS
=========================================

USED IN

app/database.py

"""

# WHY?
# Database Session manages communication
# between FastAPI and the Database.

# CIVIL AI IMPLEMENTATION


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# CONCEPT

# Session

# ↓

# Execute Queries

# ↓

# Commit / Rollback

# ↓

# Close Session

# SQL EQUIVALENT

# OPEN CONNECTION

# Execute SQL

# CLOSE CONNECTION

# INTERVIEW

# Q: What is a Database Session?
#
# A:
# A Database Session manages
# database operations during
# one request.

# COMMON BEGINNER MISTAKE

# ❌ Forgetting db.close()

# ✅ Always close the Session.

# RELATED CONCEPTS

# Dependency Injection

# Connection Pool

# REMEMBER

# ✔ Session executes queries
# ✔ One Session per Request
# ✔ Always close Session
