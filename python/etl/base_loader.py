from psycopg2.extras import execute_values

from python.database.connection import get_connection
from python.utils.logger import logger


def load_data(data, insert_query, entity_name):

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        execute_values(
            cursor,
            insert_query,
            data
        )

        connection.commit()

        logger.info(
            f"{entity_name} loaded successfully. Rows inserted: {len(data)}"
        )

    except Exception as e:

        if connection:
            connection.rollback()

        logger.error(
            f"{entity_name} loading failed: {e}"
        )

        raise

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

        logger.info("Database connection closed.")