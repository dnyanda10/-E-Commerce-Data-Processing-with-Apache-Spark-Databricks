# analytics.py
# Handles analytics and aggregations

from pyspark.sql import DataFrame

def top_n_products(df: DataFrame, n=10):
    """
    Returns top N products by sales.
    """
    return df.groupBy("ProductID").count().orderBy("count", ascending=False).limit(n)
