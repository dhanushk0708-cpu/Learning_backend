"""
=========================================
PHASE 3

TOPIC : CRUD
=========================================

USED IN

app/repositories/

"""

# WHY?
# CRUD represents the four basic
# database operations.

# CIVIL AI IMPLEMENTATION

# CREATE

db.add(complaint)

# READ

db.query(ComplaintModel).all()

# UPDATE

complaint.status = "Resolved"

# DELETE

db.delete(complaint)

db.commit()

# CONCEPT

# C -> Create

# R -> Read

# U -> Update

# D -> Delete

# INTERVIEW

# Q: What is CRUD?
#
# A:
# CRUD represents the four basic
# operations performed on a database.

# COMMON BEGINNER MISTAKE

# ❌ Forgetting db.commit()
# after Create, Update and Delete.

# ✅ Always commit changes.

# RELATED CONCEPTS

# Repository

# ↓

# SQLAlchemy

# ↓

# Database

# REMEMBER

# ✔ Create -> add()
# ✔ Read -> query()
# ✔ Update -> modify + commit()
# ✔ Delete -> delete() + commit()
