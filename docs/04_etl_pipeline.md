# ETL Pipeline

## Overview

The ETL pipeline extracts data from the DummyJSON API, validates and transforms it using Python, and loads it into PostgreSQL.

Apache Airflow orchestrates the entire workflow.

---

## Customer Pipeline

1. Extract customer data from the DummyJSON API.
2. Validate and clean customer records.
3. Load data into `raw.customers`.

---

## Product Pipeline

1. Extract product data from the DummyJSON API.
2. Validate and clean product records.
3. Load data into `raw.products`.

---

## Order Pipeline

1. Extract cart data from the DummyJSON API.
2. Transform nested cart data into order records.
3. Validate and clean order records.
4. Load data into `raw.orders`.

---

## Data Validation

Python validation includes:

- Removing duplicate records
- Removing null values
- Validating required columns
- Ensuring valid quantities

---

## Data Transformation

After loading raw data, dbt:

- Builds staging models
- Creates dimensional and fact tables
- Runs data quality tests