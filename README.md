# oracle-to-snowflake-data-platform
Enterprise-grade Oracle to Snowflake data migration platform using Python, Airflow, AWS S3, Snowpipe, dbt, and Great Expectations.
# Oracle to Snowflake Data Platform

## Overview

This project demonstrates an enterprise-grade data platform designed to migrate data from an on-premises Oracle warehouse to Snowflake on AWS.

The platform supports:

- Incremental ingestion
- Automated orchestration
- Data quality validations
- Reconciliation checks
- Audit framework
- Curated business marts

This project simulates a real-world consulting engagement where an organization modernizes its legacy analytics infrastructure.

---

## Business Problem

A retail organization currently stores analytical data in an on-prem Oracle data warehouse.

The legacy platform faces several challenges:

- Limited scalability
- High maintenance cost
- Long ETL execution times
- Complex operational support

The organization decided to migrate its analytics workloads to Snowflake on AWS.

---

## Solution Architecture

```text
                    +------------------+
                    | Oracle Database  |
                    +------------------+
                              |
                     Python Extraction
                              |
                              v
                    +------------------+
                    | AWS S3 Raw Zone  |
                    +------------------+
                              |
                         Snowpipe
                              |
                              v
                    +------------------+
                    | Snowflake RAW    |
                    +------------------+
                              |
                         dbt Models
                              |
                              v
                    +------------------+
                    | Curated Layer    |
                    +------------------+
                              |
                        Power BI
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Source | Oracle |
| Language | Python |
| Orchestration | Apache Airflow |
| Cloud Storage | AWS S3 |
| Warehouse | Snowflake |
| Transformation | dbt |
| Data Quality | Great Expectations |
| Visualization | Power BI |
| Version Control | Git |
| Containerization | Docker |

---

## Features

### Incremental Data Ingestion

Uses watermark-based loading strategy.

### Automated Orchestration

Apache Airflow orchestrates end-to-end workflows.

### Metadata-Driven Framework

Table configurations are maintained externally.

### Data Quality Checks

Validates:

- Null records
- Duplicate records
- Invalid values
- Referential integrity

### Audit Framework

Captures:

- Start time
- End time
- Source count
- Target count
- Status
- Error messages

### Reconciliation Framework

Validates source and target consistency.

---

## Folder Structure

```text
oracle-to-snowflake-data-platform/
│
├── airflow/
│   └── dags/
│
├── extraction/
│
├── ingestion/
│
├── quality/
│
├── reconciliation/
│
├── dbt_project/
│   ├── models/
│
├── config/
│
├── sql/
│
├── docs/
│
├── sample_data/
│
├── screenshots/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

## Workflow

1. Extract data from Oracle.
2. Upload raw files to AWS S3.
3. Trigger Snowpipe ingestion.
4. Load RAW tables.
5. Execute data quality checks.
6. Transform using dbt.
7. Run reconciliation checks.
8. Publish business marts.

---

## Sample Source Tables

### CUSTOMER

| Column |
|--------|
| customer_id |
| first_name |
| last_name |
| email |
| city |
| created_date |

### PRODUCT

| Column |
|--------|
| product_id |
| product_name |
| category |
| price |

### ORDERS

| Column |
|--------|
| order_id |
| customer_id |
| product_id |
| quantity |
| amount |
| order_date |
| last_updated_timestamp |

---

## Incremental Load Strategy

```sql
SELECT *
FROM ORDERS
WHERE LAST_UPDATED_TIMESTAMP >
(
SELECT MAX(last_loaded_timestamp)
FROM ETL_CONTROL_TABLE
WHERE table_name='ORDERS'
);
```

---

## Data Quality Rules

- Customer ID cannot be null
- Order ID must be unique
- Order amount must be positive
- Product price cannot be negative
- Order date cannot be in the future

---

## Future Enhancements

- CDC using Kafka and Debezium
- Slack alert integration
- Infrastructure as Code using Terraform
- CI/CD using GitHub Actions
- Data observability dashboard

---

## Author

Sumanth Katari
