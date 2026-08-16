"""
PHASE 5
TOPIC: DEPENDENCY INJECTION

PURPOSE:

Give a component the dependencies
it needs from outside instead of
creating them internally.


FLOW:

Router
   ↓
Service
   ↓
Repository
   ↓
Database


EXAMPLE:

def get_user_repository():
    return UserRepository()


def get_user_service(
    repository=Depends(get_user_repository)
):
    return UserService(repository)


ROUTER:

service: UserService = Depends(
    get_user_service
)


WHY?

✔ Easy testing
✔ Easy replacement
✔ Less tightly coupled
✔ Cleaner architecture


IMPORTANT:

Component needs dependency
        ↓
Dependency is provided from outside


REMEMBER:

Depends()
→ tells FastAPI where to get
  the dependency.


SELF:

self = current object


Example:

self.repository

→ repository belonging to
  THIS object.
"""
