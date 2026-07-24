import psycopg2    #This is the library that allows Python to communicate with PostgreSQL.
from python.config.database_config import DB_CONFIG


def get_connection():  #Creates a reusable function.Later every ETL script will simply call  get_connection() instead of rewriting the connection code.
    """
    Creates and returns a PostgreSQL database connection.
    """

    try:
        connection = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )

        print("✅ Connected to PostgreSQL successfully!")

        return connection

    except Exception as error:
        print(f"❌ Connection failed: {error}")
        return None


if __name__ == "__main__":  #Only run this test when this file is executed directly.Later other Python files can import get_connection() without automatically connecting to the database.
    connection = get_connection()

    if connection:
        connection.close()
        print("✅ Connection closed.")