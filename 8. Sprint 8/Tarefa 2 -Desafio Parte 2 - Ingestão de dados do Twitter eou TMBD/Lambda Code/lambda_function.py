import os
import time
import json
import boto3
import requests
import pandas as pd
from datetime import datetime

def obter_dados_filme(filme_id, api_key):
    # Consultar a API do themoviedb
    url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {"id": filme_id, "popularidade": data['popularity'], "receita": data['revenue']}
    return None

def lambda_handler(event, context):
    # Definição de variáveis de configuração
    api_key = os.getenv("API_KEY_TMDB")
    aws_access_key_id = os.getenv("AWS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_KEY_ACCESS")
    region_name = 'us-east-1'
    bucket_name = 'data-lake-danilo'
    key = 'Raw/Local/CSV/Movies/2023/05/19/movies.csv'
    storage_layer = 'Raw'
    data_source = 'TMDB'
    data_format = 'JSON'
    current_date = datetime.now().strftime('%Y/%m/%d')
    selected_columns = ['id', 'genero']
    generos_filtrados = ['Horror']
    chunk_size = 100  

    # Iniciar cliente S3 e obter objeto CSV
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    response = s3.get_object(Bucket=bucket_name, Key=key)

    # Filtrar DataFrame por gênero e criar chunks de filmes
    df = pd.read_csv(response['Body'], delimiter='|', usecols=selected_columns, dtype={'id': str})
    df_filtrado = df[df['genero'].isin(generos_filtrados)]
    ids_filmes_filtrados = df_filtrado['id'].unique()
    df_chunks = [ids_filmes_filtrados[i:i+chunk_size] for i in range(0, len(ids_filmes_filtrados), chunk_size)]

    # Iterar sobre cada chunk e obter dados do filme
    for i, lote in enumerate(df_chunks):
        filmes_dados = []
        for filme_id in lote:
            filme_dado = obter_dados_filme(filme_id, api_key)
            if filme_dado is not None:
                filmes_dados.append(filme_dado)
            time.sleep(0.02)  # Para evitar limitação da API

        # Salvar no S3
        data_specification = f'movies_tmdb_'
        file_name = f'{data_specification}_{str(i).zfill(3)}.json'
        dados_json = json.dumps(filmes_dados, ensure_ascii=False)
        s3.put_object(Body=dados_json, Bucket=bucket_name, Key=f'{storage_layer}/{data_source}/{data_format}/{current_date}/{data_specification}/{file_name}')

    return {
        'statusCode': 200,
        'body': 'Dados salvos no AWS S3 com sucesso!'
    }
