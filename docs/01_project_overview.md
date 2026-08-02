# Automated Retail Analytics ETL Pipeline

## Project Overview

This project is an end-to-end Retail Analytics Data Pipeline that automates the process of collecting, transforming, validating, storing, and visualizing retail data.

The pipeline extracts customer, product, and order data from the DummyJSON REST API, performs data validation and transformation using Python, stores raw data in PostgreSQL, builds analytics-ready models with dbt, orchestrates the workflow using Apache Airflow, and visualizes business insights in Power BI.

The entire application is containerized using Docker, allowing the complete environment to be deployed consistently on any machine.

---

# Business Objective

The objective of this project is to simulate a modern retail data platform that automates data ingestion and prepares reliable datasets for business reporting and analytics.

The pipeline demonstrates how raw operational data can be transformed into clean analytical models that support dashboard reporting and decision-making.

---

# Architecture

```
DummyJSON API
      │
      ▼
Python ETL
      │
      ▼
PostgreSQL (Raw Layer)
      │
      ▼
dbt Staging Models
      │
      ▼
dbt Mart Models
      │
      ▼
Power BI Dashboard
```

Apache Airflow orchestrates the complete workflow and Docker provides the execution environment.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | ETL development |
| PostgreSQL | Data warehouse |
| Apache Airflow | Workflow orchestration |
| dbt | Data transformation |
| Power BI | Dashboard and reporting |
| Docker | Containerization |
| REST API | Data source |

---

# Pipeline Features

- Automated API data extraction
- Data validation
- Data transformation
- Raw data storage
- dbt staging models
- dbt dimensional models
- Data quality tests
- Airflow scheduling
- Docker deployment
- Power BI dashboards

---

# Data Flow

1. Airflow triggers the ETL workflow.
2. Python extracts data from the DummyJSON API.
3. Data is validated and transformed.
4. Raw data is loaded into PostgreSQL.
5. dbt builds staging models.
6. dbt builds dimensional models.
7. dbt executes data quality tests.
8. Power BI connects to the analytics schema for reporting.

---

# Project Structure

```
Automated-ETL-Data-Pipeline/
│
├── airflow/
├── database/
├── docs/
├── powerbi/
├── python/
├── retail_dbt/
├── screenshots/
├── README.md
├── docker-compose.yml
└── requirements.txt
```

---

# Key Skills Demonstrated

- Python ETL Development
- REST API Integration
- PostgreSQL
- SQL
- Apache Airflow
- dbt Data Modeling
- Docker
- Power BI
- Data Validation
- Data Quality Testing
- Workflow Automation
- Data Warehousing

---

# Outcome

The project produces analytics-ready datasets and interactive Power BI dashboards through an automated and repeatable ETL pipeline.