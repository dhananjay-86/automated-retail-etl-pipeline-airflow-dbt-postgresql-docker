from python.utils.logger import get_logger

logger = get_logger(__name__)
from python.api.fetch_orders import fetch_orders
from python.mappers.order_mapper import map_orders
from python.validators.order_validator import validate_orders

from python.etl.load_orders import load_orders


def run_order_api_pipeline():

    logger.info("Fetching orders from API...")

    orders_df = fetch_orders()

    logger.info(f"Fetched {len(orders_df)} carts")

    orders_df = map_orders(orders_df)

    logger.info(f"Flattened into {len(orders_df)} order rows")

    orders_df = validate_orders(orders_df)

    logger.info("Order validation completed")

    load_orders(orders_df)

    logger.info("Order API pipeline completed successfully.")


if __name__ == "__main__":
    run_order_api_pipeline()