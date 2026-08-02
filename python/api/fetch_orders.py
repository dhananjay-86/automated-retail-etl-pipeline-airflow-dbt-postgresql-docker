import pandas as pd

from python.api.api_client import APIClient


def fetch_orders():

    client = APIClient()

    response = client.get_data("/carts?limit=100&skip=0")

    carts = response["carts"]

    return pd.DataFrame(carts)


