import pandas as pd
from pathlib import Path

from python.etl.base_loader import load_data

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = PROJECT_ROOT / "data" / "raw" / "customers.csv"


def load_customers(customers_df):

    insert_query = """
    INSERT INTO raw.customers
    (
        customer_id,
        first_name,
        last_name,
        email,
        city
    )

    VALUES %s

    ON CONFLICT (customer_id)

    DO UPDATE SET
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        email = EXCLUDED.email,
        city = EXCLUDED.city;
    """

    data = [
        (
            int(row["customer_id"]),
            row["first_name"],
            row["last_name"],
            row["email"],
            row["city"]
        )
        for _, row in customers_df.iterrows()
    ]

    load_data(
        data=data,
        insert_query=insert_query,
        entity_name="Customers"
    )

    print("Customers loaded successfully.")


if __name__ == "__main__":

    customers_df = pd.read_csv(CUSTOMERS_FILE)

    load_customers(customers_df)