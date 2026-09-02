"""
=========================================
PHASE 3

TOPIC : MIGRATIONS
=========================================

USED IN

alembic/versions/

"""

# WHY?
# Migrations keep the Database
# schema synchronized with Models.

# CIVIL AI IMPLEMENTATION

alembic revision --autogenerate -m "Add Status Column"

alembic upgrade head

# CONCEPT

# Model Updated

# ↓

# Migration File Created

# ↓

# Database Updated

# SQL EQUIVALENT

# ALTER TABLE complaints

# ADD COLUMN status VARCHAR(50);

# INTERVIEW

# Q: What is a Migration?
#
# A:
# A Migration records database
# schema changes and applies
# them safely.

# COMMON BEGINNER MISTAKE

# ❌ Changing Models but
# forgetting to migrate.

# ✅ Generate and Apply Migration.

# RELATED CONCEPTS

# Alembic

# Models

# Database

# REMEMBER

# ✔ Model Change → Migration
# ✔ Migration → Database Update
# ✔ Keep Model & DB in Sync