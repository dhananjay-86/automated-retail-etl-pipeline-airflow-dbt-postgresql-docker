from python.utils.logger import get_logger
logger = get_logger(__name__)
from python.api.fetch_customers import fetch_customers
from python.mappers.customer_mapper import map_customers
from python.validators.customer_validator import validate_customers

from python.etl.load_customers import load_customers


def run_customer_api_pipeline():

    logger.info("Fetching customers from API...")

    customers_df = fetch_customers()

    logger.info(f"Fetched {len(customers_df)} customers")

    customers_df = map_customers(customers_df)

    logger.info("Customer mapping completed")

    customers_df = validate_customers(customers_df)

    logger.info("Customer validation completed")

    load_customers(customers_df)

    logger.info("Customer API pipeline completed successfully.")


if __name__ == "__main__":
    run_customer_api_pipeline()
