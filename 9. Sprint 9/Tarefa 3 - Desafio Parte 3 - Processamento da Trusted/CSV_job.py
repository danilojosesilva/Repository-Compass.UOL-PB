from pyspark.sql import SparkSession

# Criação de uma sessão Spark
spark = SparkSession.builder.appName("job-dados-csv").getOrCreate()

# Leitura dos dados CSV da zona Raw
dados_csv_brutos = spark.read.format("csv").option("header", "true").load("s3://data-lake-danilo/Raw/Local/CSV/Movies/2023/05/19/movies.csv")

# Gravação dos dados CSV na zona Trusted no formato Parquet
dados_csv_brutos.write.format("parquet").mode("overwrite").save("s3://data-lake-danilo/Trusted/Movies/")
