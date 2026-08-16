"""
PHASE 5
TOPIC: CLEAN ARCHITECTURE

FLOW:

Router
   ↓
Service
   ↓
Repository
   ↓
Database


ROUTER
→ HTTP request / response
→ status codes
→ API endpoint


SERVICE
→ Business logic
→ Business decisions
→ Workflow


REPOSITORY
→ Database operations
→ Queries
→ CRUD


WHY?

Separates responsibilities.

Makes code:
✔ Easy to maintain
✔ Easy to test
✔ Easy to modify
✔ Reusable


REMEMBER:

Router   = HTTP
Service  = Business Logic
Repository = Database
"""
