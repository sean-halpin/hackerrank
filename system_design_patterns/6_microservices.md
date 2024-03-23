# Microservices

- Small independant loosely couples services
- Each service, one codebase
- MicroServices communicate via APIs
- Can be deployed independantly and autonomously
- Microservices can have different tech/frameworks
- Each MS has its own DB, not shared with another. 

Martin Fowler
- MS is a srtle to dev a single app as a suite of small services
- Each running own process and comms via lightweight mechanisms
  - HTTP, gRPC, GraphQL
- Built around business capabilities
- Owned by small, self contained teams
- Fits within a bounded context

![MS](./media/microservices.png)

# Characteristics

- Componentization via Services
- Organised around business capabilities
- Products not Projects
- Smart endpoints and dumb pipes
  - Endpoints(Apps/Services) can be complicated
  - Pipes(Message passing) should be simple
- Decentralized Governance
  - Empowers teams to choose their own tech 
- Decentralized Data Management
  - Empowers teams to choose their own models, schema, api, etc
- Infrastructure automation
  - develop/test/deploy
- Design for failure

# Benefits

- Agility, Innovation, and Time-to-market
  - Microservices enable rapid development and innovation, accelerating time-to-market for new features.
- Flexible Scalability
  - Microservices allow independent scaling, enabling efficient resource allocation by scaling out specific services rather than the entire application.
- Small, Focused Teams
  - Microservices facilitate small feature teams to build, test, and deploy services independently.
- Small and Separated Code Base
  - Microservices have minimal dependencies, as they do not share code or data stores with other services. This separation simplifies adding new features.
- Easy Deployment
  - Microservices support continuous integration and continuous delivery, allowing for quick experimentation and easy rollback if necessary.
- Technology Agnostic
  - Right Tool for the Job: Small teams can choose the technology stack that best suits each microservice, enabling flexibility and leveraging the right tools for specific tasks.
- Resilience and Fault Isolation
  - Microservices are fault-tolerant and implement resilience patterns such as retry and circuit breaking, ensuring robustness in the face of failures.
- Data Isolation
  - Microservices maintain separate databases, facilitating easier schema updates as changes only affect a single database, enhancing data isolation and management.

# Challenges

- Complexity: Microservices introduce complexity due to the increased number of services. Managing deployments and communications becomes challenging with numerous microservices.
- Network Problems and Latency: Inter-service communication in microservices architecture requires handling network issues and latency. Chains of services can exacerbate latency and lead to chatty API calls.
- Development and Testing: Developing and testing end-to-end processes in microservices architectures is more challenging compared to monolithic ones due to the distributed nature of the system.
- Data Integrity: Each microservice has its own data persistence, leading to challenges in maintaining data consistency. Eventual consistency is often followed to address this challenge.
- Deployment: Deployments in microservices architectures require significant investment in DevOps automation processes and tools. The complexity of managing multiple microservices can be overwhelming for manual deployment.
- Logging & Monitoring: Distributed systems necessitate centralized logging to aggregate logs for monitoring and troubleshooting. A centralized view of the system helps identify sources of problems.
- Debugging: Debugging across multiple microservices is challenging as debugging through a local IDE is not feasible across dozens or hundreds of services. Alternative debugging strategies are required.