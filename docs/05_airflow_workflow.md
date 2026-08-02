# Airflow Workflow

## Overview

Apache Airflow orchestrates the complete ETL pipeline by executing each task in the correct order.

---

## DAG Workflow

```
Start
   │
   ▼
Initialize Database
   │
   ▼
Load Customers
   │
   ▼
Load Products
   │
   ▼
Load Orders
   │
   ▼
dbt Run
   │
   ▼
dbt Test
   │
   ▼
End
```

---

## Tasks

| Task | Description |
|------|-------------|
| Initialize Database | Creates schemas and tables if they do not exist |
| Load Customers | Loads customer data from the API |
| Load Products | Loads product data from the API |
| Load Orders | Loads order data from the API |
| dbt Run | Builds staging and mart models |
| dbt Test | Runs data quality tests |

---

## Features

- Daily scheduled execution
- Automatic retry on task failure
- Task-level logging
- Modular ETL workflow
- dbt integration