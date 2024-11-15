from datetime import datetime
from airflow import DAG
from airflow import sql as aql

with DAG(
    dag_id='etl_snowflake',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    

