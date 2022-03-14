import pendulum
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow import DAG


def test_function(**kwargs):
    print(kwargs)

    return 'Return test function to logs'

with DAG(
    dag_id = 'eth_etl',
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    schedule_interval="@daily",
    catchup=False
) as dag:
    dummy_task = DummyOperator(task_id='dummy_task', retries=3)
    extract_task = PythonOperator(task_id="extract_task",python_callable=test_function("testing python task"))

    dummy_task >> extract_task