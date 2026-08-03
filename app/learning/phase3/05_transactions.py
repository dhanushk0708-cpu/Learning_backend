"""
=========================================
PHASE 3

TOPIC : TRANSACTIONS
=========================================

USED IN

app/repositories/

"""

# WHY?
# A Transaction ensures that
# multiple database operations
# succeed together or fail together.

# CIVIL AI IMPLEMENTATION

try:
    db.add(complaint)

    db.commit()

except:
    db.rollback()

# CONCEPT

# commit()

# ↓

# Save Changes

# rollback()

# ↓

# Undo Changes

# SQL EQUIVALENT

# BEGIN;

# INSERT ...

# UPDATE ...

# COMMIT;

# OR

# ROLLBACK;

# INTERVIEW

# Q: Why do we use Transactions?
#
# A:
# To maintain data consistency.
# If one operation fails,
# all changes are rolled back.

# COMMON BEGINNER MISTAKE

# ❌ Forgetting rollback()
# after an error.

# ✅ Use rollback() when
# a transaction fails.

# RELATED CONCEPTS

# CRUD

# commit()

# rollback()

# REMEMBER

# ✔ commit() saves changes
# ✔ rollback() undoes changes
# ✔ Maintains data consistency
