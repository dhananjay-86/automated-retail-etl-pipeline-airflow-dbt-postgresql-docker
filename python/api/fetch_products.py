import pandas as pd

from python.api.api_client import APIClient


def fetch_products():

    client = APIClient()

    initial_response = client.get_data("/products")

    total_products = initial_response["total"]

    response = client.get_data(f"/products?limit={total_products}")

    return pd.DataFrame(response["products"])




