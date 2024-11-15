from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG(
    dag_id='Task_group',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    

    start=DummyOperator(
        task_id='start'
    )

    with TaskGroup("extract_task") as extract_task:
        task1=DummyOperator(
            task_id='extract_task1'
        )

        task2=DummyOperator(
            task_id='extract_task2'
        )
        task3=DummyOperator(
            task_id='extrac_task3'
        )

    with TaskGroup("transform_task") as transform_task:
        task4=DummyOperator(
            task_id='transform_task4'
        )

        task5=DummyOperator(
            task_id='transform_task5'
        )
        task6=DummyOperator(
            task_id='transform_task6'
        )

    end=DummyOperator(
        task_id='end'
    )



    start>>extract_task>>transform_task>>end