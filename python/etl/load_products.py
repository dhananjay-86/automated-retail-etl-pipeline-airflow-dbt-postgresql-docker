import pandas as pd
from pathlib import Path

from python.etl.base_loader import load_data

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PRODUCTS_FILE = PROJECT_ROOT / "data" / "raw" / "products.csv"


def load_products(products_df):

    insert_query = """
    INSERT INTO raw.products
    (
        product_id,
        product_name,
        category,
        price,
        stock_quantity
    )

    VALUES %s

    ON CONFLICT (product_id)

    DO UPDATE SET
        product_name = EXCLUDED.product_name,
        category = EXCLUDED.category,
        price = EXCLUDED.price,
        stock_quantity = EXCLUDED.stock_quantity;
    """

    data = [

        (

            int(row["product_id"]),

            row["product_name"],

            row["category"],

            float(row["price"]),

            int(row["stock_quantity"])

        )

        for _, row in products_df.iterrows()

    ]

    load_data(

        data=data,

        insert_query=insert_query,

        entity_name="Products"

    )

    print("Products loaded successfully.")


if __name__ == "__main__":

    products_df = pd.read_csv(PRODUCTS_FILE)

    load_products(products_df)