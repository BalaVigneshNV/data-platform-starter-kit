"""
Spark Utilities Module

Provides helper functions for Spark session management, configuration,
and common DataFrame operations.
"""

from typing import Optional
from pyspark.sql import SparkSession
import logging

logger = logging.getLogger(__name__)


def get_spark_session(
    app_name: str = "DataPlatform",
    master: str = "local[*]",
    config: Optional[dict] = None
) -> SparkSession:
    """
    Get or create a Spark session with default configurations.
    
    Args:
        app_name: Application name for Spark session
        master: Spark master URL
        config: Additional Spark configurations
        
    Returns:
        SparkSession instance
    """
    builder = SparkSession.builder.appName(app_name).master(master)
    
    # Add default configurations
    default_config = {
        "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
        "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        "spark.sql.adaptive.enabled": "true",
        "spark.sql.adaptive.coalescePartitions.enabled": "true",
    }
    
    # Merge with user-provided config
    if config:
        default_config.update(config)
    
    for key, value in default_config.items():
        builder = builder.config(key, value)
    
    spark = builder.getOrCreate()
    logger.info(f"Spark session created: {app_name}")
    
    return spark


def write_delta_table(
    df,
    path: str,
    mode: str = "overwrite",
    partition_by: Optional[list] = None,
    optimize: bool = True
) -> None:
    """
    Write DataFrame to Delta Lake table.
    
    Args:
        df: PySpark DataFrame
        path: Delta table path
        mode: Write mode (overwrite, append, etc.)
        partition_by: Columns to partition by
        optimize: Whether to optimize table after write
    """
    writer = df.write.format("delta").mode(mode)
    
    if partition_by:
        writer = writer.partitionBy(*partition_by)
    
    writer.save(path)
    logger.info(f"Data written to Delta table: {path}")
    
    if optimize:
        spark = SparkSession.getActiveSession()
        spark.sql(f"OPTIMIZE DELTA `{path}`")
        logger.info(f"Optimized Delta table: {path}")


def read_delta_table(path: str, version: Optional[int] = None):
    """
    Read Delta Lake table.
    
    Args:
        path: Delta table path
        version: Specific version to read (time travel)
        
    Returns:
        PySpark DataFrame
    """
    spark = SparkSession.getActiveSession()
    
    if version is not None:
        df = spark.read.format("delta").option("versionAsOf", version).load(path)
    else:
        df = spark.read.format("delta").load(path)
    
    logger.info(f"Read Delta table: {path}")
    return df


def add_ingestion_metadata(df, source_name: str, ingestion_date: str):
    """
    Add ingestion metadata columns to DataFrame.
    
    Args:
        df: Input DataFrame
        source_name: Data source identifier
        ingestion_date: Ingestion timestamp
        
    Returns:
        DataFrame with metadata columns
    """
    from pyspark.sql.functions import lit, current_timestamp
    
    return df.withColumn("_source", lit(source_name)) \
        .withColumn("_ingestion_date", lit(ingestion_date)) \
        .withColumn("_processed_timestamp", current_timestamp())
