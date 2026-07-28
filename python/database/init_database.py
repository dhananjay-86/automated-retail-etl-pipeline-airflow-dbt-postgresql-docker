from pathlib import Path

from python.database.connection import get_connection


SQL_DIR = Path(__file__).parent / "sql"


def execute_sql_file(cursor, filename):
    with open(SQL_DIR / filename, "r", encoding="utf-8") as file:
        cursor.execute(file.read())


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    execute_sql_file(cursor, "schemas.sql")
    execute_sql_file(cursor, "customers.sql")
    execute_sql_file(cursor, "products.sql")
    execute_sql_file(cursor, "orders.sql")

    connection.commit()

    cursor.close()
    connection.close()

    print("✅ Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()