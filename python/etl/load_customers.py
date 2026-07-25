import pandas as pd

from python.etl.base_loader import load_data


def load_customers():

    customers_df = pd.read_csv("data/raw/customers.csv")

    insert_query = """
    INSERT INTO raw.customers
    (customer_id, first_name, last_name, email, city)
    VALUES %s
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
    load_customers()