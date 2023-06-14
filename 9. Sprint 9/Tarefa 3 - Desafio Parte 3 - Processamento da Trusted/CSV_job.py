from pyspark.sql import SparkSession

# Criação de uma sessão Spark
spark = SparkSession.builder.appName("job-dados-csv").getOrCreate()

# Leitura dos dados CSV de filmes da zona Raw, usando "|" como separador de colunas
dados_csv_filmes_brutos = spark.read.format("csv").option("header", "true").option("delimiter", "|").load("s3://data-lake-danilo/Raw/Local/CSV/Movies/2023/05/19/movies.csv")

# Gravação dos dados CSV de filmes na zona Trusted no formato Parquet.
# Usando coalesce(1) para garantir que todos os dados sejam escritos em um único arquivo Parquet.
dados_csv_filmes_brutos.coalesce(1).write.format("parquet").mode("overwrite").save("s3://data-lake-danilo/Trusted/Movies/")

# Leitura dos dados CSV de séries da zona Raw, usando "|" como separador de colunas
dados_csv_series_brutos = spark.read.format("csv").option("header", "true").option("delimiter", "|").load("s3://data-lake-danilo/Raw/Local/CSV/Series/2023/05/19/series.csv")

# Gravação dos dados CSV de séries na zona Trusted no formato Parquet.
# Usando coalesce(1) para garantir que todos os dados sejam escritos em um único arquivo Parquet.
dados_csv_series_brutos.coalesce(1).write.format("parquet").mode("overwrite").save("s3://data-lake-danilo/Trusted/Series/")
