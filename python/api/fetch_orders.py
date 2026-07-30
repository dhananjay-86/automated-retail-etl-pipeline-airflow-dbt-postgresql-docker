import pandas as pd

from python.api.api_client import APIClient


def fetch_orders():

    client = APIClient()

    response = client.get_data("/carts")

    carts = response["carts"]

    return pd.DataFrame(carts)


if __name__ == "__main__":

    df = fetch_orders()

    print(df.head())

    print(df.columns)

    print(f"\nTotal Orders: {len(df)}")