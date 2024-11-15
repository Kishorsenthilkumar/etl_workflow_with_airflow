from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset("C:/Users/Kisho/Downloads")


with DAG(
    dag_id="consumer",
    schedule=[my_file],
    start_date=datetime(2024, 1, 1),
    catchup=False
):
    @task

    def update_consumer():
        with open(my_file.uri,"r") as f:
            print(f.write())
    
    update_consumer()