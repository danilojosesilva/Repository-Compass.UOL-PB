import os
import time
import json
import boto3
import requests
import pandas as pd
import numpy as np
from datetime import datetime

def obter_dados_filme(filme_id, api_key):
    # Consultar a API do themoviedb
    url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        studio = data['production_companies'][0]['name'] if data['production_companies'] else None
        return {"id": filme_id, "popularidade": data['popularity'], "receita": data['revenue'], "estudio": studio, "orcamento": data['budget']}
    return None

def processar_lote_filmes(lote_ids, api_key, bucket_name, storage_layer, data_source, data_format, current_date):
    filmes_dados = []
    for filme_id in lote_ids:
        filme_dado = obter_dados_filme(filme_id, api_key)
        if filme_dado is not None:
            filmes_dados.append(filme_dado)
        time.sleep(0.02)  # Para evitar limitação da API

    # Salvar no S3
    data_specification = f'movies_tmdb_{str(lote_ids[0]).zfill(3)}-{str(lote_ids[-1]).zfill(3)}'
    file_name = f'{data_specification}.json'
    dados_json = json.dumps(filmes_dados, ensure_ascii=False)
    s3 = boto3.client('s3')
    s3.put_object(Body=dados_json, Bucket=bucket_name, Key=f'{storage_layer}/{data_source}/{data_format}/{current_date}/{data_specification}/{file_name}')

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
    chunk_size = 100  

    # Iniciar cliente S3 e obter objeto CSV
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    response = s3.get_object(Bucket=bucket_name, Key=key)

    # Filtrar DataFrame por gênero e criar chunks de filmes
    df = pd.read_csv(response['Body'], delimiter='|', usecols=selected_columns, dtype={'id': str})
    df_filtrado = df[df['genero'].str.contains('Horror', na=False)]  # Filtrar por filmes que contêm 'Horror' em seu campo de gênero
    ids_filmes_filtrados = df_filtrado['id'].unique()  # Remover IDs repetidos

    # Dividir IDs dos filmes em lotes menores
    lote_ids = np.array_split(ids_filmes_filtrados, np.ceil(len(ids_filmes_filtrados) / chunk_size))

    # Invocar assincronamente novas execuções do Lambda para processar cada lote de IDs
    lambda_client = boto3.client('lambda')
    lambda_function_name = context.function_name

    for lote in lote_ids:
        payload = {
            'lote_ids': lote.tolist(),
            'api_key': api_key,
            'bucket_name': bucket_name,
            'storage_layer': storage_layer,
            'data_source': data_source,
            'data_format': data_format,
            'current_date': current_date
        }
        lambda_client.invoke(
            FunctionName=lambda_function_name,
            InvocationType='Event',  # Invocação assíncrona
            Payload=json.dumps(payload)
        )

    return {
        'statusCode': 200,
        'body': 'Processamento iniciado!'
    }
