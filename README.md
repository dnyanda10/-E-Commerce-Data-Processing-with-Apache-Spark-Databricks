# Spark eCommerce Data Pipeline Project

## 📌 Project Overview
This project demonstrates an end-to-end data processing pipeline using Apache Spark (PySpark) on Databricks.
It performs data cleaning, transformation, and analytics on eCommerce datasets to derive insights on sales, customers, and products.
The goal is to showcase industry-grade ETL development with Spark and GitHub portfolio readiness.

--- 

## 🏗️ Architecture
 ```text
flowchart LR
  A[Raw E‑Commerce Data (CSV/JSON)] -->|Load| B[(Spark on Databricks)]
  B -->|Clean & Transform| C[Processed Data]
  C -->|Write| D[(HDFS / Delta Tables)]
  D -->|Consume| E[Analytics & BI Tools]
 ```
-----

## Technology Stack
- **Apache Spark (PySpark)** – For data processing and transformations
- **Databricks** – Local/cloud notebook environment
- **Python** – PySpark scripts
- **Hadoop/HDFS** (optional) – For raw and processed data storage
- **GitHub** – For project version control and showcasing

----

## 🗂️Project Structure
 ```text
.
├── Architecture Diagram/
│   └── spark_ecommerce_architecture.png
├── DataSet/                       # Raw Olist CSVs (9 files)
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
├── Notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_data_transformation.ipynb
│   └── 04_analytics.ipynb
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── transformation.py
│   └── analytics.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

 ```
---- 

## 📊Dataset
The project uses the Olist eCommerce dataset split into 9 CSV files (folder: DataSet/). They cover the full sales lifecycle from order placement to delivery and review.
| Domain         | File(s)                                 | Purpose                            |
| -------------- | --------------------------------------- | ---------------------------------- |
| Customers      | `olist_customers_dataset.csv`           | Buyer profiles & city/state        |
| Geolocation    | `olist_geolocation_dataset.csv`         | Lat/long → city/state mapping      |
| Orders         | `olist_orders_dataset.csv`              | Order headers & status/timestamps  |
| Order Items    | `olist_order_items_dataset.csv`         | Line items: product, seller, price |
| Payments       | `olist_order_payments_dataset.csv`      | Payment method & amounts           |
| Reviews        | `olist_order_reviews_dataset.csv`       | Ratings & review text              |
| Products       | `olist_products_dataset.csv`            | Product catalog & category         |
| Sellers        | `olist_sellers_dataset.csv`             | Seller profiles & location         |
| Category Names | `product_category_name_translation.csv` | PT→EN category name mapping        |


-----

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

------

## 📦Output Storage
- Curated datasets written to Delta/Parquet (optionally to HDFS) under paths like:
   - processed/monthly_sales/
   - processed/top_products/
   - processed/top_customers/.

------

## 🛠️Challenges
- Efficient processing of large datasets in Spark.
- Cleaning null, missing, or malformed data.
- Maintaining schema consistency during transformations.

-----

## 🎯Key Learning Outcomes
- Hands-on experience with **PySpark DataFrame API**.
- Implementing **end-to-end Spark ETL pipelines**.
- Managing **real-world eCommerce datasets**.
- Data transformation, aggregation, and scalable processing in Spark.
- Joining multi-table eCommerce data and producing analytics-ready marts.

------

## 🔭 Future Improvements
- Streaming ingestion (Kafka) for near real-time processing.
- Delta Lake for ACID + time travel; optimize with Z-Order.
- Validation with Great Expectations or Deequ.
- Orchestration via Airflow or Databricks Jobs.
- BI: Connect to Power BI/Tableau for dashboards.
- Tests: Add unit tests for transformations (e.g., pytest).

-----

 ## 📄 License
This project is licensed under the MIT License. See LICENSE for details.




