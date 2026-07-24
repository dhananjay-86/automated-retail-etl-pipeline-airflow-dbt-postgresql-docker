import pandas as pd
import random
import os

categories = [
    "Electronics",
    "Accessories",
    "Office",
    "Furniture"
]


def generate_products(num_products=500):

    products = []

    for product_id in range(1, num_products + 1):

        products.append({
            "product_id": product_id,
            "product_name": f"Product {product_id}",
            "category": random.choice(categories),
            "price": round(random.uniform(100, 5000), 2),
            "stock": random.randint(10, 500)
        })

    products_df = pd.DataFrame(products)

    os.makedirs("data/raw", exist_ok=True)

    products_df.to_csv(
        "data/raw/products.csv",
        index=False
    )

    print("✅ products.csv generated")