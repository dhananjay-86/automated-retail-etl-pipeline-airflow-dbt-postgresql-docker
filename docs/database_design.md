# Database Design

## Tables

### Customers
- customer_id (PK)
- first_name
- last_name
- email
- city
- created_at

### Products
- product_id (PK)
- product_name
- category
- price
- stock_quantity

### Orders
- order_id (PK)
- customer_id (FK)
- product_id (FK)
- quantity
- order_date

## Relationships

Customers (1) ----< Orders >---- (1) Products