import pandas as pd

from python.api.api_client import APIClient


def fetch_products():

    client = APIClient()

    response = client.get_data("/products")

    products = response["products"]

    return pd.DataFrame(products)




