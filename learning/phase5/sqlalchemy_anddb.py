
# ## 1. Database fundamentals

# ### Primary Key

# Uniquely identifies a row.

# ```text
# users
# id  username
# 1   dhanush
# 2   mohan
# ```

# `id` is the primary key.

# ### Foreign Key

# Connects one table to another.

# ```python
# owner_id: Mapped[int] = mapped_column(
#     ForeignKey("users.id")
# )
# ```

# Meaning:

# ```text
# users.id
#    ↑
#    │
# complaints.owner_id
# ```

# A complaint belongs to a user.

# ---

# # 2. ORM

# **ORM = Object Relational Mapping**

# It lets us work with database tables using Python objects.

# Instead of:

# ```sql
# SELECT * FROM users;
# ```

# we can write:

# ```python
# select(User)
# ```

# And instead of manually converting database rows into Python objects, SQLAlchemy ORM handles that mapping.

# ### Interview answer

# > SQLAlchemy ORM maps Python classes and objects to relational database tables and rows.

# ---

# # 3. SQLAlchemy `Base`

# ```python
# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#     pass
# ```

# Models inherit from it:

# ```python
# class User(Base):
#     __tablename__ = "users"
# ```

# `Base.metadata` contains information about the tables/models.

# This is also what Alembic uses:

# ```python
# target_metadata = Base.metadata
# ```

# ---

# # 4. Model definition

# ```python
# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(
#         primary_key=True
#     )

#     username: Mapped[str] = mapped_column()

#     password_hash: Mapped[str] = mapped_column()

#     role: Mapped[str] = mapped_column()
# ```

# Mental model:

# ```text
# Python class
#      ↓
# Database table

# Python attribute
#      ↓
# Database column
# ```

# ---

# # 5. Relationships

# User:

# ```python
# complaints: Mapped[list["Complaint"]] = relationship(
#     back_populates="owner"
# )
# ```

# Complaint:

# ```python
# owner_id: Mapped[int] = mapped_column(
#     ForeignKey("users.id")
# )

# owner: Mapped["User"] = relationship(
#     back_populates="complaints"
# )
# ```

# Now:

# ```python
# complaint.owner
# ```

# gives the `User`.

# And:

# ```python
# user.complaints
# ```

# gives the user's complaints.

# ### Remember

# ```text
# ForeignKey()
#     ↓
# Database-level connection

# relationship()
#     ↓
# Python-level object navigation
# ```

# ---

# # 6. Engine

# ```python
# engine = create_engine(
#     DATABASE_URL,
#     echo=True
# )
# ```

# The **Engine** manages communication/configuration with the database and connection pool.

# Think:

# ```text
# Application
#      ↓
# SQLAlchemy Engine
#      ↓
# Database
# ```

# ---

# # 7. Session

# ```python
# SessionLocal = sessionmaker(
#     bind=engine
# )
# ```

# Then:

# ```python
# db = SessionLocal()
# ```

# The `Session` is your **working area/unit of work** for database operations.

# You use it to:

# ```python
# db.add(...)
# db.get(...)
# db.execute(...)
# db.commit()
# db.rollback()
# ```

# ---

# # 8. `db.add()`

# ```python
# user = User(
#     username="dhanush",
#     password_hash="hash",
#     role="citizen"
# )

# db.add(user)
# ```

# `add()` tells SQLAlchemy:

# > Track this object as a pending database change.

# It doesn't mean the transaction is permanently committed.

# ---

# # 9. `commit()`

# ```python
# db.commit()
# ```

# Makes the transaction permanent.

# Typical:

# ```text
# db.add()
#    ↓
# db.commit()
# ```

# ---

# # 10. `rollback()`

# ```python
# db.rollback()
# ```

# Undo uncommitted changes in the current transaction.

# Example:

# ```text
# Add Complaint       ✅
# Add Assignment      ❌
#        ↓
#    rollback()
#        ↓
# Complaint undone
# ```

# ### Interview answer

# > A transaction provides atomicity: either all operations succeed and commit, or the failed transaction is rolled back.

# ---

# # 11. `refresh()`

# ```python
# db.commit()
# db.refresh(user)
# ```

# Reloads the object's current database state.

# Very commonly used when the DB generates an ID:

# ```python
# db.add(user)
# db.commit()
# db.refresh(user)

# print(user.id)
# ```

# ---

# # 12. `flush()`

# ```python
# db.add(complaint)
# db.flush()
# ```

# Sends pending changes to the database **without committing the transaction**.

# Useful when you need a generated ID before continuing:

# ```text
# add complaint
#      ↓
# flush()
#      ↓
# complaint.id available
#      ↓
# create assignment using complaint.id
#      ↓
# commit()
# ```

# ---

# # 13. `db.get()`

# Use when you know the **primary key**.

# ```python
# user = db.get(User, user_id)
# ```

# Example:

# ```python
# complaint = db.get(
#     Complaint,
#     complaint_id
# )
# ```

# Mental shortcut:

# ```text
# Primary key known?
#        ↓
#     db.get()
# ```

# ---

# # 14. `select()`

# For building queries:

# ```python
# statement = select(User)
# ```

# With condition:

# ```python
# statement = select(User).where(
#     User.username == "dhanush"
# )
# ```

# Important:

# ```python
# User.username == "dhanush"
# ```

# not:

# ```python
# User.username = "dhanush"
# ```

# `=` → assignment
# `==` → comparison

# ---

# # 15. `scalar()` vs `scalars()`

# ### One object/value

# ```python
# user = db.scalar(statement)
# ```

# ### Multiple ORM objects

# ```python
# users = db.scalars(statement).all()
# ```

# Think:

# ```text
# scalar()
#    ↓
# one result

# scalars()
#    ↓
# multiple scalar/ORM results
# ```

# Example:

# ```python
# statement = select(User).where(
#     User.role == "citizen"
# )

# users = db.scalars(statement).all()
# ```

# ---

# # 16. Multiple conditions = AND

# ```python
# statement = select(Complaint).where(
#     Complaint.status == "open",
#     Complaint.owner_id == 3
# )
# ```

# Means:

# ```sql
# WHERE status = 'open'
# AND owner_id = 3
# ```

# ---

# # 17. OR

# ```python
# from sqlalchemy import or_

# statement = select(Complaint).where(
#     or_(
#         Complaint.status == "open",
#         Complaint.status == "pending"
#     )
# )
# ```

# You can also use:

# ```python
# (
#     Complaint.status == "open"
# ) | (
#     Complaint.status == "pending"
# )
# ```

# But `or_()` is often easier to read.

# ---

# # 18. Sorting

# Ascending:

# ```python
# .order_by(Complaint.id)
# ```

# Descending:

# ```python
# from sqlalchemy import desc

# .order_by(desc(Complaint.id))
# ```

# Example:

# ```python
# statement = (
#     select(Complaint)
#     .order_by(desc(Complaint.id))
# )
# ```

# ---

# # 19. Pagination

# ```python
# statement = (
#     select(Complaint)
#     .order_by(desc(Complaint.id))
#     .limit(10)
#     .offset(10)
# )
# ```

# Meaning:

# ```text
# limit  → number of records
# offset → number of records to skip
# ```

# Formula:

# ```text
# offset = (page - 1) × limit
# ```

# ---

# # 20. Aggregate functions

# Import:

# ```python
# from sqlalchemy import func
# ```

# ### COUNT

# ```python
# func.count()
# ```

# ### SUM

# ```python
# func.sum(Complaint.priority_score)
# ```

# ### AVG

# ```python
# func.avg(Complaint.priority_score)
# ```

# ### MIN

# ```python
# func.min(Complaint.priority_score)
# ```

# ### MAX

# ```python
# func.max(Complaint.priority_score)
# ```

# Example:

# ```python
# statement = select(
#     func.count()
# ).select_from(Complaint)

# total = db.scalar(statement)
# ```

# ---

# # 21. `GROUP BY`

# Example:

# > How many complaints are there for each status?

# ```python
# statement = (
#     select(
#         Complaint.status,
#         func.count()
#     )
#     .group_by(Complaint.status)
# )

# result = db.execute(statement).all()
# ```

# Conceptually:

# ```text
# open       → 100
# pending     → 50
# resolved   → 200
# ```

# ---

# # 22. `HAVING`

# `WHERE` filters **rows**.

# `HAVING` filters **groups**.

# ```python
# statement = (
#     select(
#         Complaint.status,
#         func.count()
#     )
#     .group_by(Complaint.status)
#     .having(func.count() > 10)
# )
# ```

# Mental model:

# ```text
# WHERE
#  ↓
# filter rows

# GROUP BY
#  ↓
# create groups

# HAVING
#  ↓
# filter groups
# ```

# ---

# # 23. Transactions + architecture

# This is very important for interviews.

# Suppose:

# ```python
# repository.add(complaint)
# repository.add(assignment)
# ```

# Both belong to one business operation.

# The service can control:

# ```python
# try:
#     repository.add(complaint)
#     repository.add(assignment)

#     db.commit()

# except Exception:
#     db.rollback()
#     raise
# ```

# Why?

# Because the **service knows the business operation** consists of both changes.

# ---

# # 24. Repository Layer

# Repository = **database access only**.

# Example:

# ```python
# class ComplaintRepository:

#     def __init__(self, db):
#         self.db = db

#     def get_by_id(self, complaint_id):
#         return self.db.get(
#             Complaint,
#             complaint_id
#         )

#     def get_by_status(self, status):
#         statement = select(Complaint).where(
#             Complaint.status == status
#         )

#         return self.db.scalars(statement).all()
# ```

# Repository should not decide:

# > "Is this user allowed to access this complaint?"

# That's business logic.

# ---

# # 25. Service Layer

# Service = **business logic/use case**.

# Example:

# ```python
# class ComplaintService:

#     def __init__(self, repository):
#         self.repository = repository

#     def get_my_complaint(
#         self,
#         complaint_id,
#         current_user
#     ):
#         complaint = self.repository.get_by_id(
#             complaint_id
#         )

#         if complaint is None:
#             raise NotFoundError(
#                 "Complaint not found",
#                 "COMPLAINT_NOT_FOUND"
#             )

#         if complaint.owner_id != current_user.id:
#             raise ForbiddenError(
#                 "You can only access your own complaint",
#                 "COMPLAINT_NOT_OWNED"
#             )

#         return complaint
# ```

# Notice:

# ```text
# Repository
# → gets data

# Service
# → decides what should happen
# ```

# ---

# # 26. Router Layer

# Router handles **HTTP**.

# ```python
# @router.get("/complaints/{complaint_id}")
# def get_complaint(
#     complaint_id: int,
#     current_user=Depends(get_current_user),
#     service=Depends(get_complaint_service)
# ):
#     return service.get_my_complaint(
#         complaint_id,
#         current_user
#     )
# ```

# Router should not contain large business logic or raw database queries.

# ---

# # 27. Dependency Injection

# ```python
# def get_complaint_repository(
#     db=Depends(get_db)
# ):
#     return ComplaintRepository(db)
# ```

# Then:

# ```python
# def get_complaint_service(
#     repository=Depends(
#         get_complaint_repository
#     )
# ):
#     return ComplaintService(repository)
# ```

# FastAPI builds the dependency chain.

# ```text
# Request
#  ↓
# get_db()
#  ↓
# Repository(db)
#  ↓
# Service(repository)
#  ↓
# Router
# ```

# ---

# # 28. Complete architecture

# This is one of the most important diagrams to remember:

# ```text
#                  HTTP Request
#                       ↓
#                    Router
#                       ↓
#                 Dependencies
#                       ↓
#                    Service
#                       ↓
#                  Repository
#                       ↓
#                  SQLAlchemy
#                       ↓
#                   Database
# ```

# And the responsibility:

# ```text
# Router       → HTTP
# Dependency   → object creation/injection
# Service      → business rules
# Repository   → database access
# SQLAlchemy   → ORM/database communication
# Database     → persistent data
# ```

# ---

# # 29. Alembic

# Alembic manages **database schema changes over time**.

# Instead of:

# ```python
# Base.metadata.create_all(engine)
# ```

# for production schema management:

# ```text
# Change SQLAlchemy model
#         ↓
# alembic revision --autogenerate
#         ↓
# Review migration
#         ↓
# alembic upgrade head
#         ↓
# Database schema updated
# ```

# Example:

# ```text
# Migration 001
# → create users

# Migration 002
# → create complaints

# Migration 003
# → add priority_score
# ```

# ### Interview answer

# > Alembic is a database migration tool commonly used with SQLAlchemy to version and apply schema changes safely.

# ---

# # ⭐ The 30-second interview answer

# If an interviewer asks:

# **"Explain how your FastAPI application accesses the database."**

# You can say:

# > "The request first reaches the FastAPI router. Dependencies provide the database session and required services. The service contains the business logic and calls the repository. The repository uses SQLAlchemy to query or modify the database. Transactions are committed or rolled back at the appropriate business-operation boundary. Alembic manages database schema migrations."

# That's a **strong backend answer**.

# ---

# ## What you've covered so far

# ```text
# Database fundamentals
#         ↓
# SQLAlchemy ORM
#         ↓
# Models
#         ↓
# Primary Key / Foreign Key
#         ↓
# Relationships
#         ↓
# Engine / Session
#         ↓
# CRUD operations
#         ↓
# select / where
#         ↓
# scalar / scalars
#         ↓
# AND / OR
#         ↓
# sorting
#         ↓
# pagination
#         ↓
# aggregates
#         ↓
# GROUP BY / HAVING
#         ↓
# transactions
#         ↓
# add / flush / commit / rollback / refresh
#         ↓
# Repository
#         ↓
# Service
#         ↓
# Dependency Injection
#         ↓
# Router
#         ↓
# Alembic
# ```

# **This is the revision sheet I'd keep for interview preparation.** Don't memorize the code line-by-line; memorize the **patterns and responsibility of each layer**. Then practice writing the small query/code snippets from memory.
