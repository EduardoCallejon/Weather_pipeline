from datetime import datetime,timedelta 
from airflow.decorators import dag,task
from pathlib import Path
import sys,os
from dotenv import load_dotenv

sys.path.insert(0,'/opt/airflow/src')

from extract import extract_data
from transform import transformations
from load import load_data

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('API_KEY')

url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo, BR&units=metric&appid={API_KEY}'

@dag(
    dag_id='weather_dag',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    description='Weather_pratice - CLima SP',
    schedule='0 */1 * * * ',
    start_date=datetime(2026, 2, 7),
    catchup=False,
    tags=['weather', 'etl',]
)

def weather_pipeline():

    @task
    def extract():
        extract_data(url)

    @task
    def transform():
       df = transformations()
       df.to_parquet('/opt/airflow/data/weather_data.parquet',index=False)

    @task
    def load():
        import pandas as pd

        df = pd.read_parquet('/opt/airflow/data/weather_data.parquet')
        load_data('sp_weather',df)

    extract() >> transform() >> load()

weather_pipeline()