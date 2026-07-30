def validate_orders(orders_df):

    orders_df = orders_df.drop_duplicates(
        subset=["order_id", "product_id"]
    )

    orders_df = orders_df.dropna(
        subset=[
            "order_id",
            "customer_id",
            "product_id",
            "quantity"
        ]
    )

    orders_df = orders_df[
        orders_df["quantity"] > 0
    ]

    return orders_df

