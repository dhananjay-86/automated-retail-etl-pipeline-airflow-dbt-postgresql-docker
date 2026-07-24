import pandas as pd

from python.database.connection import get_connection
from python.utils.logger import logger


def load_customers():

    connection = None
    cursor = None

    try:

        customers_df = pd.read_csv("data/raw/customers.csv")

        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO raw.customers
        (customer_id, first_name, last_name, email, city)
        VALUES (%s, %s, %s, %s, %s)
        """

        for _, row in customers_df.iterrows():

            cursor.execute(
                insert_query,
                (
                    int(row["customer_id"]),
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["city"]
                )
            )

        connection.commit()

        logger.info("Customers loaded successfully.")

        print("Customers loaded successfully.")

    except Exception as e:

        if connection:
            connection.rollback()

        logger.error(f"Customer loading failed: {e}")

        print(f"Error: {e}")

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

        logger.info("Database connection closed.")


if __name__ == "__main__":
    load_customers()