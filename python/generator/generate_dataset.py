from python.generator.customer_generator import generate_customers
from python.generator.product_generator import generate_products
from python.generator.order_generator import generate_orders


def main():

    print("Generating Customers...")
    generate_customers()

    print("Generating Products...")
    generate_products()

    print("Generating Orders...")
    generate_orders()

    print("\n✅ Dataset generation completed successfully!")


if __name__ == "__main__":
    main()