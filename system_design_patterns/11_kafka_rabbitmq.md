# Kafka & RabbitMQ

## Kafka

- OS streaming platform
- Designed to be horiz scalable, distributed, fault-tolerant
- Distributed pub/sub event streaming platform
- Publishers send messages to topics
  - Subcribers of a topic receive all messages published to the topic
- Event-driven Architecure
  - Kakfa is used as an event router
  - MSvcs publish and subscribe
- Distributed Arch
  - Horizontally scalable
  - Capable of trillions of events per day
  - Messages peristed on disk
  - Messages replicated within cluster
  - Built on top of Zookeeper Sync Service
- Key Components
  - Topics
  - Partitions
  - Brokers
  - Producer
  - Consumer
  - Zookeepr

## Kafka Benefits

- Reliability
  - Distributed
  - Partitioned
  - Replicated
  - Faul Tolerant
  - High Availability
- Scalability
  - Scaleseasily without downtime
- Durability
  - Distributed commit log
    - Persisted events on disk
    - Durability configurable
- Performance
  - High throughput for publishing and subscribing messages
  - Distributed event streaming capable of many many messages

## Kafka Use Cases

- Messaging
  - Message brokers are used to decouple services from one another
  - In event driven arch
    - Kafka used as an event router
    - MSvcs pub & sub messages
- Metrics
  - Used for operational monitoring
  - Aggregating stats
- Log Aggregation
  - Collect logs from multiple svcs
  - Collect to central place for analysis or monitoring
- Stream Processing
  - Used in processing pipelines with multiple stages
- Website Activity Tracking
- Event Sourcing
  - Given the compatibility for event driven arch & messaging

# Kafka Components

- Topic 
  - Messages/Events stored on topic
  - A named location items are published to
  - A new topic has its own log file
  - Producer writes to
- Partition
  - Each topic can be split into many partitions
  - Each partition has a set of messages which may be partition by some field
  - Smallest storage unit which contains messages
  - Consumer reads from
  - Offsets
    - Each msg has its own unique id an offset
  - Replicaction Factor
    - The number of partition copies in cluster

# Kafka Cluster Arch

- Can be set up to run across multiple servers, called kafka brokers
- Broker
  - A service which logically contains certain topics and certain partitions
  - Benefit of;
    - Replication
    - Fault Tolerance
    - High Availability
- Cluster consists of multiple brokers
- Brokers are stateless 
  - Use Zookeeper for maintaining their cluster state
- A Broker can handle 100ks+ of reads & writes per seconds
  - Without perf impact
- Kafka Leader Election can be done by zookeeper

- How are brokers manaaged and coordinated?
  - Management is handled by masted node
- Master node manage and maintains the workers nodes
- Zookeper is used for managing and coordinating kafka broker
  - Finds crashed or added brokers and manages lifecycle accordingly

# Kafka Core APIS

- Producers
  - Push data to brokers/topics
- Consumers
  - Subscribe to topics and process data
  - Manages messages concumed using partition offset
  - Offsets managed by zookeeper
- Streams
  - Transforming data from one topic to another
  - Allows apps to act as stream processor
  - Transforming input streams to output streams
- Connect API
  - Allows connector implementations
    - Pulling data from external systems into kafka
    - Collect metrics from servers to kafka topics

# Rabbit MQ

- RabbitMQ is a message broker software that implements AMQP
- It allows applications to communicate by sending & recx messages through queues
- RabbitMQ is a message queing system 
- Allows send and recv messages async
- Support multiple OSs & is Open Source
- Main Comps
  - Producer
  - Consumer
  - Message
  - Exchange
  - Binding 
  - FIFO

## Rabbit MQ Main components

- Producer
  - Source of messages
- Queue
  - Where msgs are stored
- Consumer
  - Server that takes msgs from queue
- Message
  - Data sent to queue
- Exchange
  - Structure that decides which queue to send messages
    - Depending on routing case
- Binding 
  - Link between exchange and queues
  - Binding Keys, routing Patterns, Fanout

- Queue Props
  - Queue name
  - Durable
    - If we want persistence
  - Exclusive
    - Queue will be used by only one connection & deleted after use
  - AutoDelete
    - Queue deleted after last consumer unsubscribes

## Rabbit MQ Exchange Types

- Exchanges control how msgs move from producers to queues
- Four Exchange Types
  - Direct
    - Single queue
  - Topic
    - Message sent to one or more queue(s) depending on msg subject
    - Variation of pub/sub
  - Fanout
    - When msgs sent to more than one queue, broadcasting
  - Header
    - Guided by header of message 
      - Attributes of header & queue match, msgs is sent to that queue

## Rabbit MQ Artchitectures

- Producers sends messages to an exchange
- Exchange has 2 sides
  - Receives messages from producers
  - Pushes them to queues
- Exchanges control routing of messages to queues
  - Accor. to exchange types
- RabbitMQ uses a push model
  - Push-based queues can overwhelm consumers is messages arrive faster than the consumers can process them.
  - Each consumer should configure a pre-fetch limit
  - Push model used to dist messages quickly & concurrently 
  - Msgs are processed in the same order they arrived to the queue