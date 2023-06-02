from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import col, when, rand
from pyspark.sql.types import StringType

# Inicializando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Lendo o arquivo e carregando em um dataframe
df_nomes = spark.read.csv('nomes_aleatorios.txt', header=True)
df_nomes.show(5)

# Renomeando a coluna e imprimindo o esquema
df_nomes = df_nomes.withColumnRenamed(df_nomes.columns[0], 'Nomes')
df_nomes.printSchema()
df_nomes.show(10)

# Adicionando a coluna Escolaridade com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").when(rand() < 0.66, "Medio").otherwise("Superior"))

# Adicionando a coluna Pais com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 0.076, "Argentina").when(rand() < 0.153, "Bolívia")
    .when(rand() < 0.230, "Brasil").when(rand() < 0.307, "Chile")
    .when(rand() < 0.384, "Colômbia").when(rand() < 0.461, "Equador")
    .when(rand() < 0.538, "Guiana").when(rand() < 0.615, "Paraguai")
    .when(rand() < 0.692, "Peru").when(rand() < 0.769, "Suriname")
    .when(rand() < 0.846, "Uruguai").when(rand() < 0.923, "Venezuela")
    .otherwise("Guiana Francesa"))

# Adicionando a coluna AnoNascimento com valores aleatórios
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (rand() * (2010 - 1945) + 1945).cast("int"))

# Selecionando pessoas que nasceram neste século e armazenando o resultado em um novo DataFrame
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)

# Criando uma tabela temporária para consultas SQL
df_nomes.createOrReplaceTempView("pessoas")

# Usando Spark SQL para fazer a mesma seleção
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)

# Contando o número de pessoas da geração Millennial (nascidos entre 1980 e 1994)
spark.sql("SELECT COUNT(*) as Number_of_Millennials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").show()

# Finalmente, obtemos a quantidade de pessoas de cada país para cada geração
df_resultado = spark.sql("""
SELECT Pais,
CASE 
    WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
    WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
    WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
    WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
    ELSE 'Outros'
END as Geracao,
COUNT(*) as Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_resultado.show()
