from datetime import datetime, timedelta
from textwrap import dedent
import datetime as dt
from airflow.operators.python_operator import PythonOperator
from airflow import DAG


default_args = {
    'retries' : 2,
    'retry_delay' : dt.timedelta(minutes=1),
    'email_on_retry' : False,
    'email_on_failure' : False,
}

dag = DAG(
    'eth_etl',
    default_args=default_args,
    start_date=dt.datetime(2022,3,1),
    schedule_interval=dt.timedelta(days=1),
    catchup=True
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
)
t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
)

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
)

t1 >> [t2, t3]