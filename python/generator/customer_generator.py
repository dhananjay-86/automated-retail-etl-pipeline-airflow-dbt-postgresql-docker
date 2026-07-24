import pandas as pd
from faker import Faker
import os

fake = Faker()


def generate_customers(num_customers=1000):
    customers = []

    for customer_id in range(1, num_customers + 1):
        customers.append({
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "city": fake.city()
        })

    customers_df = pd.DataFrame(customers)

    os.makedirs("data/raw", exist_ok=True)

    customers_df.to_csv(
        "data/raw/customers.csv",
        index=False
    )

    print("✅ customers.csv generated")