# cleaning.py
# Handles data cleaning operations

from pyspark.sql import DataFrame

def remove_nulls(df: DataFrame, columns: list):
    """
    Removes rows with null values in the specified columns.
    """
    return df.na.drop(subset=columns)
