# Scale the Microservice Design

- Scalability is the number of requests an application can handle
- Measured by the number of requests it can support simultaneously 
- If no more can be handled, it has reached its limit
- To prevent downtime and reduce scale
  - We must scale
- Horizontal Scaling & Vertical Scaling both involve adding resources to computing infrastructe
  - Horizontal, Scale OUT
    - Scaling by adding more machines
    - Splitting load across many machines
      - Sclability AND reliability
    - Consider if we have state
      - Stateless 
        - Easy to scale out
      - Stateful
        - Like with database
          - Need to consider CAP theorom
  - Vertical, Scale UP
    - Scaling by adding more power, CPU/RAM/DISK
    - Code doesnt need to change
    - Hardware has a scalability limit

# Scale Cube

- Main benefits of microsvcs
  - Indepentant scale & deploy
- Dimensions of Scale Cube
  - X, Horizontal, duplication, Scale OUT
  - Y, functional decomposition, scale by splitting small services
  - Z, data partitioning, scale by splitting data Shards/Pods
- Combination of scaling dimensions possible for better results

- When scaling OUT/Horizontal
  - Do we have state?
    - No? , easy scaling, clonse app
    - Yes?
      - how can we manage the stateful data as we scale the app?
      - Consider CAP theorom

- What is the consistency level required?
  - Strict
    - When we save data, it should be seen immediately by all clients
  - Eventual Consistency
    - It's not important to be immediate
    - It may take some time
  - When scaling stateful svcs like databases we should split the data using sharding
    - Sharing is a way of partitioning and splitting database servers