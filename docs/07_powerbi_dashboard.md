# Power BI Dashboard

## Overview

The Power BI dashboard provides interactive visualizations built on the analytics tables created by dbt.

---

## Dashboard Pages

### Executive Dashboard

Displays key business KPIs and overall sales performance.

**KPIs**

- Total Revenue
- Total Orders
- Total Customers
- Total Products

---

### Customer Analysis

Provides customer-level insights including:

- Top Customers
- Orders by City
- Customer Distribution

---

### Product Analysis

Provides product performance insights including:

- Top Selling Products
- Revenue by Category
- Quantity Sold by Product

---

## Data Source

Power BI connects directly to the PostgreSQL **analytics** schema.

---

## Dashboard Refresh

After the ETL pipeline completes successfully:

1. Trigger the Airflow DAG.
2. dbt updates the analytics tables.
3. Refresh the Power BI dataset to display the latest data.