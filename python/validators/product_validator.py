def validate_products(products_df):

    products_df = products_df.drop_duplicates(subset=["product_id"])

    products_df = products_df.dropna(
        subset=[
            "product_id",
            "product_name",
            "category",
            "price",
            "stock_quantity",
        ]
    )

    products_df = products_df[products_df["price"] > 0]

    products_df = products_df[products_df["stock_quantity"] >= 0]

    return products_df

