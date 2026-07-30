from python.utils.logger import get_logger

logger = get_logger(__name__)
from python.api.fetch_products import fetch_products

from python.mappers.product_mapper import map_products

from python.validators.product_validator import validate_products

from python.etl.load_products import load_products


def run_product_api_pipeline():

    logger.info("Fetching products from API...")

    products_df = fetch_products()

    logger.info(f"Fetched {len(products_df)} products")

    products_df = map_products(products_df)

    logger.info("Product mapping completed")

    products_df = validate_products(products_df)

    logger.info("Product validation completed")

    load_products(products_df)

    logger.info("Product API pipeline completed successfully.")


if __name__ == "__main__":

    run_product_api_pipeline()
    