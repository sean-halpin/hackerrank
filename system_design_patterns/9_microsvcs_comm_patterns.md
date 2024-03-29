# MicroService Communication Patterns

- APII Gateway PAttern
- Gateway Routing Pattern
- Gateway Aggregation PAttern
- Gateway Offloading Pattern
- Backends for Frontend Pattern

## Problems

- Problems
  - Direct Client-to-Service Communication
  - Cause to chatty calls from client to service
  - Hard to manage invocations from client app with
  all different protocols (HTTP, GraphQL, gRPC,
  WebSocket)


- Solutions
   - Well-defined API Design
   - Microservices Communication Patterns
- Steps
  - Microservice Communications and Types
  - Well-defined RESTful API Design for services
  - Microservices Communication Patterns (API
  Gateway, BFF, Publish/Subscribe..)


  # API Gateway

  - Why
    - Manage client comms
    - Client code complexity, latency
    - Strong coupling between FE & BE
    - Cross-Cutting concerns
      - Authentication, Authorisation, Rate Limiting, SSL certifications, logging, monitoring, load balancing, circuit breaker
      - Difficult across multiple microservices
    - Protocol translation
      - If calls needed that require grpc + http etc
    - Async comms req's
      - Microservices may be using async comms to decouple comms

# Solution 

- Use API Gateway 
  - Single Point of Entry
  - Sits between clients and BE svcs
  - Can handle cross cutting concerns
    - LB, monitoring, logging, rate limits, protocol transalations, authentication, authorization

- Gateway Patterns
  - Routing pattern
  - Aggregation Pattern
  - Offloading Pattern

## Gateway Routing PAttern

- Single EP exposes multiple microservices
  - Decouples client from BE services
  - Client code can be kept simple
  - Blue/Green canary deployment easier
  - Use Application Layer 7 routing

## Aggregation Pattern

- Aggregate multiple requests to internal microservices, exposing a single request to clients
- Dispatch requests to multiple svcs & aggregate the results for client response
- Reduce network overhead

## Offloading Pattern

- Shared functionalities can be moved into centralized places
 - Authentication, Authorisation. SSL, Rate Limiting, Logging, Monitoring, Load Balancing
 - Cross cutting concerns for all microservices not a good idea
   - Increases deploy & maintenance complexity
 - Gateway offloading pattern offers to manage all those cross-cutting concerns into api gateways. 

 