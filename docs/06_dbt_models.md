# dbt Models

## Overview

dbt transforms raw PostgreSQL data into analytics-ready tables for reporting and Power BI.

---

## Sources

The project uses the following raw tables as dbt sources:

- raw.customers
- raw.products
- raw.orders

---

## Staging Models

| Model | Description |
|--------|-------------|
| stg_customers | Cleans and standardizes customer data |
| stg_products | Cleans and standardizes product data |
| stg_orders | Cleans and standardizes order data |

---

## Mart Models

| Model | Description |
|--------|-------------|
| dim_customers | Customer dimension table |
| dim_products | Product dimension table |
| fact_orders | Order fact table for analytics |

---

## Data Quality Tests

The following dbt tests are implemented:

- Not Null
- Unique
- Relationships

---

## Materialization

| Model Layer | Materialization |
|--------------|----------------|
| Staging | View |
| Marts | Table / Incremental |