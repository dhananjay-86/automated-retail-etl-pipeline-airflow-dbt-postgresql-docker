from python.etl.load_customers import load_customers
from python.etl.load_products import load_products
from python.etl.load_orders import load_orders
from python.utils.logger import logger


def run_pipeline():

    logger.info("========== ETL Pipeline Started ==========")

    print("\nStarting ETL Pipeline...\n")

    load_customers()
    load_products()
    load_orders()

    logger.info("========== ETL Pipeline Completed ==========")

    print("\nETL Pipeline Completed Successfully!\n")


if __name__ == "__main__":
    run_pipeline()