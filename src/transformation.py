# transformation.py
# Handles data transformation operations

from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def rename_columns(df: DataFrame, col_map: dict):
    """
    Renames columns in the DataFrame.
    """
    for old_name, new_name in col_map.items():
        df = df.withColumnRenamed(old_name, new_name)
    return df
