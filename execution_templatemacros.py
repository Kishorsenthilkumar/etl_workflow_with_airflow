from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    dag_id="template_macros",
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily'
) as dag:
    

    task=BashOperator(
        task_id="execution_datetime",
        bash_command='echo "The execution datetime is {{ds}}"',
    )