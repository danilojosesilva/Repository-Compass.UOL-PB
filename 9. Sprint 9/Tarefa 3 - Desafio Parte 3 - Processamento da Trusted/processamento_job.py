import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

movies_path = source_file + '/Local/CSV/Movies/2023/05/19/movies.csv'
series_path = source_file + '/Local/CSV/Series/2023/05/19/series.csv'

df_movies = spark.read.csv(movies_path, header=True, inferSchema=True, sep='|')
df_series = spark.read.csv(series_path, header=True, inferSchema=True, sep='|')

json_files = [source_file + '/TMDB/JSON/2023/06/15/movies_tmdb_/movies_tmdb__{:03d}.json'.format(i) for i in range(64)]
df_filmes = spark.read.json(json_files)

movies_output_path = target_path + '/Movies'
series_output_path = target_path + '/Series'
dadosFilmes_output_path = target_path + '/TMDB/2023/06/15/movies_tmdb_'

compression_codec = "uncompressed"
block_size = "134217728"

# Salvando os DataFrames com as opções definidas
df_movies.repartition(1).write.format("parquet").option("compression", compression_codec).option("parquet.block.size", block_size).save(movies_output_path)
df_series.repartition(1).write.format("parquet").option("compression", compression_codec).option("parquet.block.size", block_size).save(series_output_path)
df_filmes.repartition(1).write.format("parquet").option("compression", compression_codec).option("parquet.block.size", block_size).save(dadosFilmes_output_path)



job.commit()
