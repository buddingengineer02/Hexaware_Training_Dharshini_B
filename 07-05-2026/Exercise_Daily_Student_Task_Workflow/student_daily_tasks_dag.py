from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def wake_up_function():
    print("Student woke up at 6 AM")


def attend_class_function():
    print("Student attended Python class")


def complete_assignment_function():
    print("Student completed Airflow assignment")


def sleep_function():
    print("Student went to sleep at 10 PM")


with DAG(
    dag_id="student_daily_tasks_dag",

    start_date=datetime(2025, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=["training"]

) as dag:


    wake_up_task = PythonOperator(
        task_id="wake_up_task",

        python_callable=wake_up_function
    )


    attend_class_task = PythonOperator(
        task_id="attend_class_task",

        python_callable=attend_class_function
    )


    complete_assignment_task = PythonOperator(
        task_id="complete_assignment_task",

        python_callable=complete_assignment_function
    )


    sleep_task = PythonOperator(
        task_id="sleep_task",

        python_callable=sleep_function
    )


    wake_up_task >> attend_class_task >> complete_assignment_task >> sleep_task