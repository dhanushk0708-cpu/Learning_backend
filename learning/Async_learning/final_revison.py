Async vs Threads vs Processes

Remember this simple decision:

What kind of work?
       │
       ├── Mostly waiting (I/O)
       │       │
       │       ├── Async library available?
       │       │       ↓
       │       │     asyncio
       │       │
       │       └── Blocking library?
       │               ↓
       │             Thread
       │
       └── Heavy CPU calculation
               ↓
        Multiprocessing
FastAPI example
GET /complaint
      ↓
Need PostgreSQL ──┐
Need Redis ───────┼──→ asyncio.gather()
Need AI API ──────┘
      ↓
   Response

If the operations are independent and support async, gather() can overlap their waiting time.

⭐ Interview rule

I/O-bound → async/threads
CPU-bound → processes
asyncio.gather() → run multiple async operations concurrently and wait for their results