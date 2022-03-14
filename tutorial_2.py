import pendulum
from airflow.operators.python import PythonOperator
from airflow import DAG

with DAG(
    dag_id = 'eth_etl',
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    schedule_interval="@daily",
    catchup=False
) as dag:

    @task(task_id="testing_python_operator")
    def test_function(**kwargs):
        print(kwargs)

        return 'Return test function to logs'

    run_this = test_function()