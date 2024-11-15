from airflow import Dataset,DAG
from airflow.decorators import task
from datetime import datetime


my_file = Dataset("C:/Users/Kisho/Downloads")


with DAG (
    dag_id="producer",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
):

   @task(outlets=[my_file])
   def producer_task():  
      with open(my_file.uri,"a+") as f:
          f.write("producer update")
   producer_task()

