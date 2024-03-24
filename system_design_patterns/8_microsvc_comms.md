# Microservice Communication Patterns

- Sync vs Async
- RESTful API design
- GraphQL
  - flexible structured comms
- gRPC
  - High performance internal comms
- WebSocket
  - 2 way comms

# Problem 

 - Direct client to svc comms
   - Chatty clients
   - Hard to manage invocations from client app

![MSCon](./media/microsvc_considerations.png)

# Solutions

- Well defined API Design
- Microservices Comm Patterns

# Steps
- Well defined Restful API design for svcs
- API Gateway
- BFF
- Pub/Sub

# MicroSvc Comms

- Challenge, inter-service comms
  - AMPQ, HTTP, gRPC
- Isolate business into microsvcs as much as possible
- Use async comms between internal svcs as much as possible
- Create well-defined APIs for inter-svc comms
- Monolith inter-process method alls beomce APIs in microsvcs
- Groups some ops and expose aggregated APIs that cover several calls from many sources
- Smart endpoints & dumb pipes
  - microsvcs should be loose couple and expose endpoints with restful apis in order to provide end-to-end use cases
- Sync vs Async
  - Sync 
    - Request/Response
  - Async
    - AMPQ

# Sync & Async Comms

![sync_async](./media/sync_async.png)

## Sync

- Http or gRPC
  - Request/Response
  - Thread blocks while waiting

## Async

- Client doesn't block or wait for response
- AMQP KAFKA RABBITMQ
- Async Comms can be
  - one to one (queue model)
  - one to many (topic model)

- One to One
  - Single producer and single reciever
- One to Many
  - Multiple recievers
    - Each message can be processed by zero to multiple recievers
- Event bus or msg broker system is publishing events berween microsvcs & recievers subscribe in an async way
- Pub/Sub mechanism used in event driven microsvcs arch

## Request driven or Event driven 

- Request/response
  - http & rest
  - gRPC & GraphQL
- Push and real time
  - Websocket protocol
- Pull Communication
  - HTTP & AMPQ (short/long polling)
- Event driven comm
  - Publish/Subsribe model

### Req/Response

- For sync, use http & rest protocols
- Expose APIS using http & rest
  - REST uses HTTP verbs GET/POST/PUT/PATCH
- If comms are between microsvcs, use gRPC, high perf & low latency
- Use Graphql alt to REST APIS
  - GraphQL we can structure the requested response
    - efficiency

### Push/Pull Comms

- Push & real-time comms based on http/web socket protocol
- Build 2way comms such as chat apps and steaming dashboards with websocket apis
- Pull comm based on HTTP and AMPQ 
  - called polling and its basically like refreshing inbox each few mins
    - potential waste of bandwidth
    - open/close connections is expensive
    - doesnt scale well
    - apis like twitter will have limits on api calls
  
### Event driven with Pub/Sub

- Microservices don't call one another
  - Instead create events & consume from a message broker system
  - AMPQ, Kafka/Rabbit
  - Pub/Sub Pattern
  - Producer doesn't know about consumer services & vice versa
  - Services decoupled 
- No clear orchestrator
  - Increased complexity debugging and controlling flow

# Designing HTTP RESTful APIs for MSvcs

- For req/resp we should use REST when deigning APIs
- How?
  - Well defined API is important
  - Should be efficient and not chatty
  - Well documented and versioned
- 2 types of APIs for sync comm in msvcs
  - Public APIs
    - Use RESTful APIs over HTTP
      - JSON payloads
  - Backend APIs
    - Inter-service comms can result in a lot of network traffic
      - Serialization speed & payload speed more important
      - Using gRPC is mandatory for increase in network performance

# Compare REST to gPRC

- REST uses HTTP & req/resp as JSON object
- API interfacts design based on HTTP verbs like GET/PUT/POST/DELETE
- gRPC remote procedure call
  - invoke external system with binary network protocols
  - payloads unreadable but fast

# RESTful apis

- lightweight, extensible & simple 
- Representation State Transfer
  - Roy Fielding PhD in 2000
- REST allows apps to communicate with each other by carrying JSON data between client and serve

- REST characteristics
  - Stateless
  - Uniform Interface
  - Cacheable
  - Client-Server
  - Layered
  - Code on Demand

- RESTful systems 
  - comms over http 

- Richardson maturity Model
  - 0 one URI all ops are POST
  - 1 URI per resource
  - 2 HTTP methods to define operations on resource (GET/POST/DELETE)
  - 3 hypermedia (dynamic resource links in response)

- HTTP methods
  - GET
    - retrieve info
  - HEAD
    - retrieve resource header
  - POST
    - submit data to server
  - PUT
    - save an object at the location
  - DELETE
    - delete object at the location
  - PATCH
    - update single piece of data(partial update)

# Design RESTful API for single microservice

- Focus on business entities
  - organise resources in line with business entities and expose via APIs


client - HTTP GET /products (200 OK) > Product - DB

- rule 1 
  - resource URIs based on nouns
    - http://e-shop.com/products
- rule 2
  - every resource has an identifier
    - http://e-shop.com/products/4
- rule 3
  - rest apis use JSON
    - http://e-shop.com/products/4
    - {"productId": 4, "name": "iPhone"}
- rule 4
  - REST APIS perform operations on resource with HTTP Verbs