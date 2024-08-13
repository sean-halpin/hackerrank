# Kafka Case Studies

## Partition Count and Replication Factor

Very important to get right from start
They impact the perf and durability of the system overall

- If partition count increases during topic lifecycle, you break the key ordering gaurantees
- If replication factor increases during topic lifecycle, you put pressure on cluster and could have an unexpected performance decrease

- Each partition can handle a few MB/s
  - More partititons means higher parallelism and throughput
    - Enables more consumers in a group to scale (max consumer count == partition count)
    - Enables leverage of more brokers in larger cluster
      - But more elections when node goes down
      - But more files opened by Kafka

Guidelines: 
- Partition Count
  - Small cluster; 3*broker count
  - Big cluster; 6*broker count
  - Increase this number for as many consumers as needed during peak load
  - Adjust for producer throughput
- Replication Factor
  - 2,3,4 ; Higher in production
  - Higher replication factor == Better system durability
  - Better availability of system (N - min.insysnc.replicas if producer acks=all)
  - But, more replication (higher latency if acks=all)
  - But, more disk space req'd

Limits
- 200k partitions zookeeper hard limit per cluster
  - 4k per broker (soft limit)
- KRaft potentially million of partitions

Topic Naming Conventions
- Create your own guidelines
  - MessageType.DataSet.Data.Format
    - e.g. streaming.movies.imdb.json