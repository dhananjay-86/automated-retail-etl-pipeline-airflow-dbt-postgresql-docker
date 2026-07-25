import pandas as pd

from python.etl.base_loader import load_data


def load_products():

    products_df = pd.read_csv("data/raw/products.csv")

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
    """

    data = [
        (
            int(row["product_id"]),
            row["product_name"],
            row["category"],
            float(row["price"]),
            int(row["stock"])
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
    load_products()