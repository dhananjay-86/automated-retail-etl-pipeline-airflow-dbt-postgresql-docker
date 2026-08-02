# Database Design

## Schemas

The project uses two PostgreSQL schemas:

| Schema | Purpose |
|--------|---------|
| raw | Stores data loaded directly from the API |
| analytics | Stores transformed tables created by dbt |

---

## Raw Tables

### customers

Stores customer information.

Primary Key:

- customer_id

---

### products

Stores product details.

Primary Key:

- product_id

---

### orders

Stores order transactions.

Primary Key:

- order_id + product_id

Foreign Keys:

- customer_id → customers.customer_id
- product_id → products.product_id

---

## Analytics Tables

### Staging Models

- stg_customers
- stg_products
- stg_orders

These models clean and standardize the raw data.

---

### Mart Models

- dim_customers
- dim_products
- fact_orders

These tables are optimized for reporting and Power BI dashboards.