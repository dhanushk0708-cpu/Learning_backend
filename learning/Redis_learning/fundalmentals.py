1. Redis = in-memory data store

2. Redis is extremely fast because data is primarily
   accessed from memory

3. PostgreSQL remains the source of truth;
   Redis is often used for caching/temporary state

Redis type	Example use
String	Cache values, tokens, counters
Hash	User/session/object-like data
List	Queues, ordered items
Set	Unique values
Sorted Set	Rankings/leaderboards
Streams	Event/message processing

Cache HIT      → data exists in Redis
Cache MISS     → data isn't in Redis
TTL            → automatic expiration
Invalidation   → remove/update stale cached data

SET       → store data
GET       → retrieve data
EX        → expiration time
TTL       → check remaining lifetime