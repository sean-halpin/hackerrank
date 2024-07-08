# Loki

Loki is a horizontally scalable, highly available, and multi-tenant log aggregation system. It is designed to be used with Grafana for efficient log storage and querying.

To get started with Loki, you need to configure a few essential options:

1. **Storage Backend**: Loki supports various storage backends, such as local disk, Amazon S3, Google Cloud Storage, and more. Choose the one that suits your needs and configure it accordingly.

2. **Indexing**: Loki uses an indexing mechanism to efficiently query logs. You can configure the indexing strategy based on your requirements. Options include label-based indexing, label-value indexing, and more.

3. **Retention**: Specify how long you want to retain logs in Loki. This can be configured based on time or size.

4. **Authentication and Authorization**: Loki supports various authentication and authorization mechanisms, such as OAuth, LDAP, and JWT. Configure the appropriate mechanism to secure your logs.

# Promtail

Promtail is an agent that collects logs from various sources and sends them to Loki for storage. It is commonly used with Loki to scrape logs from applications, containers, and other log sources.

To set up Promtail with Loki, you need to:

1. **Configure Targets**: Specify the log sources that Promtail should scrape. This can include log files, systemd journal, Docker containers, and more.

2. **Labels**: Assign labels to the logs collected by Promtail. These labels can be used for filtering and querying logs in Loki.

3. **Scraping Configuration**: Define the scraping configuration for each log source. This includes specifying the log file path, log format, and any additional parsing or filtering rules.

4. **Shipper Configuration**: Configure the shipper options, such as the Loki endpoint, authentication details, and batch size.

By setting up Promtail to collect logs and ship them to Loki, you can effectively centralize and query your logs using Grafana.
