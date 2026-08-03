"""
=========================================
PHASE 2

TOPIC : LIFESPAN EVENTS
=========================================

USED IN

app/main.py

"""

from contextlib import asynccontextmanager

# WHY?
# Run code when FastAPI
# starts and stops.

# CIVIL AI IMPLEMENTATION


@asynccontextmanager
async def lifespan(app):

    print("Application Started")

    yield

    print("Application Stopped")


app = FastAPI(lifespan=lifespan)

# CONCEPT

# Server Starts

# ↓

# Startup Code

# ↓

# APIs Run

# ↓

# Shutdown Code

# INTERNAL FLOW

# FastAPI Starts

# ↓

# Lifespan Start

# ↓

# Requests

# ↓

# Lifespan End

# INTERVIEW

# Q: What are Lifespan Events?
#
# A:
# They execute startup and
# shutdown logic for the application.

# COMMON BEGINNER MISTAKE

# ❌ Running startup code
# inside every API.

# ✅ Run it once using Lifespan.

# RELATED CONCEPTS

# FastAPI

# ↓

# Lifespan

# ↓

# Startup / Shutdown

# REMEMBER

# ✔ Runs Once
# ✔ Startup Logic
# ✔ Shutdown Logic
# ✔ Configured in main.py
