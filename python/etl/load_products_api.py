from python.api.fetch_products import fetch_products

from python.mappers.product_mapper import map_products

from python.validators.product_validator import validate_products

from python.etl.load_products import load_products


def run_product_api_pipeline():

    print("Fetching products from API...")

    products_df = fetch_products()

    print(f"Fetched {len(products_df)} products")

    products_df = map_products(products_df)

    print("Product mapping completed")

    products_df = validate_products(products_df)

    print("Product validation completed")

    load_products(products_df)

    print("Product API pipeline completed successfully.")


if __name__ == "__main__":

    run_product_api_pipeline()
    