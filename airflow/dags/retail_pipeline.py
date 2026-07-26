from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="retail_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["retail", "etl"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    python_etl = BashOperator(
        task_id="python_etl",
        bash_command="echo 'Running Python ETL...'"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="echo 'Running dbt run...'"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="echo 'Running dbt test...'"
    )

    end = EmptyOperator(
        task_id="end"
    )

    start >> python_etl >> dbt_run >> dbt_test >> end