import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

NUM_CUSTOMERS = 1000

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "city": fake.city(),
    })

customers_df = pd.DataFrame(customers)

os.makedirs("data/raw", exist_ok=True)

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("✅ customers.csv created successfully!")