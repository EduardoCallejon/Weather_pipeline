
from sqlalchemy import create_engine, text 
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

def create_connection(USER:str,PASSWORD:str,HOST:str,PORT:str,DBNAME:str):
    #Criação da Engine
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    # Test the connection
    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
        print(f"Failed to connect: {e}")
    return engine

conn = create_connection(USER,PASSWORD,HOST,PORT,DBNAME)

def load_data(table_name:str, df):
    try:
        df.to_sql(
            name = table_name,
            con = conn,
            if_exists = 'append',
            index = False
        )
        print('Dados carregados com sucesso ✅')

    except Exception as e:
        print(f'Error ao carregar os dados:{e}')

