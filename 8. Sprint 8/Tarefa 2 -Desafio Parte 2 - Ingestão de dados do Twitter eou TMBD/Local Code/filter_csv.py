import pandas as pd

# Substitua isso pelo caminho do seu arquivo CSV
file_path = 'movies.csv'

# Ler o arquivo CSV para um DataFrame
df = pd.read_csv(file_path, sep='|', encoding='utf-8')

# Filtrar o DataFrame para apenas filmes de terror
horror_movies_df = df[df['genero'] == 'Horror']

# Se você quer salvar isso em um novo arquivo CSV:
horror_movies_df.to_csv('filtered_horror_movies.csv', sep='|', index=False, encoding='utf-8')
