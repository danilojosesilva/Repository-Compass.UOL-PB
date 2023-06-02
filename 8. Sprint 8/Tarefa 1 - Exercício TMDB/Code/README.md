# Buscador de Filmes Mais Bem Avaliados

Este é um projeto Python simples que usa a API do The Movie Database (TMDB) para buscar a lista dos filmes mais bem avaliados e exibir em um DataFrame do Pandas.

## Pré-requisitos

Para executar este script, você precisará:

- Python 3.6 ou superior
- Bibliotecas Python: `requests`, `pandas`, `IPython`
- Uma chave de API do The Movie Database (TMDB)

## Como usar

1. Insira sua chave de API do TMDB na variável `api_key`.
2. Execute o script. O código irá buscar a lista de filmes mais bem avaliados no TMDB.

## Funcionamento

O código inicia importando as bibliotecas necessárias. Em seguida, define a URL da API com a chave de API e a configuração de idioma desejado.

O script então realiza uma requisição GET para a URL, transforma a resposta (um objeto JSON) em um dicionário Python e cria uma lista vazia para armazenar os dados dos filmes.

O script itera através da lista de filmes retornados pela API, cria um dicionário com os dados que queremos de cada filme, e adiciona o dicionário à lista de filmes.

Finalmente, transforma a lista de dicionários em um DataFrame do Pandas e exibe o DataFrame em um formato bonito.

Os dados exibidos para cada filme incluem o título, a data de lançamento, uma visão geral do enredo, a contagem de votos e a média dos votos.

## Conclusão

Este é um projeto simples, porém muito útil para aqueles que desejam explorar dados de filmes. Ele pode ser facilmente estendido para buscar outros dados do TMDB, ou adaptado para trabalhar com outras APIs. Além disso, os dados coletados podem ser usados para análises mais profundas, visualizações ou qualquer outro uso que se possa imaginar para dados de filmes. Aproveite para explorar e expandir de acordo com suas necessidades e interesses!

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>