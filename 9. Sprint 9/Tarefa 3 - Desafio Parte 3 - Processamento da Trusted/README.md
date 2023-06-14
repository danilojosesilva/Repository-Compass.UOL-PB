# Processamento da Trusted

Este documento descreve as tarefas realizadas para processar a camada Trusted do data lake. Foram realizados dois jobs utilizando o Apache Spark no AWS Glue para processar os dados na camada Raw e armazená-los na camada Trusted.

<p align="center"><img src="assets\Print_7.jpg"></p>

## Job 1: Processamento dos Dados CSV

O primeiro job foi responsável pelo processamento dos dados CSV. Os dados foram lidos dos seguintes locais na camada Raw:

`s3://data-lake-danilo/Raw/Local/CSV/Movies/2023/05/19/movies.csv`

`s3://data-lake-danilo/Raw/Local/CSV/Series/2023/05/19/series.csv`

Após o processamento, os dados foram gravados na camada Trusted no formato Parquet, em um único arquivo para cada pasta, usando os seguintes caminhos:

`s3://data-lake-danilo/Trusted/CSV/Series/`

`s3://data-lake-danilo/Trusted/CSV/Movies/`

<p align="center"><img src="assets\Print_1.jpg"></p>

<p align="center"><img src="assets\Print_2.jpg"></p>

<p align="center"><img src="assets\Print_3.jpg"></p>

## Job 2: Processamento dos Dados TMDB

O segundo job foi responsável pelo processamento dos dados TMDB, que estão em formato JSON. Os dados foram lidos do seguinte local na camada Raw:

`s3://data-lake-danilo/Raw/TMDB/JSON/2023/06/14/movies_tmdb_/`

Após o processamento, os dados foram gravados na camada Trusted no formato Parquet, em um único arquivo, usando o seguinte caminho:

`s3://data-lake-danilo/Trusted/TMDB/`

<p align="center"><img src="assets\Print_4.jpg"></p>

<p align="center"><img src="assets\Print_5.jpg"></p>

<p align="center"><img src="assets\Print_6.jpg"></p>

Ambos os jobs foram configurados para utilizar o worker type G.1X e 2 workers. O tempo limite do job foi definido como 60 minutos.

<p align="center"><img src="assets\Print_8.jpg"></p>

<p align="center"><img src="assets\Print_9.jpg"></p>

<p align="center"><img src="assets\Print_10.jpg"></p>

<p align="center"><img src="assets\Print_11.jpg"></p>

<p align="center"><img src="assets\Print_12.jpg"></p>

<p align="center"><img src="assets\Print_13.jpg"></p>

Os jobs foram monitorados para garantir que eles foram executados corretamente e foram finalizados após a conclusão para evitar custos desnecessários.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>