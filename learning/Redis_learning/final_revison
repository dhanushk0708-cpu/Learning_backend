# 🔴 Redis — Final Interview Revision

This is the **final sheet** you should keep in your notes. Don't memorize every command—understand the mental models.

---

## 1. What is Redis?

> Redis is an in-memory data store commonly used for caching, temporary state, counters, queues, rankings, and real-time messaging.

```text
PostgreSQL → persistent source of truth
Redis      → fast cache/state
```

---

## 2. Why Redis?

Because repeated database reads can be expensive.

```text
Without Redis:

Request → PostgreSQL → Response
Request → PostgreSQL → Response
Request → PostgreSQL → Response
```

With caching:

```text
Request → Redis → HIT → Response

Request → Redis → MISS
                  ↓
              PostgreSQL
                  ↓
                Redis
                  ↓
              Response
```

---

# 3. Redis Data Types

| Type       | Main use                       |
| ---------- | ------------------------------ |
| String     | Simple values, cache, counters |
| Hash       | Object-like data               |
| List       | Queue / ordered collection     |
| Set        | Unique values                  |
| Sorted Set | Ranking / priority             |
| Stream     | Event/message processing       |

### Examples

```redis
SET username "dhanush"
```

```redis
HSET complaint:1 title "Broken road" status "open"
```

```redis
RPUSH jobs "job-101"
```

```redis
SADD tags "road"
```

```redis
ZADD priorities 95 "complaint:101"
```

---

# 4. TTL ⭐

**TTL = Time To Live**

```redis
SET otp "123456" EX 30
```

Means the key expires after 30 seconds.

```redis
TTL otp
```

Special results:

```text
positive → seconds remaining
-1       → key exists without expiration
-2       → key doesn't exist
```

---

# 5. Cache HIT vs MISS ⭐

### HIT

```text
Redis has data
      ↓
Return it
```

### MISS

```text
Redis doesn't have data
       ↓
Database
       ↓
Store in Redis
       ↓
Return
```

---

# 6. Cache-Aside ⭐⭐⭐

This is one of the **most important Redis concepts** for backend interviews.

```text
Application
     ↓
   Redis
  ↙     ↘
HIT     MISS
 ↓        ↓
Return  PostgreSQL
           ↓
       Redis SET
           ↓
         Return
```

Interview answer:

> In the cache-aside pattern, the application checks the cache first. On a cache miss, it retrieves the data from the database, stores it in the cache, and returns it.

---

# 7. Cache Invalidation ⭐⭐⭐

Suppose:

```text
PostgreSQL → "Broken road"
Redis      → "Broken road"
```

Update PostgreSQL:

```text
PostgreSQL → "Road repaired"
Redis      → "Broken road" ❌
```

Redis is now stale.

One simple solution:

```python
redis_client.delete("complaint:1")
```

Then:

```text
Next GET
   ↓
Redis MISS
   ↓
PostgreSQL
   ↓
Redis SET latest value
```

Interview phrase:

> Cache invalidation removes or updates stale cached data when the source data changes.

---

# 8. Atomic Operations

Redis supports atomic commands such as:

```redis
INCR complaint_count
```

Useful for:

```text
Counters
Views
Likes
Request counts
Rate limiting
```

Atomic means concurrent operations don't simply overwrite each other's increments.

---

# 9. Rate Limiting ⭐

Example:

> Maximum 5 requests per minute.

Concept:

```text
Request
   ↓
INCR rate_limit:user1
   ↓
count <= 5 → allowed
count > 5  → HTTP 429
```

TTL makes the counter expire:

```text
60 seconds
    ↓
counter disappears
    ↓
new window
```

Interview answer:

> Redis is useful for rate limiting because atomic counters and TTL can efficiently track requests over a time window.

---

# 10. MULTI / EXEC

Redis can group commands:

```redis
MULTI
SET key value
INCR counter
EXEC
```

Mental model:

```text
MULTI
  ↓
Queue commands
  ↓
EXEC
  ↓
Execute sequentially
```

It is **not identical to PostgreSQL transactions**.

---

# 11. Pub/Sub

Pub/Sub means:

```text
Publisher
    ↓
Redis Channel
    ↓
Subscribers
```

Example:

```redis
PUBLISH complaint_updates "Complaint 101 updated"
```

Useful for:

* Real-time notifications
* Live updates
* Event broadcasting

Important limitation:

> A subscriber that is disconnected when a message is published doesn't receive that old message later.

---

# 12. Redis Streams

Streams provide an event/message log.

```text
complaint_events
│
├── complaint created
├── complaint updated
├── complaint assigned
└── complaint resolved
```

Useful for:

* Event processing
* Background workers
* Asynchronous workflows

### Pub/Sub vs Streams

```text
Pub/Sub
→ real-time
→ active subscribers
→ messages aren't retained for offline subscribers

Streams
→ stored event data
→ can be processed later
→ better for event-processing workflows
```

---

# 13. RDB vs AOF

Redis can persist data to disk.

### RDB

Periodic snapshots:

```text
Redis
 ↓
Snapshot
 ↓
dump.rdb
```

### AOF

Records write operations:

```text
SET ...
INCR ...
HSET ...
 ↓
AOF
```

| RDB             | AOF                               |
| --------------- | --------------------------------- |
| Snapshots       | Write-operation log               |
| Smaller/compact | Usually larger                    |
| Fast recovery   | Better durability characteristics |
| Backup friendly | More continuous logging           |

Interview answer:

> RDB periodically saves snapshots, while AOF records write operations so Redis can reconstruct the dataset after restart.

---

# 14. Eviction

Redis memory is limited.

When it reaches its configured memory limit, Redis can use an **eviction policy**.

Important ones:

```text
noeviction
allkeys-lru
allkeys-lfu
volatile-lru
```

### LRU

**Least Recently Used**

Removes keys that haven't been used recently.

### LFU

**Least Frequently Used**

Removes keys that are accessed least frequently.

For a cache, eviction is acceptable because:

```text
Redis data removed
      ↓
Cache MISS
      ↓
PostgreSQL
      ↓
Rebuild cache
```

---

# 15. Connection Pooling

A Redis client can reuse connections rather than creating a completely new network connection for every request.

```text
FastAPI
   ↓
Redis Client
   ↓
Connection Pool
 ┌──┬──┬──┬──┐
 │C1│C2│C3│C4│
 └──┴──┴──┴──┘
   ↓
 Redis
```

Purpose:

> Efficiently manage and reuse Redis connections under concurrent workloads.

---

# 16. Redis Security

Production principles:

```text
Don't expose Redis directly to the internet
Use authentication
Use TLS when appropriate
Keep credentials in secrets/env variables
Configure memory limits
Use appropriate eviction policies
Don't casually store sensitive information
```

---

# 17. Redis + FastAPI Architecture ⭐⭐⭐

The architecture we actually built:

```text
                Client
                  ↓
               FastAPI
                  ↓
                Router
                  ↓
                Service
             ↙          ↘
          Redis       Repository
            ↓             ↓
          Cache       PostgreSQL
```

Request:

```text
GET /complaints/1
       ↓
    Service
       ↓
    Redis GET
      ↙   ↘
    HIT   MISS
     ↓      ↓
  Return  Repository
             ↓
        PostgreSQL
             ↓
          Redis SET
             ↓
          Return
```

Update:

```text
PUT /complaints/1
       ↓
    Service
       ↓
 PostgreSQL UPDATE
       ↓
 Redis DELETE
       ↓
    Response
```

That's the important real-world pattern you implemented.

---

# 🎯 15 Interview Questions You Should Be Able To Answer

Try answering these **without looking at the answers**:

1. What is Redis?
2. Why would you use Redis with PostgreSQL?
3. What is a cache hit?
4. What is a cache miss?
5. What is TTL?
6. Explain cache-aside.
7. What is cache invalidation?
8. Why can stale cache be dangerous?
9. Redis String vs Hash?
10. Set vs Sorted Set?
11. Why is `INCR` useful?
12. How can Redis implement rate limiting?
13. Pub/Sub vs Streams?
14. RDB vs AOF?
15. What happens if Redis cache data disappears?

### ⭐ The most important answer

If an interviewer asks:

**"Explain how you used Redis in your backend project."**

You can now say:

> "I used Redis as a cache in front of PostgreSQL. When a complaint is requested, the service first checks Redis. If there's a cache hit, it returns the cached data. On a miss, it retrieves the complaint from PostgreSQL through the repository, serializes the result, stores it in Redis with a TTL, and returns it. When the complaint is updated, the PostgreSQL data is updated first and the corresponding Redis key is invalidated to prevent stale data."

That's a **real backend answer**, not a textbook definition.

---

## 🏁 Redis COMPLETE

You've gone from:

```text
Redis basics
    ↓
Docker Redis
    ↓
Redis CLI
    ↓
Data structures
    ↓
TTL
    ↓
Cache-aside
    ↓
FastAPI
    ↓
PostgreSQL
    ↓
Repository
    ↓
Service
    ↓
Cache invalidation
    ↓
Rate limiting
    ↓
Pub/Sub
    ↓
Streams
    ↓
Persistence
    ↓
Eviction
    ↓
Production concepts
    ↓
Interview revision
```

**Redis is officially closed for now.** 🔴

Next we'll move to the **next backend concept**, without getting stuck endlessly studying Redis.
