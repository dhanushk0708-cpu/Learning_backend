"""
=========================================
PHASE 3

TOPIC : ORM
=========================================

USED IN

app/models/

"""

# WHY?
# ORM maps Python Classes
# to Database Tables.

# CIVIL AI IMPLEMENTATION


class ComplaintModel(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)

    title = Column(String)


# CONCEPT

# Python Class

# ↓

# Database Table

# INTERVIEW

# Q: What is ORM?
#
# A:
# ORM (Object Relational Mapping)
# maps Python Objects
# to Database Tables.

# COMMON BEGINNER MISTAKE

# ❌ Thinking ORM stores data.

# ✅ Database stores data.
# ORM is only a bridge.

# RELATED CONCEPTS

# SQLAlchemy

# Models

# Tables

# REMEMBER

# ✔ Class → Table
# ✔ Object → Row
# ✔ Attribute → Column
