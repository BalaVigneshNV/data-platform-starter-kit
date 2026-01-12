"""
Bronze Layer Ingestion Module

Handles raw data ingestion from multiple sources with complete metadata
tracking and audit trails.
"""

from typing import Dict, Any, Optional
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    current_timestamp,
    lit,
    col,
    monotonically_increasing_id
)
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class BronzeIngestion:
    """
    Handles ingestion of raw data into Bronze layer.
    """
    
    def __init__(self, spark: SparkSession):
        """
        Initialize BronzeIngestion.
        
        Args:
            spark: SparkSession instance
        """
        self.spark = spark
    
    def ingest_from_csv(
        self,
        source_path: str,
        table_name: str,
        delta_path: str,
        source_system: str,
        **read_options
    ) -> DataFrame:
        """
        Ingest CSV data into bronze layer.
        
        Args:
            source_path: Path to CSV file
            table_name: Logical table name
            delta_path: Target Delta Lake path
            source_system: Source system identifier
            **read_options: Additional Spark read options
            
        Returns:
            Ingested DataFrame with metadata
        """
        try:
            # Read CSV with default options
            df = self.spark.read.csv(
                source_path,
                header=True,
                inferSchema=True,
                **read_options
            )
            
            # Add ingestion metadata
            df = self._add_ingestion_metadata(df, source_system, source_path, table_name)
            
            # Write to Delta Lake (append-only)
            df.write.format("delta").mode("append").save(delta_path)
            
            logger.info(
                f"Ingested {df.count()} records from {source_path} to {table_name}"
            )
            return df
            
        except Exception as e:
            logger.error(f"Error ingesting CSV from {source_path}: {str(e)}")
            raise
    
    def ingest_from_parquet(
        self,
        source_path: str,
        table_name: str,
        delta_path: str,
        source_system: str,
    ) -> DataFrame:
        """
        Ingest Parquet data into bronze layer.
        
        Args:
            source_path: Path to Parquet file
            table_name: Logical table name
            delta_path: Target Delta Lake path
            source_system: Source system identifier
            
        Returns:
            Ingested DataFrame with metadata
        """
        try:
            df = self.spark.read.parquet(source_path)
            df = self._add_ingestion_metadata(df, source_system, source_path, table_name)
            df.write.format("delta").mode("append").save(delta_path)
            
            logger.info(
                f"Ingested {df.count()} records from {source_path} to {table_name}"
            )
            return df
            
        except Exception as e:
            logger.error(f"Error ingesting Parquet from {source_path}: {str(e)}")
            raise
    
    @staticmethod
    def _add_ingestion_metadata(
        df: DataFrame,
        source_system: str,
        source_path: str,
        table_name: str
    ) -> DataFrame:
        """
        Add metadata columns for audit trail.
        
        Args:
            df: Input DataFrame
            source_system: Source system identifier
            source_path: Source file path
            table_name: Target table name
            
        Returns:
            DataFrame with metadata columns
        """
        return df.withColumn("_ingestion_timestamp", current_timestamp()) \
            .withColumn("_source_system", lit(source_system)) \
            .withColumn("_source_path", lit(source_path)) \
            .withColumn("_table_name", lit(table_name)) \
            .withColumn("_ingestion_date", lit(datetime.now().date())) \
            .withColumn("_record_id", monotonically_increasing_id())


def ingest_customer_data(
    spark: SparkSession,
    source_path: str,
    target_delta_path: str
) -> None:
    """
    Example function to ingest customer data.
    
    Args:
        spark: SparkSession instance
        source_path: Path to customer CSV
        target_delta_path: Target Delta path
    """
    ingestion = BronzeIngestion(spark)
    ingestion.ingest_from_csv(
        source_path=source_path,
        table_name="customer_raw",
        delta_path=target_delta_path,
        source_system="customer_system"
    )
