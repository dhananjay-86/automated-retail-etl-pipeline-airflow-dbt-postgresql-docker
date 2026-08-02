import pandas as pd

from python.api.api_client import APIClient


def fetch_customers():
    """
    Fetch customer data from DummyJSON API
    and return it as a Pandas DataFrame.
    """

    client = APIClient()

    data = client.get_data("/users?limit=208&skip=0")

    customers = data["users"]

    df = pd.DataFrame(customers)

    return df





