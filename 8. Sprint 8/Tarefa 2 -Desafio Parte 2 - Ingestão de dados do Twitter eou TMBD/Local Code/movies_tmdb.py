import pandas as pd
import requests
import json

# Substitua isso pelo caminho do seu arquivo CSV
file_path = 'filtered_horror_movies_no_duplicates.csv'

# Insira sua chave de API aqui
api_key = '2cfaaaec89d52639de0e409cf19b0cb4'

# Nome do arquivo de saída
output_filename = "movie_data_"

# Contador para diferentes arquivos
file_counter = 1

# Ler o arquivo CSV em lotes de 100 linhas
for chunk in pd.read_csv(file_path, sep='|', encoding='utf-8', chunksize=100):
    # Inicializar a lista de dados de filmes para o arquivo atual
    current_file_data = []

    # Para cada ID de filme no lote atual
    for movie_id in chunk['id']:
        # Fazer uma requisição à API TMDB
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
        
        # Se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Obter os dados do filme
            movie_data = response.json()
            
            # Criar um novo dicionário contendo apenas o id, título, popularidade e receita
            filtered_movie_data = {
                'popularity': movie_data['popularity'],
                'revenue': movie_data['revenue']
            }
            
            # Adicionar os dados filtrados do filme à lista atual
            current_file_data.append(filtered_movie_data)

    # Escrever os dados do filme em um arquivo JSON
    with open(f'{output_filename}{file_counter}.json', 'w', encoding='utf-8') as f:
        json.dump(current_file_data, f, ensure_ascii=False, indent=4)

    # Incrementar o contador de arquivos para começar um novo arquivo
    file_counter += 1
