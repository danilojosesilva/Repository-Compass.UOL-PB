from pyspark.sql import SparkSession

# Criação de uma sessão Spark
spark = SparkSession.builder.appName("job-dados-tmdb").getOrCreate()

# Leitura dos dados JSON da zona Raw. O Spark lê todos os arquivos JSON do diretório.
dados_json_brutos = spark.read.format("json").load("s3://data-lake-danilo/Raw/TMDB/JSON/2023/06/14/movies_tmdb_/")

# Gravação dos dados JSON na zona Trusted no formato Parquet.
# Usando coalesce(1) para garantir que todos os dados sejam escritos em um único arquivo Parquet.
dados_json_brutos.coalesce(1).write.format("parquet").mode("overwrite").save("s3://data-lake-danilo/Trusted/TMDB/2023/06/14/")
