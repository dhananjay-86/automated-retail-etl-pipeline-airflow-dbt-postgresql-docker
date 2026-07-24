import pandas as pd

from python.database.connection import get_connection


def load_customers():

    customers_df = pd.read_csv("data/raw/customers.csv")

    connection = get_connection()  #Connects Python to PostgreSQL.

    cursor = connection.cursor()  #The cursor sends SQL queries to the database.

    insert_query = """
        INSERT INTO raw.customers
        (customer_id, first_name, last_name, email, city)
        VALUES (%s, %s, %s, %s, %s)
    """

    for _, row in customers_df.iterrows():  #Reads one customer at a time from the DataFrame.

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

    connection.commit() #Saves all inserted records permanently.

    cursor.close()
    connection.close() #Always close database resources after you're done.

    print("✅ Customers loaded successfully!")


if __name__ == "__main__":
    load_customers()