import pandas as pd

from python.etl.base_loader import load_data


def load_orders():

    orders_df = pd.read_csv("data/raw/orders.csv")

    insert_query = """
    INSERT INTO raw.orders
    (
        order_id,
        customer_id,
        product_id,
        quantity,
        order_date
    )
    VALUES %s
    """

    data = [
        (
            int(row["order_id"]),
            int(row["customer_id"]),
            int(row["product_id"]),
            int(row["quantity"]),
            row["order_date"]
        )
        for _, row in orders_df.iterrows()
    ]

    load_data(
        data=data,
        insert_query=insert_query,
        entity_name="Orders"
    )

    print("Orders loaded successfully.")


if __name__ == "__main__":
    load_orders()