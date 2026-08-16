"""
PHASE 5
TOPIC: SERVICE LAYER

PURPOSE:

Keep business logic outside the Router.


FLOW:

Router
   ↓
Service
   ↓
Repository
   ↓
Database


SERVICE DOES:

✔ Business decisions
✔ Validation of business rules
✔ Workflows
✔ Coordinates multiple operations


EXAMPLE:

Service:
→ Check duplicate complaint
→ Calculate priority
→ Decide department
→ Call repository


IMPORTANT:

Service should NOT contain
direct database queries.


REMEMBER:

Service = What should the application DO?


INTERVIEW:

Q: Why Service Layer?

A:
To separate business logic from
HTTP and database concerns.
"""
