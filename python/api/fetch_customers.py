import pandas as pd

from python.api.api_client import APIClient


def fetch_customers():
    """
    Fetch customer data from DummyJSON API
    and return it as a Pandas DataFrame.
    """

    client = APIClient()

    data = client.get_data("/users")

    customers = data["users"]

    df = pd.DataFrame(customers)

    return df


if __name__ == "__main__":

    df = fetch_customers()

    print(df.head())