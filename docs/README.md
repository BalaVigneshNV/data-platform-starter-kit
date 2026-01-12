# Documentation Index

Welcome to the Data Platform Starter Kit documentation. This guide covers all aspects of the project.

## Getting Started

- **[Prerequisites](setup/prerequisites.md)** - System requirements and dependencies
- **[Local Development Setup](setup/local_development.md)** - Quick start with Docker Compose
- **[Azure Cloud Setup](setup/azure_setup.md)** - Deploy to Azure cloud
- **[CI/CD Setup](setup/ci-cd-setup.md)** - Configure GitHub Actions pipelines

## Architecture

- **[Architecture Overview](architecture/overview.md)** - High-level system design
- **[Medallion Architecture](architecture/medallion_layers.md)** - Bronze, Silver, Gold pattern
- **[Data Flow](architecture/data_flow.md)** - Data flow through layers

## Pipelines

- **[Bronze Layer](pipelines/bronze_layer.md)** - Raw data ingestion
- **[Silver Layer](pipelines/silver_layer.md)** - Data cleaning and validation
- **[Gold Layer](pipelines/gold_layer.md)** - Analytics-ready data
- **[Data Quality Framework](pipelines/data_quality.md)** - Quality rules and validation

## Operations

- **[Monitoring & Observability](operations/monitoring.md)** - Dashboards and alerts
- **[Troubleshooting](operations/troubleshooting.md)** - Common issues and solutions
- **[Cost Optimization](operations/cost_optimization.md)** - Reduce cloud costs
- **[Scaling Guide](operations/scaling.md)** - Scale for production

## Examples

- **[E-Commerce Example](examples/e_commerce_example.md)** - End-to-end example
- **[Financial Reporting](examples/financial_reporting.md)** - Financial use case
- **[Customer 360](examples/customer_360.md)** - Unified customer view

## Contributing

- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute
- **[Code Style](../CONTRIBUTING.md#code-style-guide)** - Coding standards
- **[Testing](../CONTRIBUTING.md#testing-guidelines)** - Test requirements

## Key Concepts

### Medallion Architecture
Data is organized into three progressive quality layers:
- **Bronze**: Raw, immutable data directly from sources
- **Silver**: Cleansed, validated, standardized data
- **Gold**: Business-ready, aggregated, analytics data

### Delta Lake
All data is stored in Delta Lake format for:
- ACID transactions
- Schema enforcement
- Time travel capabilities
- Unified batch and streaming

### Data Quality
Comprehensive validation at Silver layer ensures:
- Schema correctness
- Data completeness
- Value constraints
- Business rule validation

## Quick Links

- [GitHub Repository](https://github.com/BalaVigneshNV/data-platform-starter-kit)
- [Issues & Discussions](https://github.com/BalaVigneshNV/data-platform-starter-kit/issues)
- [License](../LICENSE)

## Table of Contents by Topic

### For Data Engineers
- How to build Bronze layer pipelines
- Implementing Silver layer transformations
- Optimizing Gold layer queries
- Testing pipelines

### For DevOps/Platform Engineers
- Infrastructure as Code (Terraform)
- CI/CD pipeline setup
- Monitoring and alerting
- Cost optimization

### For Data Analysts
- Consuming Gold layer data
- Creating analytical views
- Building dashboards
- Understanding data lineage

### For Data Scientists
- Accessing clean Silver layer data
- Feature engineering patterns
- Integration with ML pipelines
- Model serving patterns

## Getting Help

1. **Check Documentation**: Start with relevant sections above
2. **Search Issues**: Look for similar problems on GitHub
3. **Open an Issue**: Report bugs or request features
4. **Start a Discussion**: Ask questions and get community help

## Development Workflow

```bash
# Clone repository
git clone https://github.com/BalaVigneshNV/data-platform-starter-kit.git

# Setup local environment
cd data-platform-starter-kit
docker-compose up -d

# Run sample pipeline
python scripts/run_sample_pipeline.py

# Run tests
pytest tests/ -v
```

## Documentation Status

- ✅ Architecture documentation
- ✅ Setup guides
- 🔄 Example implementations (in progress)
- 🔄 Advanced patterns (planned)
- 📋 Performance tuning (planned)

Last updated: January 2026
