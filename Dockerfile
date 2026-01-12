FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    git \\
    curl \\
    openjdk-11-jre-headless \\
    scala \\
    && rm -rf /var/lib/apt/lists/*

# Set Java home
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Copy requirements
COPY requirements.txt requirements-dev.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy application code
COPY . .

# Create directories
RUN mkdir -p logs warehouse metastore_db

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV SPARK_HOME=/usr/local/lib/python3.10/site-packages/pyspark
ENV PYSPARK_PYTHON=/usr/local/bin/python
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/python

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Default command
CMD ["bash"]
