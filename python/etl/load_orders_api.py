from python.api.fetch_orders import fetch_orders
from python.mappers.order_mapper import map_orders
from python.validators.order_validator import validate_orders

from python.etl.load_orders import load_orders


def run_order_api_pipeline():

    print("Fetching orders from API...")

    orders_df = fetch_orders()

    print(f"Fetched {len(orders_df)} carts")

    orders_df = map_orders(orders_df)

    print(f"Flattened into {len(orders_df)} order rows")

    orders_df = validate_orders(orders_df)

    print("Order validation completed")

    load_orders(orders_df)

    print("Order API pipeline completed successfully.")


if __name__ == "__main__":
    run_order_api_pipeline()