import pandas as pd


def map_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert DummyJSON customer data
    into our database schema.
    """

    mapped_df = pd.DataFrame()

    mapped_df["customer_id"] = df["id"]

    mapped_df["first_name"] = df["firstName"]

    mapped_df["last_name"] = df["lastName"]

    mapped_df["email"] = df["email"]

    mapped_df["city"] = df["address"].apply(
        lambda address: address.get("city")
    )

    return mapped_df

