# Commands and Queries

## Problem 

Cross Service Queries and Write Command on Distributed Scaled Databases

- Considerations
  - How to retrieve data from several msvcs?
  - How can we seperate read/write at scale?
- Problems
  - Cross-Service Queries with Complex JOIN ops
  - Read/Write ops at scale
  - Dstributed TX Management
- Solutions
  - Microservices Data Query Pattern 
  - Materialized View Pattern
  - CQRS Pattern
  - Event Sourcing Pattern

# Cross-Service Queries & how to reduce

- Monolith can query many entities easily
  - Strong consistency 
  - ACID compliant
- Microservices use Polyglot persistence
  - We need a strategy to manage queries
- What if clients requests visit multiple svcs

- How to manage cross svc queries?
  - Direct HTTP?
    - Not good, couples microservices. 
  - Async Comms?
    - BP = Reduce inter-svc as much as possible & use async
    - Sometimes not possible
    - Client may need immediate response, Async no good
    - Transient errors, network congestion, svc overload may cause long running queries
  - Materialized View Pattern
    - Reduce inter-service comms and provide sync response. 

## X-Service query solutions

- API Gateway Patterns
  - We can solve X-qeuries applying aggregator pattern 
    - Using an aggregator microsvc
- How can we solve this problem at database level?

- Problems
  - Cross-service queries with complex joins
  - Return sync response with low latency
  - reduce inter-service comms
- Considerations
  - Sync Comms, Svc Aggregator Pattern but increase coupling & latency
  - Async Comms, decoupling svcs, but query requests are waiting for response async
- Solutions
  - Materialized View Pattern
  - CQRS Pattern

# Materialized View Pattern

- Why do we need Materialized View Pattern?
- mostly DB are designed focusing on tables for managing data size & data integrity
- How is the data stored?
  - Instead, how is the data read?
    - This can impact queries, throughput/latency
- Materialized View Pattern is a store containing a denormalized copy of data in the microservices database. 
  - This eliminates the need for cross-service calls. 
  - Reduces coupling and improves reliability, response time
  - Can execute entire op in a single process
- MV could also be called READ model
- Instead of querying services, it maintains it's own local copy of the data

- In summary MV pattern offers to generate pre-populated views of data, more suitable for querying & provide good query performance. 
  - These prepopulated views include joining tables and combining data entities & calculated cols & data transforms
  - Views are disposable and re-built from sources

- Drawbacks
  - Duplicated data
    - However for strategic reasons
    - Only one svc can own data
    - How will our denormalized view be updated?
    - When the original source is updated, so too should the MV be updated
      - We solve this with async messaging & pub/sub pattern
      - Publish an event when data changes, subscribers listen to updated their MV or denomalised table. 
      - Possible to use scheduled task, external triggers or manual action to update MV

# CQRS

## Command Query Responsibility Segregation Patter

- CQRS is used to avoid complex queries and get rid of inefficient joins
- Seperates read & write ops by seperating them into databases for read & write
- 