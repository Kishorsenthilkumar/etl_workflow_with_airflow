from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id='docker_image',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    

    task=DockerOperator(
        task_id='docker_container',
        image="python:3.8",
        api_version="auto",
        auto_remove=True,
        command='echo "docker image is created successfully"',
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )