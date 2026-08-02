from datetime import date, timedelta
import random
import pandas as pd


def map_orders(orders_df):

    rows = []

    for _, order in orders_df.iterrows():

        order_id = order["id"]
        customer_id = order["userId"]

        # One date per order
        order_date = date.today() - timedelta(
            days=random.randint(0, 90)
        )

        for product in order["products"]:

            rows.append(
                {
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "product_id": product["id"],
                    "quantity": product["quantity"],
                    "order_date": order_date
                }
            )

    return pd.DataFrame(rows)




