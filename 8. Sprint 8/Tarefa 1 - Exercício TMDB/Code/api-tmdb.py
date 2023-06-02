import requests  
import pandas as pd  
from IPython.display import display

# Sua chave de API para o serviço the movie database
api_key = "MINHA_CHAVE"

# URL do serviço da API, usando f-string para inserir a chave de API e a configuração do idioma desejado
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

# Fazendo uma requisição GET para a URL fornecida
response = requests.get(url)

# Transformando a resposta da requisição (um objeto JSON) em um dicionário Python
data = response.json()

# Criando uma lista vazia para armazenar os dados dos filmes
filmes = []

# Iterando através da lista de filmes retornados pela API
for movie in data['results']:
    # Cria um dicionário com os dados que queremos de cada filme
    df = {'Titulo': movie['title'],
          'Data de lançamento': movie['release_date'],
          'Visão geral': movie['overview'],
          'Votos': movie['vote_count'],
          'Média de votos:': movie['vote_average']}

    # Adiciona o dicionário do filme à lista de filmes
    filmes.append(df)

# Transforma a lista de dicionários em um DataFrame do Pandas
df = pd.DataFrame(filmes)

# Mostra o DataFrame em uma tabela bonita
display(df)
