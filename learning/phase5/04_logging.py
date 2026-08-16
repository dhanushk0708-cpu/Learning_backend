"""
PHASE 5
TOPIC: LOGGING

PURPOSE:

Track what happens inside
a production application.


BASIC:

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)


LEVELS:

DEBUG    → Developer details
INFO     → Normal events
WARNING  → Something unusual
ERROR    → Something failed
CRITICAL → Serious failure


EXAMPLE:

logger.info("Server started")

logger.warning("Slow request")

logger.error("Database failed")


__name__:

logging.getLogger(__name__)

→ Creates/gets a logger identified
  by the current Python module.


REQUEST LOGGING:

Middleware
   ↓
Start timer
   ↓
call_next(request)
   ↓
Response
   ↓
Calculate time
   ↓
Log request


IMPORTANT:

perf_counter()
→ seconds

seconds × 1000
→ milliseconds


EXAMPLE:

GET /complaints 200 42ms


SLOW REQUEST:

if process_ms > 1000:
    logger.warning(...)


REMEMBER:

Logging helps us debug
and monitor production systems.
"""
