from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'snowflake_dbt_pipeline',
    default_args=default_args,
    description='A DAG to run dbt models and tests for Snowflake pipeline',
    schedule_interval='@daily',
    catchup=False,
)

# 1. تشغيل dbt run للمراحل (Staging, Intermediate, Marts)
dbt_run_task = BashOperator(
    task_id='dbt_run',
    bash_command='cd /opt/airflow/dbt_project && dbt run --profiles-dir .',
    dag=dag,
)

# 2. تشغيل dbt test لتأكيد صحة البيانات
dbt_test_task = BashOperator(
    task_id='dbt_test',
    bash_command='cd /opt/airflow/dbt_project && dbt test --profiles-dir .',
    dag=dag,
)

# تحديد الترتيب: Run الأول وبعده Test
dbt_run_task >> dbt_test_task
