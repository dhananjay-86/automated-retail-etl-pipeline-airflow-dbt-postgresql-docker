import pandas as pd


def validate_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate customer data before loading
    into PostgreSQL.
    """

    validated_df = df.copy()

    # Remove duplicate customer IDs
    validated_df = validated_df.drop_duplicates(subset=["customer_id"])

    # Remove rows with missing first name
    validated_df = validated_df.dropna(subset=["first_name"])

    # Remove rows with missing last name
    validated_df = validated_df.dropna(subset=["last_name"])

    # Remove rows with missing email
    validated_df = validated_df.dropna(subset=["email"])

    # Remove rows with missing city
    validated_df = validated_df.dropna(subset=["city"])

    return validated_df