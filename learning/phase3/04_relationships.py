"""
=========================================
PHASE 3

TOPIC : RELATIONSHIPS
=========================================

USED IN

app/models/

"""

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# WHY?
# Relationships connect
# multiple database tables.

# CIVIL AI IMPLEMENTATION


class ComplaintModel(Base):
    citizen_id = Column(Integer, ForeignKey("citizens.id"))

    citizen = relationship("CitizenModel")


# CONCEPT

# ForeignKey

# ↓

# Connects Tables

# ↓

# relationship()

# Access Related Data

# INTERNAL FLOW

# Complaint

# ↓ citizen_id

# Citizen Table

# ↓

# Citizen Object

# INTERVIEW

# Q: Why do we use Relationships?
#
# A:
# Relationships connect related
# tables and allow easy access
# to related data.

# COMMON BEGINNER MISTAKE

# ❌ Creating duplicate data
# in multiple tables.

# ✅ Use Foreign Keys and Relationships.

# RELATED CONCEPTS

# Foreign Key

# JOIN

# Lazy Loading

# Eager Loading

# REMEMBER

# ✔ ForeignKey connects tables.
# ✔ relationship() accesses related data.
# ✔ One-to-One
# ✔ One-to-Many
# ✔ Many-to-Many
