"""
PHASE 5
TOPIC: PROFESSIONAL ERROR HANDLING

FLOW:

Service
   ↓
raise AppException
   ↓
Global Exception Handler
   ↓
HTTP Response


BASE EXCEPTION:

class AppException(Exception):

    def __init__(
        self,
        message,
        error_code,
        status_code
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code


EXCEPTION HIERARCHY:

AppException
│
├── NotFoundError → 404
├── ConflictError → 409
└── UnauthorizedError → 401


super():

super()
→ parent class

super().__init__()
→ calls parent's __init__()


EXAMPLE:

raise NotFoundError(
    "User not found",
    "USER_NOT_FOUND"
)


GLOBAL HANDLER:

@app.exception_handler(AppException)
async def app_exception_handler(request, exc):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "error_code": exc.error_code
        }
    )


WHY?

Don't create 100 handlers for
100 different resources.

Group errors by category.


FLOW:

Service
   ↓
Exception
   ↓
Global Handler
   ↓
HTTP Response


REMEMBER:

Service → raises error
Exception → describes error
Handler → converts it to HTTP response
"""
