from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Inicializa uma sessão Spark
spark = SparkSession.builder.getOrCreate()

# Carrega o arquivo de texto como um DataFrame
file_path = "README.md"
df = spark.read.text(file_path)

# Separa as palavras em cada linha usando espaço como delimitador
words = df.select(explode(split(df.value, " ")).alias("word"))

# Calcula a contagem de frequência de palavras
word_counts = words.groupBy("word").count()

# Exibe a contagem de frequência de todas as palavras
word_counts.show(word_counts.count(), truncate=False)
