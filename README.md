# Spark eCommerce Data Pipeline Project

## 📌 Project Overview
This project demonstrates an end-to-end data processing pipeline using Apache Spark (PySpark) on Databricks.
It performs data cleaning, transformation, and analytics on eCommerce datasets to derive insights on sales, customers, and products.
The goal is to showcase industry-grade ETL development with Spark and GitHub portfolio readiness.


## 🏗️ Architecture
flowchart LR
  A[Raw E‑Commerce Data (CSV/JSON)] -->|Load| B[(Spark on Databricks)]
  B -->|Clean & Transform| C[Processed Data]
  C -->|Write| D[(HDFS / Delta Tables)]
  D -->|Consume| E[Analytics & BI Tools]

## Technology Stack
- **Apache Spark (PySpark)** – For data processing and transformations
- **Databricks** – Local/cloud notebook environment
- **Python** – PySpark scripts
- **Hadoop/HDFS** (optional) – For raw and processed data storage
- **GitHub** – For project version control and showcasing

  
## 🗂️ Project Structure
 ```text
.
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_data_transformation.ipynb
│   └── 04_analytics.ipynb
├── src/
│   ├── etl/
│   │   ├── ingestion.py
│   │   ├── cleaning.py
│   │   └── transformation.py
│   ├── utils/
│   │   └── io.py
│   └── main.py
├── data/
│   ├── raw/
│   └── processed/
├── tests/
│   └── test_transformations.py
├── Architecture Diagram/
│   └── spark_ecommerce_architecture.png
├── requirements.txt
├── README.md
└── LICENSE
 ```

## Dataset
- The project uses a real-world eCommerce dataset split into 9 CSV files, covering:
- Customers – customer profiles and contact details
- Products – product details, categories, and pricing
- Orders & Order Items – purchase transactions and quantities
- Payments – order payment details
- Reviews – customer feedback and ratings
- Geolocation – customer and seller location information
These files collectively represent the full sales process from order placement to delivery and review.



## 📜Project Workflow

### 1. Data Ingestion
- Raw data loaded into Databricks using Spark `read.csv` / `read.json`.
- Optionally stored in HDFS directories for persistence.

### 2. Data Cleaning
- Handle missing and null values.
- Remove duplicate records.
- Standardize data types and formats.
- Normalize text fields (product names, categories).

### 3. Data Transformation
- Derived columns, e.g., `TotalPrice = Quantity * Price`.
- Aggregation of sales by product, category, and customer.
- Spark transformations used: `filter()`, `select()`, `groupBy()`, `join()`, `withColumn()`.

### 4. Analytics & Insights
- Identify top-selling products and categories.
- Analyze customer purchase behavior.
- Monthly sales and revenue trends.
- Revenue per product category.

### 5. Output Storage
- Cleaned and transformed data saved to Databricks tables or HDFS directories (`/processed/sales`).
- Prepared datasets ready for visualization or further analytics.


## Challenges
- Efficient processing of large datasets in Spark.
- Cleaning null, missing, or malformed data.
- Maintaining schema consistency during transformations.


## Key Learning Outcomes
- Hands-on experience with **PySpark DataFrame API**.
- Implementing **end-to-end Spark ETL pipelines**.
- Managing **real-world eCommerce datasets**.
- Data transformation, aggregation, and scalable processing in Spark.


## 🔭 Future Improvements
- Streaming ingestion (Kafka) for near real-time processing.
- Delta Lake for ACID + time travel; optimize with Z-Order.
- Validation with Great Expectations or Deequ.
- Orchestration via Airflow or Databricks Jobs.
- BI: Connect to Power BI/Tableau for dashboards.
- Tests: Add unit tests for transformations (e.g., pytest).

 ## 📄 License
This project is licensed under the MIT License. See LICENSE for details.

