# Importação de pacotes necessários
import os
import time
import json
import boto3
import requests
import pandas as pd
from datetime import datetime

# Função para obter dados de um filme específico
def obter_dados_filme(filme_id, api_key):
    """Função para consultar a API do themoviedb e obter detalhes de um filme"""

    # Criação da URL de consulta à API
    url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={api_key}'

    # Requisição GET para a API
    response = requests.get(url)
    data = response.json()

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        return data['popularity'], data['revenue']  # Retorno da popularidade e receita do filme

    # Intervalo de tempo para evitar exceder o limite de requisições por segundo da API
    time.sleep(0.02)

    # Se a requisição falhar, retorna None para popularidade e receita
    return None, None

def lambda_handler(event, context):
    """Função principal que será chamada quando a lambda for executada"""
    
    # Configuração de variáveis do ambiente de execução
    api_key = os.getenv("API_KEY_TMDB")
    aws_access_key_id = os.getenv("AWS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_KEY_ACCESS")
    region_name = 'us-east-1'
    
    # Configuração de variáveis relacionadas ao S3
    bucket_name = 'data-lake-danilo'
    key = 'Raw/Local/CSV/Movies/2023/05/19/movies.csv'
    storage_layer = 'Raw'
    data_source = 'TMDB'
    data_format = 'JSON'
    current_date = datetime.now().strftime('%Y/%m/%d')

    # Configuração de variáveis relacionadas ao processamento de dados
    selected_columns = ['id', 'genero']
    generos_filtrados = ['Horror']
    chunk_size = 100  # Tamanho do lote de filmes para processar de cada vez

    # Criação do cliente S3
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Obtenção do objeto CSV do S3
    response = s3.get_object(Bucket=bucket_name, Key=key)

    # Leitura do CSV para um DataFrame, selecionando apenas as colunas de interesse
    df = pd.read_csv(response['Body'], delimiter='|', usecols=selected_columns, dtype={'id': str})

    # Filtragem do DataFrame por gênero
    df_filtrado = df[df['genero'].isin(generos_filtrados)]

    # Obtenção de uma lista única de IDs de filmes após a filtragem
    ids_filmes_filtrados = df_filtrado['id'].unique()

    # Divisão da lista de IDs de filmes em lotes (chunks)
    df_chunks = [ids_filmes_filtrados[i:i+chunk_size] for i in range(0, len(ids_filmes_filtrados), chunk_size)]

    # Iteração sobre cada lote de IDs de filmes
    for i, lote in enumerate(df_chunks):
        filmes_dados = {}

        # Para cada ID de filme no lote, consulta os detalhes do filme e os adiciona ao dicionário filmes_dados
        for filme_id in lote:
            popularidade, receita = obter_dados_filme(filme_id, api_key)
            if popularidade is not None and receita is not None:
                filmes_dados[filme_id] = {
                    'popularidade': popularidade,
                    'receita': receita
                }

        # Salva o dicionário de dados de filmes como um arquivo JSON no S3
        data_specification = f'movies_tmdb_'
        file_name = f'{data_specification}_{str(i).zfill(3)}.json'
        dados_json = json.dumps(filmes_dados, ensure_ascii=False)
        s3.put_object(Body=dados_json, Bucket=bucket_name, Key=f'{storage_layer}/{data_source}/{data_format}/{current_date}/{data_specification}/{file_name}')

    # Retorna uma resposta indicando que a execução foi bem-sucedida
    return {
        'statusCode': 200,
        'body': 'Dados salvos no AWS S3 com sucesso!'
    }
