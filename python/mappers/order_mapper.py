import pandas as pd


def map_orders(orders_df):

    rows = []

    for _, order in orders_df.iterrows():

        order_id = order["id"]
        customer_id = order["userId"]

        for product in order["products"]:

            rows.append(
                {
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "product_id": product["id"],
                    "quantity": product["quantity"],
                    "order_date": None
                }
            )

    return pd.DataFrame(rows)




