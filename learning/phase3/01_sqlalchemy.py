"""
=========================================
PHASE 3

TOPIC : SQLALCHEMY
=========================================

USED IN

app/models/
app/repositories/
app/database.py

"""

# WHY?
# SQLAlchemy lets Python communicate
# with the Database using ORM.

# CIVIL AI IMPLEMENTATION

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

# CONCEPT

# SQLAlchemy

# ↓

# Python Code

# ↓

# SQL Query

# ↓

# Database

# INTERVIEW

# Q: What is SQLAlchemy?
#
# A:
# SQLAlchemy is a Python ORM
# used to interact with databases.

# COMMON BEGINNER MISTAKE

# ❌ Writing raw SQL
# for every operation.

# ✅ Use SQLAlchemy ORM.

# RELATED CONCEPTS

# ORM

# CRUD

# Database Session

# REMEMBER

# ✔ ORM Library
# ✔ Converts Python → SQL
# ✔ Supports Multiple Databases
