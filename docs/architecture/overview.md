# Data Platform Architecture Overview

## System Architecture

The Data Platform Starter Kit implements a modern data lakehouse architecture on Azure with three key components:

### 1. Data Lake (Storage)
- **Azure Data Lake Storage (ADLS) Gen2** - Hierarchical namespace for organized data storage
- **Delta Lake** - ACID transactions and schema enforcement
- **Partitioned Structure** - Bronze → Silver → Gold organization

### 2. Compute Engine (Processing)
- **Apache Spark** - Distributed data processing
- **PySpark** - Python API for Spark
- **Databricks** - Managed Spark platform (optional)
- **Azure Synapse** - Integration option

### 3. Orchestration (Scheduling)
- **Apache Airflow** - Workflow orchestration
- **Azure Data Factory** - Cloud-native orchestration
- **DAG-based** - Dependency management and scheduling

## Data Flow Architecture

```
External Sources
       │
       ├─→ APIs
       ├─→ Databases
       ├─→ Files (CSV, JSON, Parquet)
       └─→ Streaming (Kafka, Event Hub)
       │
       ▼
┌──────────────────────────────────────────┐
│         DATA INGESTION LAYER              │
│  (Python Scripts, Data Factory Pipelines) │
└──────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│    BRONZE LAYER (Raw Data)                │
│  - Append-only Delta tables               │
│  - Full history & audit trails            │
│  - Metadata tracking                      │
│  Path: /bronze/source_system/table_name   │
└──────────────────────────────────────────┘
       │
       ▼ (PySpark Transformations)
┌──────────────────────────────────────────┐
│    SILVER LAYER (Cleaned Data)            │
│  - Data quality validation                │
│  - Deduplication & standardization        │
│  - SCD Type 2 dimensions                  │
│  Path: /silver/validated/schema/table     │
└──────────────────────────────────────────┘
       │
       ▼ (Business Logic)
┌──────────────────────────────────────────┐
│    GOLD LAYER (Analytics Ready)           │
│  - Facts & dimensions                     │
│  - Pre-aggregated KPIs                    │
│  - Domain-specific marts                  │
│  Path: /gold/domain/mart/table            │
└──────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│   CONSUMPTION LAYER                       │
│  - Power BI dashboards                    │
│  - SQL analytical queries                 │
│  - ML feature stores                      │
│  - Custom applications                    │
└──────────────────────────────────────────┘
```

## Component Details

### Bronze Layer Responsibilities
- Ingest raw data from all sources
- Maintain append-only audit trail
- Track ingestion metadata
- Handle schema evolution
- Error quarantine for failed records

### Silver Layer Responsibilities
- Implement data quality rules
- Standardize data formats
- Deduplicate records
- Handle slowly changing dimensions
- Enrich with reference data
- Create audit reports

### Gold Layer Responsibilities
- Create fact tables from transactions
- Build dimension tables from entities
- Implement slowly changing dimensions
- Calculate KPIs and metrics
- Optimize for specific use cases
- Enable self-service analytics

## Infrastructure Components

### Storage
```
ADLS Gen2 Structure:
adlsaccount.dfs.core.windows.net
├── bronze/
│   ├── customer_system/
│   ├── sales_system/
│   └── inventory_system/
├── silver/
│   ├── validated/
│   ├── quarantine/
│   └── audit/
└── gold/
    ├── facts/
    ├── dimensions/
    └── marts/
```

### Compute Clusters
- **Development**: Auto-scaling, low-cost
- **Staging**: Production-like configuration
- **Production**: High availability, monitoring

### Network & Security
- **VNet Integration** - Private connectivity
- **Key Vault** - Secrets management
- **RBAC** - Role-based access control
- **Encryption** - Data at rest and in transit

## Data Quality Framework

Quality validation occurs at Silver layer:

1. **Schema Validation**
   - Column existence
   - Data type correctness
   - Null constraints

2. **Value Validation**
   - Range checks
   - Pattern matching (regex)
   - Enum validation

3. **Business Rules**
   - Referential integrity
   - Cross-field validation
   - Custom business logic

4. **Freshness Checks**
   - Ingestion SLA monitoring
   - Data staleness alerts

## Monitoring & Observability

### Logging
- Application logs → Log Analytics
- Pipeline execution logs → Application Insights
- Audit logs → Storage Account

### Metrics
- Pipeline execution time
- Data quality scores
- Data freshness
- Cluster utilization
- Cost per pipeline

### Alerts
- Pipeline failures
- Data quality threshold breaches
- SLA violations
- Cost anomalies

## Security Architecture

```
┌─────────────────────────────────────┐
│   Azure AD (Authentication)         │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│   Key Vault (Secrets)               │
│   - Database credentials            │
│   - API keys                        │
│   - Storage connection strings      │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│   RBAC (Authorization)              │
│   - Service Principal               │
│   - Managed Identity                │
│   - User Roles                      │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│   Data Lake Access                  │
│   - ADLS Gen2 Permissions           │
│   - Delta Lake Table ACLs           │
└─────────────────────────────────────┘
```

## Performance Considerations

### Partitioning Strategy
- **Bronze**: Partition by ingestion date
- **Silver**: Partition by business key date
- **Gold**: Partition by reporting period

### Optimization Techniques
- Z-order clustering for hot columns
- Predicate pushdown for early filtering
- Column pruning in SELECT
- Caching frequently accessed data

### Cost Optimization
- Lifecycle policies: Hot → Cool → Archive
- Spot instances for non-critical jobs
- Right-sizing compute resources
- Query result caching
- Scheduled cluster shutdown

## Scalability

The platform scales:
- **Horizontally**: Add more compute nodes
- **Vertically**: Increase node size
- **Elastically**: Auto-scale based on demand
- **Incrementally**: Add new sources easily

## Disaster Recovery

- **Backup Strategy**: Daily snapshots of critical tables
- **Replication**: Geo-redundant storage
- **RTO/RPO**: Recovery time/point objectives defined
- **Testing**: Regular DR drills

## Related Documentation

- [Medallion Architecture Details](medallion_layers.md)
- [Data Flow Diagrams](data_flow.md)
- [Setup Guide](../setup/local_development.md)
- [Operations Guide](../operations/monitoring.md)
