import pandas as pd
import random
import os
from faker import Faker

fake = Faker()


def generate_orders(num_orders=20000):

    orders = []

    for order_id in range(1, num_orders + 1):

        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1, 1000),
            "product_id": random.randint(1, 500),
            "quantity": random.randint(1, 5),
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        })

    orders_df = pd.DataFrame(orders)

    os.makedirs("data/raw", exist_ok=True)

    orders_df.to_csv(
        "data/raw/orders.csv",
        index=False
    )

    print("✅ orders.csv generated")