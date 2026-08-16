"""
=========================================
PHASE 3

TOPIC : CONSTRAINTS
=========================================

USED IN

app/models/

"""

from sqlalchemy import Column, Integer, String

# WHY?
# Constraints enforce rules
# on database data.

# CIVIL AI IMPLEMENTATION

id = Column(Integer, primary_key=True)

email = Column(String, unique=True, nullable=False)

# CONCEPT

# primary_key=True

# Unique Identifier

# unique=True

# No Duplicate Values

# nullable=False

# Value is Required

# SQL EQUIVALENT

# PRIMARY KEY

# UNIQUE

# NOT NULL

# INTERVIEW

# Q: What are Constraints?
#
# A:
# Constraints enforce rules
# to keep data valid and consistent.

# COMMON BEGINNER MISTAKE

# ❌ Depending only on
# frontend validation.

# ✅ Database should also
# enforce constraints.

# RELATED CONCEPTS

# Primary Key

# Foreign Key

# Validation

# REMEMBER

# ✔ PRIMARY KEY
# ✔ FOREIGN KEY
# ✔ UNIQUE
# ✔ NOT NULL
