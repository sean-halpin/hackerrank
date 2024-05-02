# Choosing the right database

- Polyglot Persistence, DB per service pattern, shared db anti-pattern
- Relational & NoSQL DB
- CAP Theorom
- Data Partitioning, Hor, Ver, Functional
- DB Sharing Pattern

## Problem - DB Bottlenecks when scaling

- Problems
  - DB are stateful services
  - Scaling stateful svcs not easy
  - Vertical Scaling has limits, learn to scale horiz
- Solutions
  - Scale stateful application horizontal scaling
  - Service & Data Partitioning along Business Boundaries
    - Shards/Pods
  - Use NoSQL DB to gain easy patitioning features
- Question
  - How to choose the type of DB for msvcs

## Polyglot Persistence Principle

- DB per sevc
  - Do not share DB
  - Share data over rest apis
    - So as to decouple svcs
  - DB Schema change shouldn't break other svcs
    - Limits scope of changes when schema changes
  - Can choose a different DB type per svc
- Challenges
  - Duplicated or partitions data can make problems for 
    - Data Integrity 
    - Data Consistency
  - Strict or eventual consistency

- In monolith apps we can avoid dupe data and avoid consistency issues with strict transcations
- In MSvcs we have to welcome duplicate data & eventual consistency 
- We accept eventual conssitency where possible
- Define consistency req's before we design the system
- If we need strict consistency & ACID txs we should follow traditional approaches
  - ACID (atomicity, consistency, isolation, durability)
- Event-driven arch embraces eventual consistency 
  - Msvcs publish an event when any changes happen to the data model
  - Subscribers msvcs consume & process events afterwards, leading to eventual consistency

- Cannot have ACID transactions between distributed systems
- Challenge to query and perform transactions across multiple svcs

- Microservice DB Management Patterns & Principles
  - DB per svc pattern 
  - API composition pattern
  - CQRS pattern
  - Event Sourcing pattern
  - SAGA pattern
  - Shared DB anti-pattern

## DB per svc pattern

- When shifting to msvcs
  - Need to decompose monolith db
    - Distributed Data model with smaller dbs for each svc
    - Data schema changes can be made without impact to other svcs
    - No SPOF, adds resiliency
    - Individual DBs easier to scale
      - Granularity in scaling also

- We can use different DB tech per svc/db
  - Choose relational, doc, key-val, graph-based data stores

- Drawbacks of DB per svc
  - Services needing data from another svc must communicate on network
  - Each svc must provide a clear API
    - Maybe needing retry & circuit breaker
  - Distributed transactions across msvcs can impact consistency & atomicity
  - Complex queries
    - No simple way to execute join queries on multiple data stores

## Shared DB anti-pattern

- Shared DB among msvcs is an ANTI-PATTERN
- It will cause issues with new features, bugs, deploys
- Msvcs lose, scalability, resiliency & independance with shared DB
- Shared DB becomes SPOF for many msvcs
- If shared DB is the best option
  - Consider that a monolith may be a better choice

- Pros
  - Tx management, no need for SAGA 
  - Decrease dupe data
  - Follow ACID principles easily
- Drawbacks
  - Msvcs with shared db cannot scale
  - Shared db becomes SPOF for multiple svcs
  - Msvcs won't be independent in terms of development & deployment.

- Polyglot persistence
  - Each svc & each team can choose a db that suits their use case
  - Comes at a cost
    - When relational db is used inappropriately they harm an app development
    - If you have no need to share db or perform acid tx
      - Relational db may not be best

## Relational & NoSQL DBs

- Relational DBs
  - Fixed schema
  - Use SQL to manage data
  - Support tx with ACID principles
  - Table uses columns and rows to store data
  - Each table has a unique key, primary key
  - A primary key in another table is a foreign key
  - Main benefits
    - ACID compliance
      - Atomicity
      - Consistency
      - Isolation
      - Durability

- NoSQL DBs, Non-relational DB
  - Types
    - Document
    - Key-Value
    - Graph
    - Column
  - Characteristics
    - Ease of use
    - Scalability
    - Resilience
    - Availability
  - NoSQL stores unstructured data
    - Huge perf advantage
  - Unstructred JSON or key-val pairs
  - No ACID gaurantees
  - Drawback is tx management

- NoSQL DBs
  - Data & metadata can be stored hierarchically 
    - No need to run joins
    - Objects map to app code
  - Scalability
    - Document stores scale well
    - Good choice for content management or catalogs
  - Examples;
    - Mongo
- NoSQL Key-Value databases
  - Good for session oriented apps
  - Examples;
    - Redis
- NoSQL Column Based DBs
  - Stored in columns
  - Use cases, Big Data Processing
  - Examples;
    - Cassandra
    - HBase
    - DynamoDB
    - CosmosDB
- NoSQL Graph-based DBs
  - Data stored in graph structure
    - Node, Edhe, Data props
  - Benefits is to store and navigate graph relationship
  - Example
    - OrientDB
    - Neo4J
    - Amazon Neptune

## When to use Relational DBs

- ACID compliance
  - If one change fails, DB should remain in the previous state before the tx
  - Data Consistency is fully provided
  - Predictable Data, Low Workload Volume
    - RDMS good choice is app data is predictable & workload within thousands of tx per second. 
  - Normalization also reduce the size of the data on disk by minimising dupe data & anomalies
- RDBMS works where relationships between tables are important and data is highly structured & requires referential integrity
- Can work with complex queries, joins, reports on normalized models
- Supports powerful SQL language
- Deployments & Centralized structure
- SPOF
- Deployed in Vertical fashion

## When to use No-SQL DBs

- Flexible Schema, Dynamic data
- Use Case
  - IoT platform storing data from diff sensors with frequently changed attributes
  - Unpredictable Data & High Workload Volume
    - Scaling horiz is possible
- NoSQL prioritizes partitioning 
- Data Consistency, BASE
  - Basically Available
  - Soft State
  - Eventual Consistency
- no TX support
- Write Support Req'd
  - noSQl compromises consistency to achieve fast write perf
    - Eventual consistency embraced
- Not Good for complex join queries
- Deployments
  - De-centralized
  - Better availability & perf with distributed deployments

## Best Practices when choosing data store

- Focus on data type needed to be stored
  - JSON in NoSQL Document DB
  - Transactional Data in RDMS
  - Telemetry in Time Series DB
  - Blob in Blob Storage
  - App Logs in Elastic Search DB
- Understand Tradeoffs between availability and consistency
  - Prefer high availability over strong consistency where possible
    - in order to scale horizontally (CAP)
- Consider Transactional Boundaries
  - If a transaction occurs across multiple microservices
    - It may not be consistent
    - Compensating transactions needed in case of failure
- Competence of dev teams
  - What DB tech do they know?

## How to choose db for microservice

- Problem
  - DBs create bottlenecks when scaling
  - DB are stateful
  - Scaling not easy
  - Veritcal Scaling has limits
  - Diff data reqs per service
- Solutions
  - Scale Stateful App Horizontally
  - Service & Data Partitioning along business boundaries
  - Use NoSQL DB to gain partitioning
  - Identify Database Reqs following best practices
- Question
  - How to choose DB for msvcs?

- How?
  - Questions
    - Data Consistency Level?
      - Strict or Eventual?
    - ACID compliance?
      - Requires RDMS to perform ACID in tx scope
        - Prevents high scalability and availability
    - Fixed or Flexible Schema
      - Is the data shape predictable or dynamic?
      - RDMS for predicatable data
      - NoSQL for dynamic data
    - High Volume or Low?
      - High vol benefits from NoSQL scaling
      - NoSQL allows partitioning & partition tolerance
    - Read Requirements
      - Relational or Non Relational Data, Complex Join Queries?
      - Is data highly structured and requires referential integrity
      - Or, is there no relational data 
      - Are data operations simple and done without table joins?
    - Deployments
      - Centralized or De-centralized across geo zones?
    - High-Perf ?
      - Do we need fast read-write perf?
      - Low Latency reqs
    - Scalability Reqs
      - Do we need high scalability?
      - Is vertical enough?
      - To provide millions of reqs
        - Must sacrficie strong consistency
    - High availability & Low Latency Reqs
      - Do we need high availability & Low Latency across geo zones?
    - We cannot prodivde ALL the above at once.
      - Due to CAP theorom

## CAP Theorem

- Eric Brewer 1998
  - Consistency, Availability & Partition Tolerance cannot all be achieved at same time. 
  - Distributed Systems must sacrifice one of CAP
  - Any DB can only gaurantee 2 of the 3 concepts of CAP
- CAP Theorom
  - Consistency 
    - All clients see same view of data, even right after update or delete
    - If data is not up to date, db should block until it has the latest
  - Availability
    - All clients can find a replica of the data, even when nodes have failures
    - Ensures system is available 100% of the time
  - Partition Tolerance
    - System continues to work as expected, even in the presence of network failure or node failure.

- Consistency & Availability at the same time?
  - If there is a partition tolerance req, availability or consistenct myst be sacrificed
  - Partition Tolerance is a MUST for distributed architectures
    - The emergence of NoSQL DB is to overcome the SPOF problem
  - RDBMS prevent distribution of data on different nodes
    - NoSQL dont use foreign keys, joins or relations
  - NoSQL databases easily scalable

- NoSQL DBs
  - MongoDB
  - Cassandra

- In Distributed arch, partition tolerance is a must
  - If a system is to be fully consistent is must sacrfice availability
  - If it is desiered to be accessible at all time the consistency should be sacrificed
- In Microsvcs
  - Choose Partition Tolerance, then
    - Availability & so - Eventual Consistency

## Problem - Single DB Server performance is not sufficient

- Problems
  - DB becomes slow as app grows
  - Runs out of disk space
- Solutions
  - Data Partitioning
  - Horizontal, Vertical, Functional Data Partitioning
    - Improves;
      - Availability
      - Scalability
      - Performance
      - Security

## What is data partitioning?

- Data Partitioning
  - Divides Dataset into smaller partititions
  - Smaller Parts can be easier to manage
  - Distributes data across partitions to improve db availability, scalability & performance (Non FRs)
- Abstract Partitioning from clients !
  - Clients should see db as a single unit

- Why use data partitioning?
  - Increase scalability
  - Spread data across servers
  - Vertical scaling instead has physical limits
  - Improve availability
    - If an instance fails, only affects some data
  - Increase Perforance
    - Only query partitions holding such data
  - Improve Security
    - Store sensitive data in diff partitions
  - Improve Data Management
    - Easier to index smaller tables/partitions

- Partitioning Strategies
  - Horizontal
    - aka Sharding
    - Each partition is a seperate data store with same schema
    - Split on partition key
      - Client queries db based on partition key
    - Data load spread over multiple servers
    - Important to choose partition key that distributes evenly
  - Vertical
    - Each partition holds a subset of columns for a table
    - We can divide by mostly visited columns
    - Benefit;
      - Seperate critical and mostly visited columns in diff servers
    - Best Practices
      - Seperate rarely changed and freq changed data into diff servers
  - Functional
    - Data is segregated by bounded context or subdomains
    - Similar to decomposing microservices per responsibilities considering bounded contexts

## Database Sharding Pattern

- Seperation of data into unique small pieces of db called shards
- Each shard has same schema, holding its own subset of data
- Sharding enables scaling
- Imrpove perf & reduce contention by spreading workload across shards
- Gain cloud power
  - Locate servers near geo zones
- DB divides with partition keys
- Keys should be static & not affected by data changes

- Benefits
  - Increase
    - Scalability
    - Availability
    - Performance
    - Security
    - Data Management

### Evaluate DB Sharding

- Benefits
  - Distributed dbs , Ready for k8s
  - Horizontal and Functional Partitioning
  - Sharding, increase scalabilit, availability & managability
  - Master-Master arch with peer to peer column db (cassandra)
- Drawbacks
  - CAP theorom, Sacrifice strong consistency for partition tolerance
  - Cross-service queries
  - Complex Join Operations
  - Lack of read-write db seperations
  - Distributed TX management req'd

### Problem

- Cross-Service Queries & Write Commands on Dist'd Scaled DB
  - Bottleneck & difficult to implement

- Considerations
  - X-service queries that retrieve data from multiple msvcs?
  - Seperate read & write ops at scale?
- Problems
  - X-Service Queries with complex join ops
  - Read & Write ops at scale
  - Dist'd TX management
- Solutions
  - MSvcs Data Query Pattern & Best Practices
  - Materialzied View Pattern
  - CQRS Pattern
  - Event Sourcing Pattern
