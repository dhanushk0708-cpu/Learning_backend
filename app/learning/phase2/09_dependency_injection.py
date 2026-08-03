"""
=========================================
PHASE 2

TOPIC : DEPENDENCY INJECTION
=========================================

USED IN

app/database.py
app/routers/

"""

# WHY?
# Reuse common logic without
# writing it in every API.

# CIVIL AI IMPLEMENTATION


@router.get("/complaints")
def get_complaints(db: Session = Depends(get_db)): ...


# CONCEPT

# Depends(get_db)

# ↓

# FastAPI calls get_db()

# ↓

# Creates Database Session

# ↓

# Passes Session to Router

# INTERNAL FLOW

# Request

# ↓

# Depends(get_db)

# ↓

# Database Session

# ↓

# Router

# ↓

# Response

# INTERVIEW

# Q: What is Dependency Injection?
#
# A:
# Dependency Injection provides
# required objects (like a database
# session) automatically instead of
# creating them manually.

# COMMON BEGINNER MISTAKE

# ❌ Creating a new database
# connection inside every API.

# ✅ Use Depends(get_db).

# RELATED CONCEPTS

# get_db()

# ↓

# Database Session

# ↓

# Connection Pool

# REMEMBER

# ✔ Reusable
# ✔ Cleaner Code
# ✔ FastAPI manages dependencies
