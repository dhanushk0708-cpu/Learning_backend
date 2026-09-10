Absolutely. Before we connect Redis with FastAPI, let's lock in the **Redis Fundamentals revision sheet**.

# 🔴 Redis Fundamentals — Interview Revision Sheet

## 1. What is Redis?

**Redis = Remote Dictionary Server**

It is an **in-memory data store** commonly used for:

* Caching
* Temporary data
* Sessions
* Counters
* Queues
* Rankings
* Real-time state

### Core idea

```text
PostgreSQL → permanent/source of truth
Redis      → fast/temporary data
```

---

# 2. Why do we use Redis?

Suppose your API repeatedly asks PostgreSQL:

```text
GET /complaints/101

FastAPI → PostgreSQL → complaint
```

If 10,000 users request the same complaint:

```text
10,000 requests
       ↓
10,000 PostgreSQL queries
```

With Redis:

```text
Request
   ↓
Redis
   ↓
 HIT → return immediately
   ↓
 MISS
   ↓
PostgreSQL
   ↓
Store in Redis
   ↓
Return
```

Redis reduces repeated database work and gives very fast reads.

---

# 3. Redis vs PostgreSQL

| Redis                     | PostgreSQL                                  |
| ------------------------- | ------------------------------------------- |
| Mainly in-memory          | Persistent database                         |
| Extremely fast            | Slower than Redis for simple repeated reads |
| Usually cache/state       | Source of truth                             |
| Key-value/data structures | Relational database                         |
| TTL commonly used         | Data normally persists                      |
| Great for temporary data  | Great for permanent application data        |

**Interview answer:**

> Redis is commonly used as a high-speed cache or temporary data store, while PostgreSQL is usually the persistent source of truth.

---

# 4. Redis Key-Value Model

The simplest Redis model is:

```text
KEY → VALUE
```

Example:

```redis
SET username "dhanush"
GET username
```

Result:

```text
dhanush
```

Think:

```text
"username" → "dhanush"
```

---

# 5. Redis Data Types

These are the important ones we practiced:

| Type       | Example use              |
| ---------- | ------------------------ |
| String     | Cache, token, counter    |
| Hash       | Object-like data         |
| List       | Queue                    |
| Set        | Unique values            |
| Sorted Set | Ranking/priorities       |
| Stream     | Event/message processing |

---

# 6. String

Basic commands:

```redis
SET username "dhanush"
GET username
```

Useful for:

```text
cached API response
OTP
token
counter
simple value
```

Example:

```redis
SET complaint:1 "Broken road"
GET complaint:1
```

---

# 7. TTL — Time To Live

TTL tells Redis **how long a key should remain alive**.

Example:

```redis
SET otp "123456" EX 30
```

The key expires after **30 seconds**.

Check remaining time:

```redis
TTL otp
```

Possible results:

```text
25
10
3
```

Special values:

```text
-1 → key exists but has no expiration
-2 → key does not exist
```

### Why TTL?

For temporary data:

```text
OTP
Cache
Temporary session data
Rate-limit information
```

You don't want these to live forever.

---

# 8. Cache Hit vs Cache Miss

### Cache HIT

Data exists in Redis:

```text
Request
   ↓
Redis
   ↓
HIT
   ↓
Return data
```

No PostgreSQL query required.

### Cache MISS

Data isn't in Redis:

```text
Request
   ↓
Redis
   ↓
MISS
   ↓
PostgreSQL
   ↓
Store in Redis
   ↓
Return
```

---

# 9. Cache-Aside Pattern ⭐

This is the most important Redis caching pattern for our backend.

```text
             ┌─────────┐
Request ───→ │  Redis  │
             └────┬────┘
                  │
             ┌────┴────┐
             │         │
            HIT       MISS
             │         │
             ↓         ↓
           Return   PostgreSQL
                       │
                       ↓
                  Store Redis
                       │
                       ↓
                    Return
```

Python idea:

```python
cached_data = redis.get(key)

if cached_data:
    return cached_data

data = get_from_postgresql()

redis.set(key, data, ex=60)

return data
```

**Interview answer:**

> In cache-aside, the application first checks Redis. On a cache miss, it fetches the data from the database, stores it in Redis, and returns it.

---

# 10. Cache Invalidation ⭐

Suppose PostgreSQL has:

```text
complaint:1 → "Broken road"
```

Redis also has:

```text
complaint:1 → "Broken road"
```

Then PostgreSQL is updated:

```text
"Fixed road"
```

But Redis still says:

```text
"Broken road"
```

Now Redis contains **stale data**.

Therefore, after updating the source of truth, we may:

```redis
DEL complaint:1
```

or update the cached value.

### Important principle

> Cache invalidation means removing or updating stale cached data after the underlying data changes.

---

# 11. Hash

Hash stores multiple fields under one key.

Example:

```redis
HSET complaint:10 title "Broken street" status "open" priority "high"
```

Read everything:

```redis
HGETALL complaint:10
```

Read one field:

```redis
HGET complaint:10 status
```

Conceptually:

```text
complaint:10
│
├── title → Broken street
├── status → open
└── priority → high
```

Useful for:

```text
User/session information
Cached objects
Complaint state
```

---

# 12. TTL on Hash

You can apply expiration to the **whole hash key**:

```redis
EXPIRE complaint:10 60
```

Important:

```text
complaint:10
     ↓
 entire hash expires
```

Individual fields don't independently get TTL through this command.

---

# 13. List

A Redis List is an ordered collection.

Example:

```redis
RPUSH jobs "job 101"
RPUSH jobs "job 102"
RPUSH jobs "job 103"
```

Read:

```redis
LRANGE jobs 0 -1
```

Remove from left:

```redis
LPOP jobs
```

### Queue pattern

```text
Producer
   ↓
RPUSH
   ↓
Redis List
   ↓
LPOP
   ↓
Consumer
```

Useful for simple queues/background jobs.

---

# 14. Set

A Set stores **unique values**.

```redis
SADD complaint:tags "road"
SADD complaint:tags "pothole"
SADD complaint:tags "road"
```

The second `"road"` isn't added again.

Read:

```redis
SMEMBERS complaint:tags
```

Key property:

> Set = unique values, unordered.

---

# 15. Sorted Set ⭐

A Sorted Set stores:

```text
MEMBER + SCORE
```

Example:

```redis
ZADD complaint_priority 95 "complaint:101"
ZADD complaint_priority 80 "complaint:102"
ZADD complaint_priority 60 "complaint:103"
```

Read highest first:

```redis
ZREVRANGE complaint_priority 0 -1 WITHSCORES
```

Result:

```text
complaint:101 95
complaint:102 80
complaint:103 60
```

Get a member's score:

```redis
ZSCORE complaint_priority "complaint:102"
```

Useful for:

```text
Leaderboards
AI priority
Top complaints
Ranking systems
```

For our **Civil AI** project, this can become useful for prioritizing complaints.

---

# 16. Redis Commands We Know

### Strings

```redis
SET
GET
DEL
TTL
EXPIRE
```

### Hash

```redis
HSET
HGET
HGETALL
```

### Lists

```redis
LPUSH
RPUSH
LPOP
LRANGE
```

### Sets

```redis
SADD
SMEMBERS
```

### Sorted Sets

```redis
ZADD
ZREVRANGE
ZSCORE
```

---

# 17. Redis + FastAPI Architecture

This is the important part going forward.

Eventually our backend will look like:

```text
             Client
                ↓
             FastAPI
                ↓
             Service
                ↓
          ┌─────┴─────┐
          ↓           ↓
       Redis      Repository
          ↓           ↓
       Cache      PostgreSQL
```

For a complaint:

```text
GET /complaints/101
        ↓
      Service
        ↓
   Redis GET
     ↙     ↘
  HIT      MISS
   ↓         ↓
return   Repository
             ↓
        PostgreSQL
             ↓
        Redis SET
             ↓
           return
```

---

# 18. Most Important Interview Questions

### Q1. Why Redis?

> Redis provides very fast in-memory access and is commonly used to cache frequently accessed data and reduce database load.

### Q2. What is TTL?

> TTL means Time To Live. It specifies how long a Redis key should exist before automatically expiring.

### Q3. What is a cache hit?

> A cache hit occurs when the requested data is already present in Redis.

### Q4. What is a cache miss?

> A cache miss occurs when the requested data is not present in Redis, so the application fetches it from the database or another source.

### Q5. What is cache invalidation?

> Cache invalidation means removing or updating stale cached data when the underlying source-of-truth data changes.

### Q6. What is cache-aside?

> The application checks the cache first. If there's a miss, it reads from the database, stores the result in the cache, and returns it.

### Q7. Redis vs PostgreSQL?

> Redis is primarily used for fast temporary/cache/state data, while PostgreSQL is a persistent relational database and usually the source of truth.

### Q8. Difference between Set and Sorted Set?

> A Set stores unique values, while a Sorted Set stores unique members associated with scores and maintains them according to those scores.

### Q9. What is a Redis Hash?

> A Hash stores multiple field-value pairs under a single Redis key and is useful for representing object-like data.

### Q10. Can Redis replace PostgreSQL?

> Usually no. Redis and PostgreSQL solve different problems. Redis is commonly used as a cache or fast state store, while PostgreSQL provides durable relational storage and complex querying.

---

# 🧠 One-minute mental revision

If you remember only this:

```text
REDIS
│
├── In-memory → very fast
│
├── Key → Value
│
├── String → simple values/cache
├── Hash → object fields
├── List → queue
├── Set → unique values
├── Sorted Set → ranking/priority
│
├── TTL → automatic expiration
│
├── HIT → data found in cache
├── MISS → go to database
│
├── Cache-aside
│      Redis → HIT → return
│      Redis → MISS → DB → Redis → return
│
└── Invalidation
       DB changed → remove/update stale cache
```

