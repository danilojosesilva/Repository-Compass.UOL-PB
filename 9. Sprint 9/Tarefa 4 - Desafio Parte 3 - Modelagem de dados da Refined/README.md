# Modelagem de Dados - Camada Refined

Nesta tarefa, foi realizada a modelagem dos dados na camada Refined do data lake. A camada Refined contém os dados prontos para análise e extração de insights, seguindo os princípios de modelagem multidimensional.

## Tabelas iniciais (crawlers)

A seguir está o passo a passo detalhado do processo de modelagem de dados:

1. Utilizando o AWS Glue, foi criado um database chamado "trusted_db" no AWS Glue Data Catalog.

2. Foram criados dois crawlers, "Movies_db" e "TMDB_db", no AWS Glue para criar as tabelas com base nos dados da camada Trusted.

3. A tabela "movies" foi criada no database "trusted_db", utilizando o arquivo .parquet do diretório 's3://data-lake-danilo/Trusted/Movies/' do bucket S3 'data-lake-danilo'. Essa tabela possui 15 colunas: id, titulopincipal, titulooriginal, anolancamento, tempominutos, genero, notamedia, numerovotos, generoartista, personagem, nomeartista, anonascimento, anofalecimento, profissao e titulosmaisconhecidos.

4. A tabela "tmdb15" foi criada no database "trusted_db", utilizando o arquivo .parquet do diretório 's3://data-lake-danilo/Trusted/TMDB/2023/06/15/' do bucket S3 'data-lake-danilo'. Essa tabela possui 5 colunas: estudio, id, orcamento, popularidade e receita.

<p align="center"><img src="assets\Print_5.jpg"></p>

<p align="center"><img src="assets\Print_6.jpg"></p>

## Estrutura dos Dados

Para atender aos requisitos de consulta e visualização dos dados de diferentes perspectivas, foram criadas as seguintes tabelas no AWS Glue Data Catalog, com base nos dados da camada Trusted Zone:

<p align="center"><img src="assets\Print_1.jpg"></p>

### Tabela 'facts_movies'

Esta tabela contém informações sobre os filmes, incluindo os dados de orçamento, popularidade, receita, notas médias e número de votos. A tabela possui as seguintes colunas:

- id_estudios (string): chave estrangeira referenciando a tabela 'dim_studios'.
- orcamento (bigint): valor do orçamento do filme.
- popularidade (double): valor da popularidade do filme.
- receita (bigint): valor da receita do filme.
- id_filmes (string): chave estrangeira referenciando a tabela 'dim_movies'.
- notamedia (double): nota média do filme.
- numerovotos (int): número de votos recebidos pelo filme.

<p align="center"><img src="assets\Print_4.jpg"></p>

### Tabela 'dim_studios'

Esta tabela contém informações sobre os estúdios de filmes. A tabela possui as seguintes colunas:

- id_estudios (string): chave primária identificadora do estúdio.
- estudio (string): nome do estúdio.

<p align="center"><img src="assets\Print_2.jpg"></p>

### Tabela 'dim_movies'

Esta tabela contém informações sobre os filmes, incluindo o título original, ano de lançamento e gênero. A tabela possui as seguintes colunas:

- id_filmes (string): chave primária identificadora do filme.
- titulooriginal (string): título original do filme.
- anolancamento (int): ano de lançamento do filme.
- genero (string): gênero do filme.

<p align="center"><img src="assets\Print_3.jpg"></p>

## Modelagem dimensional

Foi criado um modelo lógico dimensional utilizando os recursos do site 'https://online.visual-paradigm.com/pt/' para demonstrar as relações entre as tabelas com as respectivas chaves primárias e estrangeiras.

<p align="center"><img src="assets\Diagrama_dimensional.jpg"></p>

## Considerações Finais

A modelagem de dados na camada Refined foi realizada com sucesso, seguindo as práticas de modelagem multidimensional. As tabelas 'facts_movies', 'dim_studios' e 'dim_movies' foram criadas no AWS Glue Data Catalog, proporcionando a disponibilidade dos dados para a ferramenta de visualização. Os dados foram estruturados de forma a permitir consultas e análises eficientes em diferentes perspectivas. O processo de modelagem foi executado com o uso do AWS Glue e seus recursos, garantindo a integridade e a qualidade dos dados na camada Refined. As tabelas foram devidamente criadas e estão prontas para serem utilizadas na próxima etapa do projeto.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>