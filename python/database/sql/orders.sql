CREATE TABLE IF NOT EXISTS raw.orders (

    order_id INT PRIMARY KEY,

    customer_id INT,

    product_id INT,

    quantity INT,

    order_date DATE

);