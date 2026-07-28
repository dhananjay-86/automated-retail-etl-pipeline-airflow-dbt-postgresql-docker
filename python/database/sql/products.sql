CREATE TABLE IF NOT EXISTS raw.products (

    product_id INT PRIMARY KEY,

    product_name VARCHAR(255),

    category VARCHAR(100),

    price NUMERIC(10,2),

    stock_quantity INT

);