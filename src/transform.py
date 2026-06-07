import pandas as pd
import requests as rs
from dotenv import load_dotenv
import os
from pathlib import Path
import json

path_name = Path(__file__).parent.parent /'data' / 'weather_data.json'
columns_name_to_drop = ['weather','weather_icon','sys.type']
columns_names_to_rename = {
        "base": "base",
        "visibility": "visibility",
        "dt": "datetime",
        "timezone": "timezone",
        "id": "city_id", 
        "name": "city_name",
        "cod": "code",
        "coord.lon": "longitude",
        "coord.lat": "latitude",
        "main.temp": "temperature",
        "main.feels_like": "feels_like",
        "main.temp_min": "temp_min",
        "main.temp_max": "temp_max",
        "main.pressure": "pressure",
        "main.humidity": "humidity",
        "main.sea_level": "sea_level",
        "main.grnd_level": "grnd_level",
        "wind.speed": "wind_speed",
        "wind.deg": "wind_deg",
        "wind.gust": "wind_gust",
        "clouds.all": "clouds", 
        "sys.type": "sys_type",                 
        "sys.id": "sys_id",                
        "sys.country": "country",                
        "sys.sunrise": "sunrise",                
        "sys.sunset": "sunset",
        # weather_id, weather_main, weather_description 
    }

columns_to_normalize_datetime = ['datetime', 'sunrise', 'sunset']


def create_dataframe(path_name:str) -> pd.DataFrame:

    path = path_name

    if not path.exists():
        print('Pasta não encontrada')

    with open(path_name) as f:
        data = json.load(f)
        print('Dados carregados com sucesso, iniciando normalização...')

        data = pd.json_normalize(data)
        print('Dados normalizados com sucesso')

        return data
 
def normalize_weather_columns(df: pd.DataFrame) -> pd.DataFrame:   

    #Passando uma função lambda para pegar o índice[0] do valor weather dentro do json

    df_weather = pd.json_normalize(df['weather'].apply(lambda x: x[0]))

    print('Iniciando renomeação de colunas...')
    df_weather = df_weather.rename(columns={
        'id': 'weather_id',
        'main': 'weather_main',
        'description':'weather_description',
        'icon':'weather_icon'}
        )
    df = pd.concat([df,df_weather],axis=1)

    return df

def drop_columns(df:pd.DataFrame,columns_names:list[str]) -> pd.DataFrame:
    df = df.drop(columns=columns_names)
    print('Colunas removidas com sucesso')
    
    return df

def rename_columns(df:pd.DataFrame,columns_name:dict[str,str]) -> pd.DataFrame:
                   
    df = df.rename(columns=columns_name)

    return df

def normalize_date_time(df:pd.DataFrame,columns_names:list[str]) -> pd.DataFrame:
   for name in columns_names:
       df[name] = pd.to_datetime(df[name], unit='s',utc=True).dt.tz_convert('America/Sao_Paulo')

   return df

def transformations():
    print('\n Iniciando as alterações....')

    df = create_dataframe(path_name)

    df = normalize_weather_columns(df)
    
    df = drop_columns(df,columns_name_to_drop)
    
    df = rename_columns(df,columns_names_to_rename)

    df = normalize_date_time(df,columns_to_normalize_datetime)


    return df


transformations()

