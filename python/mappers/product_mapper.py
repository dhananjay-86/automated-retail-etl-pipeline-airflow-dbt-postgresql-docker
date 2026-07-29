def map_products(products_df):

    mapped_df = products_df.rename(
        columns={
            "id": "product_id",
            "title": "product_name",
            "stock": "stock_quantity",
        }
    )

    mapped_df = mapped_df[
        [
            "product_id",
            "product_name",
            "category",
            "price",
            "stock_quantity",
        ]
    ]

    return mapped_df

