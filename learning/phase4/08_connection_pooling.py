"""
=========================================================

PHASE 4

TOPIC : CONNECTION POOLING

=========================================================

REAL PROJECT FILE

app/database.py

Reason:
The SQLAlchemy Engine creates and manages
the Connection Pool.

=========================================================
"""

from sqlalchemy import create_engine

# ==========================================================
# WHY?
# ==========================================================

# Opening a new database connection
# for every request is expensive.
#
# Connection Pool reuses existing
# database connections.


# ==========================================================
# CIVIL AI IMPLEMENTATION
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    # ------------------------------------------------------
    # CONCEPT : pool_size
    #
    # Keep 20 database connections
    # ready for reuse.
    # ------------------------------------------------------
    pool_size=20,
    # ------------------------------------------------------
    # CONCEPT : max_overflow
    #
    # If all 20 connections are busy,
    # SQLAlchemy can temporarily create
    # 10 extra connections.
    #
    # Maximum Connections = 30
    # ------------------------------------------------------
    max_overflow=10,
)

# ==========================================================
# get_db()
# File : app/database.py
# ==========================================================


def get_db():

    # ------------------------------------------------------
    # CONCEPT : Session
    #
    # Session borrows one connection
    # from the Connection Pool.
    # ------------------------------------------------------
    db = SessionLocal()

    try:
        yield db

    finally:
        # --------------------------------------------------
        # CONCEPT : db.close()
        #
        # Returns the connection back
        # to the pool.
        #
        # It DOES NOT destroy
        # the connection.
        # --------------------------------------------------
        db.close()


# ==========================================================
# INTERNAL FLOW
# ==========================================================

# Request
#    ↓
# SessionLocal()
#    ↓
# Connection Pool
#    ↓
# Database Connection
#    ↓
# Query
#    ↓
# db.close()
#    ↓
# Connection returned to Pool


# ==========================================================
# INTERVIEW
# ==========================================================

# Q: What is Connection Pooling?
#
# A:
# Connection Pooling reuses existing
# database connections instead of creating
# a new one for every request,
# improving performance.


# ==========================================================
# REMEMBER
# ==========================================================

# ✔ Engine owns Connection Pool
# ✔ Session uses a Connection
# ✔ db.close() returns connection to Pool
# ✔ Reusing connections is faster than creating new ones
