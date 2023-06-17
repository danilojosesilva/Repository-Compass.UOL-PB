# Processamento da Trusted

Este documento descreve as tarefas realizadas para processar a camada Trusted do data lake. Foi realizado um job (processamento_job) utilizando o Apache Spark no AWS Glue para processar os dados na camada Raw e armazená-los na camada Trusted.

<p align="center"><img src="assets\Print_8.jpg"></p>

## Job: Processamento dos Dados CSV e TMDB

O job foi responsável pelo processamento dos dados CSV e TMDB. Os dados foram lidos dos seguintes locais na camada Raw:

`s3://data-lake-danilo/Raw/Local/CSV/Movies/2023/05/19/movies.csv`

`s3://data-lake-danilo/Raw/Local/CSV/Series/2023/05/19/series.csv`

`s3://data-lake-danilo/Raw/TMDB/JSON/2023/06/14/movies_tmdb_/`

Após o processamento, os dados foram gravados na camada Trusted no formato Parquet, em um único arquivo para cada pasta, usando os seguintes caminhos:

`s3://data-lake-danilo/Trusted/Movies/`

`s3://data-lake-danilo/Trusted/Series/`

`s3://data-lake-danilo/Trusted/TMDB/`

<p align="center"><img src="assets\Print_4.jpg"></p>

<p align="center"><img src="assets\Print_5.jpg"></p>

<p align="center"><img src="assets\Print_6.jpg"></p>

<p align="center"><img src="assets\Print_7.jpg"></p>

Ambos os jobs foram configurados para utilizar o worker type G.1X e 2 workers. O tempo limite do job foi definido como 60 minutos.

<p align="center"><img src="assets\Print_1.jpg"></p>

<p align="center"><img src="assets\Print_2.jpg"></p>

<p align="center"><img src="assets\Print_3.jpg"></p>

O job foi monitorado para garantir que foi executado corretamente e foi finalizado após a conclusão para evitar custos desnecessários.

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>