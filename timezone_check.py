from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
import pendulum

local_tz=pendulum.timezone("America/New_York")

with DAG(
    dag_id="timezone_check",
    start_date=datetime(2023, 1, 1, tzinfo=local_tz),
    schedule_interval='@daily'
    
) as dag:
    
    task=BashOperator(
        task_id="local_timezone",
        bash_command='echo "the execution of datetime according to localtime{{ds}}"'
    )