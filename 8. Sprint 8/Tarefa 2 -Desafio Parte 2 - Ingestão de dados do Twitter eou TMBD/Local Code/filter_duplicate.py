import pandas as pd

# Substitua isso pelo caminho do seu arquivo CSV
file_path = 'filtered_horror_movies.csv'

# Ler o arquivo CSV para um DataFrame
df = pd.read_csv(file_path, sep='|', encoding='utf-8')

# Remover filmes duplicados com base no ID
df = df.drop_duplicates(subset='id')

# Salvar o DataFrame em um novo arquivo CSV
df.to_csv('filtered_horror_movies_no_duplicates.csv', sep='|', index=False)
