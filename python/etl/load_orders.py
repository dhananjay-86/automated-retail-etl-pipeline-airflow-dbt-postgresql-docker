import pandas as pd
from pathlib import Path

from python.etl.base_loader import load_data

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ORDERS_FILE = PROJECT_ROOT / "data" / "raw" / "orders.csv"


def load_orders(orders_df):

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

    ON CONFLICT (order_id, product_id)

    DO UPDATE SET
        customer_id = EXCLUDED.customer_id,
        quantity = EXCLUDED.quantity,
        order_date = EXCLUDED.order_date;
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

    orders_df = pd.read_csv(ORDERS_FILE)

    load_orders(orders_df)