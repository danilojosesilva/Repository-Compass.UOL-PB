import pandas as pd

df = pd.read_csv("actors.csv")

#Ator/atriz c/ maior número de filmes e respec. filme
ator_com_mais_filmes = df.loc[df["Number of Movies"].idxmax(), "Actor"]
num_filmes_mais = df["Number of Movies"].max()
print(f"Ator/atrizes com mais filmes: {ator_com_mais_filmes}, {num_filmes_mais} filmes")

#Média do nº de filmes
media_num_filmes = df["Number of Movies"].mean()
print(f"Média de número de filmes: {media_num_filmes:.2f}")

#Ator/atriz com maior média per filme
ator_maior_media = df.loc[df["Average per Movie"].idxmax(), "Actor"]
maior_media_filme = df["Average per Movie"].max()
print(f"Ator/atrizes com maior média por filme: {ator_maior_media}, {maior_media_filme:.2f}")

#Filme mais frequente
filmes_mais_frequentes = df[df["#1 Movie"].duplicated(keep=False)]
frequencia_filmes_mais_frequentes = filmes_mais_frequentes.groupby("#1 Movie").size()
frequencia_maxima = frequencia_filmes_mais_frequentes.max()
filmes_mais_frequentes = frequencia_filmes_mais_frequentes[frequencia_filmes_mais_frequentes == frequencia_maxima]
for filme, frequencia in filmes_mais_frequentes.items():
    print(f"Filme: {filme}, Frequência: {frequencia}")
