from datetime import datetime, timedelta
import sys

sys.path.append("/opt/project")

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from python.database.init_database import initialize_database
from python.etl.load_customers import load_customers
from python.etl.load_products import load_products
from python.etl.load_orders import load_orders


# Default settings applied to all tasks
default_args = {
    "owner": "Dhananjay",
    "retries": 3,
    "retry_delay": timedelta(seconds=30),
}


with DAG(
    dag_id="retail_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["Retail", "ETL"],
) as dag:

    # Start Task
    start = EmptyOperator(
        task_id="start"
    )

    # Initialize Database
    initialize_db = PythonOperator(
        task_id="initialize_database",
        python_callable=initialize_database,
        execution_timeout=timedelta(minutes=5),
    )

    # Load Customers
    customers = PythonOperator(
        task_id="load_customers",
        python_callable=load_customers,
        execution_timeout=timedelta(minutes=5),
    )

    # Load Products
    products = PythonOperator(
        task_id="load_products",
        python_callable=load_products,
        execution_timeout=timedelta(minutes=5),
    )

    # Load Orders
    orders = PythonOperator(
        task_id="load_orders",
        python_callable=load_orders,
        execution_timeout=timedelta(minutes=5),
    )

    # End Task
    end = EmptyOperator(
        task_id="end"
    )

    # Task Dependencies
    start >> initialize_db >> customers >> products >> orders >> end