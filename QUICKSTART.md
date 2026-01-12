# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- Git

### Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/BalaVigneshNV/data-platform-starter-kit.git
cd data-platform-starter-kit

# 2. Start all services
docker-compose up -d

# 3. Wait for services to be ready (about 30 seconds)
docker-compose ps

# 4. Access the services
# Spark Master UI:  http://localhost:8080
# Airflow UI:       http://localhost:8080  (user: airflow, password: airflow)
# Jupyter:          http://localhost:8888
```

### Verify Installation

```bash
# Check all services are running
docker-compose ps

# Expected output:
# NAME                STATUS              PORTS
# spark-master        Up 30s              7077/tcp, 0.0.0.0:4040->4040/tcp, 0.0.0.0:8080->8080/tcp
# spark-worker        Up 30s              0.0.0.0:8081->8081/tcp
# postgres            Up 30s              0.0.0.0:5432->5432/tcp
# airflow-webserver   Up 15s              0.0.0.0:8080->8080/tcp
# airflow-scheduler   Up 15s
# jupyter             Up 10s              0.0.0.0:8888->8888/tcp
```

### Run Sample Pipeline

```bash
# Submit a sample Spark job
docker-compose exec spark-master spark-submit \\
    --class org.apache.spark.examples.SparkPi \\
    --master spark://spark-master:7077 \\
    --num-executors 2 \\
    --executor-cores 2 \\
    --executor-memory 1G \\
    /opt/spark/examples/jars/spark-examples.jar 100
```

### Access Jupyter Notebook

1. Open http://localhost:8888 in your browser
2. Create a new Python notebook
3. Run sample code:

```python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("Sample").getOrCreate()

# Create sample data
df = spark.createDataFrame(
    [(1, "Alice"), (2, "Bob"), (3, "Charlie")],
    ["id", "name"]
)

# Display data
df.show()
```

## 📁 Project Structure

```
data-platform-starter-kit/
├── src/                    # Source code
│   ├── bronze/            # Raw data ingestion
│   ├── silver/            # Data cleaning
│   ├── gold/              # Analytics data
│   └── utils/             # Shared utilities
├── tests/                 # Test suite
├── dags/                  # Airflow DAGs
├── docs/                  # Documentation
├── docker-compose.yml     # Local environment
├── requirements.txt       # Dependencies
└── README.md              # Main documentation
```

## 🔧 Common Commands

### Development

```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Format code
black src/ tests/
flake8 src/ tests/

# Type checking
mypy src/
```

### Docker

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f airflow-webserver

# Execute command in container
docker-compose exec spark-master spark-shell
```

### Data Pipeline

```bash
# Submit Spark job
docker-compose exec spark-master spark-submit src/bronze/ingestion.py

# Run Airflow DAG
docker-compose exec airflow-scheduler airflow dags list

# Trigger DAG run
docker-compose exec airflow-scheduler airflow dags trigger bronze_ingestion_dag
```

## 🌐 Service URLs (Local)

| Service | URL | Credentials |
|---------|-----|----------|
| Spark Master UI | http://localhost:8080 | N/A |
| Spark Worker UI | http://localhost:8081 | N/A |
| Airflow Web UI | http://localhost:8080 | airflow/airflow |
| Jupyter Notebook | http://localhost:8888 | No password |
| PostgreSQL | localhost:5432 | airflow/airflow |

## 📚 Next Steps

1. **Explore Documentation**: Read [docs/README.md](docs/README.md)
2. **Understand Architecture**: Check [docs/architecture/overview.md](docs/architecture/overview.md)
3. **Run Examples**: Follow example use cases in [docs/examples/](docs/examples/)
4. **Deploy to Cloud**: Follow [docs/setup/azure_setup.md](docs/setup/azure_setup.md)
5. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## ⚡ Performance Tips

```bash
# Allocate more resources to Spark
export SPARK_EXECUTOR_MEMORY=4G
export SPARK_DRIVER_MEMORY=2G

# Enable Spark UI history server
docker-compose exec spark-master \\
    /opt/spark/sbin/start-history-server.sh
```

## 🆘 Troubleshooting

### Service won't start
```bash
# Check logs
docker-compose logs <service-name>

# Restart services
docker-compose restart
```

### Port already in use
```bash
# Change port in docker-compose.yml
# Example: change "8080:8080" to "8090:8080"
```

### Out of memory
```bash
# Reduce Spark memory
env SPARK_EXECUTOR_MEMORY=1G docker-compose up
```

## 📖 Documentation

- **Full Documentation**: [docs/](docs/README.md)
- **Setup Guides**: [docs/setup/](docs/setup/README.md)
- **Architecture**: [docs/architecture/](docs/architecture/overview.md)
- **Examples**: [docs/examples/](docs/examples/)

## 💡 Tips for Success

1. **Read the Architecture Guide** - Understand the medallion pattern
2. **Start with Bronze Layer** - Learn data ingestion first
3. **Explore Sample Data** - Use provided examples
4. **Check Logs** - Docker logs are your friend
5. **Ask for Help** - Open an issue on GitHub

## 🚀 Next: Deploy to Azure

When ready to deploy to production:

```bash
# Configure Azure credentials
az login

# Deploy infrastructure
cd infrastructure/terraform
terraform init
terraform apply -var-file=env/dev.tfvars
```

See [docs/setup/azure_setup.md](docs/setup/azure_setup.md) for detailed instructions.

---

**Happy data engineering! 🎉**

Have questions? Open an issue on [GitHub](https://github.com/BalaVigneshNV/data-platform-starter-kit/issues)
