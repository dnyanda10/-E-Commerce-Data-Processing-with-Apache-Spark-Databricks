# ingestion.py
# Handles loading CSV data into Spark DataFrames

from pyspark.sql import SparkSession

def load_csv(spark, file_path, header=True, infer_schema=True):
    """
    Loads a CSV file into a Spark DataFrame.
    """
    return spark.read.csv(file_path, header=header, inferSchema=infer_schema)
