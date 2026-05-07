from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_marks_file_function():
    data = """Math,80
Science,75
English,90
Python,95"""

    with open("/tmp/student_marks.txt", "w") as file:
        file.write(data)

    print("student_marks.txt file created")


def read_marks_file_function():
    with open("/tmp/student_marks.txt", "r") as file:
        content = file.read()

    print(content)


def calculate_total_function():
    total = 80 + 75 + 90 + 95

    print(f"Total Marks = {total}")


def percentage_calculation_function():
    percentage = 340 / 4

    print(f"Percentage = {percentage}")


def generate_result_function():
    result_data = """Student Result Summary
Total Marks = 340
Result = PASS"""

    with open("/tmp/result.txt", "w") as file:
        file.write(result_data)

    print("result.txt file created")


with DAG(
    dag_id="student_marks_workflow_dag",

    start_date=datetime(2025, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=["training"]

) as dag:

    create_marks_file = PythonOperator(
        task_id="create_marks_file",

        python_callable=create_marks_file_function
    )

    read_marks_file = PythonOperator(
        task_id="read_marks_file",

        python_callable=read_marks_file_function
    )

    calculate_total = PythonOperator(
        task_id="calculate_total",

        python_callable=calculate_total_function
    )

    percentage_calculation = PythonOperator(
        task_id="percentage_calculation",

        python_callable=percentage_calculation_function
    )

    generate_result = PythonOperator(
        task_id="generate_result",

        python_callable=generate_result_function
    )

    create_marks_file >> read_marks_file >> calculate_total >> percentage_calculation >> generate_result