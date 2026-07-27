from datetime import datetime
import sys

sys.path.append("/opt/project")

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from python.database.init_database import initialize_database
from python.etl.load_customers import load_customers
from python.etl.load_products import load_products
from python.etl.load_orders import load_orders


with DAG(
    dag_id="retail_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["Retail", "ETL"],
) as dag:

    start = EmptyOperator(task_id="start")

    initialize_db = PythonOperator(
        task_id="initialize_database",
        python_callable=initialize_database,
    )

    customers = PythonOperator(
        task_id="load_customers",
        python_callable=load_customers,
    )

    products = PythonOperator(
        task_id="load_products",
        python_callable=load_products,
    )

    orders = PythonOperator(
        task_id="load_orders",
        python_callable=load_orders,
    )

    end = EmptyOperator(task_id="end")

    start >> initialize_db >> customers >> products >> orders >> end
    