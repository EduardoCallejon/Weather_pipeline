import pandas as pd
import requests as rs
from dotenv import load_dotenv
import os
from pathlib import Path
import json

dotenv_path = Path(__file__).parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv('API_KEY')
if API_KEY is None:
    raise ValueError("A chave API não consta no arquivo, verifique o arquivo .env e tente novamente.")
else:
    print("API_KEY carregada com sucesso.")

url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo, BR&units=metric&appid={API_KEY}'


def extract_data(url: str) -> list:

    response = rs.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Erro ao acessar a API: {response.status_code} - {data.get('message', 'No message')}")
        return []
    if not data:
        print("Nenhum dado retornado pela API.")
        return []

    #Mapeamento de pastas
    output_destiny = 'data/weather_data.json'
    output_dir = Path(output_destiny).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_destiny, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Dados extraídos e salvos em {output_destiny}")

    return data


extract_data(url)


