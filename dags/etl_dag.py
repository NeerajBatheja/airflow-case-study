from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

def transform_data():
    commission_df = pd.read_csv('/opt/airflow/helper/commission.csv')
    orders_df = pd.read_csv('/opt/airflow/helper/orders.csv')

    merged_df = pd.merge(orders_df, commission_df, left_on='airline_id', right_on='operating_airline', how='left')

    merged_df['gross_commission'] = merged_df['base_fare'] * merged_df['commission_percentage']
    merged_df['bf_net_commission'] = merged_df['base_fare'] - merged_df['gross_commission']
    merged_df['gross_income'] = merged_df['bf_net_commission'] * merged_df['incentive_percentage']
    merged_df['wht_commission'] = merged_df['gross_commission'] * merged_df['tax_percentage']
    merged_df['wht_income'] = merged_df['gross_income'] * merged_df['tax_percentage']
    merged_df['net_commission'] = merged_df['gross_commission'] - merged_df['wht_commission']
    merged_df['net_income'] = merged_df['gross_income'] - merged_df['wht_income']


    merged_df['revenue'] = merged_df['net_commission'] + merged_df['net_income']
    merged_df.to_csv('/opt/airflow/dags/transformed_data.csv', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 16),
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('etl_dag', default_args=default_args, schedule_interval=None) as dag:
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

transform_task
