"""
=========================================
PHASE 3

TOPIC : ALEMBIC
=========================================

USED IN

Backend Project Root

"""

# WHY?
# Alembic manages database
# schema changes.

# CIVIL AI IMPLEMENTATION

alembic revision --autogenerate -m "Create Complaint Table"

alembic upgrade head

# CONCEPT

# Model Changed

# ↓

# Alembic detects changes

# ↓

# Migration File

# ↓

# Update Database

# SQL EQUIVALENT

# ALTER TABLE

# CREATE TABLE

# ADD COLUMN

# DROP COLUMN

# INTERVIEW

# Q: What is Alembic?
#
# A:
# Alembic is the migration tool
# used with SQLAlchemy.

# COMMON BEGINNER MISTAKE

# ❌ Editing database tables manually.

# ✅ Use Alembic Migrations.

# RELATED CONCEPTS

# SQLAlchemy

# Migrations

# REMEMBER

# ✔ Tracks schema changes
# ✔ Auto Generates Migration Files
# ✔ Updates Database