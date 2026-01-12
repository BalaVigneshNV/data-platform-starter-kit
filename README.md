# 🚀 Data Platform Starter Kit

A **production-ready, open-source data platform** implementing medallion architecture on Azure with comprehensive observability, data quality, and DevOps practices.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Spark 3.3+](https://img.shields.io/badge/apache%20spark-3.3+-orange.svg)](https://spark.apache.org/)
[![Azure](https://img.shields.io/badge/cloud-azure-0078d4.svg)](https://azure.microsoft.com/)

## 📋 Overview

This starter kit provides a complete reference implementation of a modern data platform that organizations can clone, configure, and deploy in days rather than months. It demonstrates enterprise-level patterns while remaining accessible to the community.

### Key Features

✅ **Medallion Architecture** - Bronze → Silver → Gold layer pattern for data organization
✅ **Production-Ready** - ACID transactions, data lineage, and audit trails
✅ **Comprehensive Data Quality** - Built-in validation framework with Great Expectations
✅ **Full Observability** - Logging, metrics, dashboards, and alerting
✅ **Enterprise DevOps** - CI/CD pipelines, IaC with Terraform, automated testing
✅ **Local Development** - Docker Compose setup for quick local testing
✅ **Open Source** - MIT licensed, community-driven, extensible architecture

## 🏗️ Architecture

The medallion architecture organizes data into three progressive quality layers:

- **Bronze Layer**: Raw data ingestion from multiple sources
- **Silver Layer**: Cleansed, validated, and standardized data
- **Gold Layer**: Business-ready, aggregated analytics data

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.9+
- Azure CLI
- Git

### Local Development (5 minutes)

```bash
# Clone the repository
git clone https://github.com/BalaVigneshNV/data-platform-starter-kit.git
cd data-platform-starter-kit

# Start local development environment
docker-compose up -d

# Run sample pipeline
python scripts/run_sample_pipeline.py

# View results
# Spark UI: http://localhost:4040
# Airflow UI: http://localhost:8080
```

### Azure Cloud Deployment (30 minutes)

```bash
# Configure Azure credentials
az login

# Navigate to infrastructure directory
cd infrastructure/terraform

# Initialize and deploy
terraform init
terraform plan -var-file=env/dev.tfvars
terraform apply
```

## 📁 Project Structure

```
data-platform-starter-kit/
│
├── src/                    # Source code
│   ├── bronze/            # Bronze layer pipelines
│   ├── silver/            # Silver layer pipelines
│   ├── gold/              # Gold layer pipelines
│   ├── utils/             # Shared utilities
│   └── common/            # Common transformations
│
├── tests/                 # Test suite
│   ├── unit/             # Unit tests
│   ├── integration/       # Integration tests
│   └── fixtures/         # Test data
│
├── dags/                  # Airflow DAGs
│   ├── bronze_ingestion_dag.py
│   ├── silver_processing_dag.py
│   └── gold_aggregation_dag.py
│
├── infrastructure/        # Infrastructure as Code
│   └── terraform/        # Terraform modules
│
├── .github/              # GitHub workflows
│   └── workflows/        # CI/CD pipelines
│
├── docs/                 # Documentation
│   ├── architecture/     # Architecture guide
│   ├── setup/           # Setup instructions
│   ├── pipelines/       # Pipeline documentation
│   └── operations/      # Operations guide
│
├── scripts/              # Utility scripts
├── config/               # Configuration files
├── docker-compose.yml    # Local dev environment
├── Dockerfile            # Docker image
├── requirements.txt      # Python dependencies
└── LICENSE              # MIT License
```

## 🎯 Use Cases

- **E-Commerce Analytics** - Real-time inventory, customer patterns, revenue analytics
- **Financial Reporting** - Multi-currency transactions, compliance reporting
- **Customer 360** - Unified customer view from multiple sources
- **Supply Chain Optimization** - End-to-end visibility and forecasting

## 📚 Documentation

- **[Setup Guide](docs/setup/README.md)** - Local and cloud deployment
- **[Architecture Guide](docs/architecture/overview.md)** - System design
- **[Pipeline Documentation](docs/pipelines/README.md)** - Layer-by-layer details
- **[Operations Guide](docs/operations/monitoring.md)** - Monitoring and troubleshooting
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Cloud** | Azure | Latest |
| **Storage** | ADLS Gen2 + Delta Lake | Latest |
| **Compute** | Apache Spark | 3.3+ |
| **Orchestration** | Apache Airflow | 2.5+ |
| **IaC** | Terraform | 1.3+ |
| **Language** | Python | 3.9+ |
| **Testing** | pytest + Great Expectations | Latest |
| **Monitoring** | Azure Monitor + Log Analytics | Latest |
| **CI/CD** | GitHub Actions | Latest |

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/BalaVigneshNV/data-platform-starter-kit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/BalaVigneshNV/data-platform-starter-kit/discussions)

---

**⭐ If you find this helpful, please consider starring the repository!**
