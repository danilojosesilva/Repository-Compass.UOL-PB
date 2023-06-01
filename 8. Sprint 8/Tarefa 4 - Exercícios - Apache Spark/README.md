# Apache Spark

O Apache Spark é um framework de processamento de dados em larga escala, projetado para ser rápido e de fácil utilização. Ele oferece APIs de alto nível em Java, Scala, Python e R, e um motor otimizado que suporta a execução de gráficos de computação em geral.

## Tarefas

Esta série de tarefas envolve o uso do Apache Spark para ler um arquivo de texto contendo nomes e realizar várias operações, incluindo a adição de colunas com dados gerados aleatoriamente, filtrando dados e executando consultas SQL.

## Preparação do ambiente

Inicialmente, é necessário preparar o ambiente para execução do código. Neste caso, será utilizado o PySpark para executar em ambiente local. Para isso, é necessário ter o Spark e o PySpark instalados.

## Leitura de arquivo

O arquivo de entrada é um arquivo de texto chamado 'nomes_aleatorios.txt'. O arquivo é lido para dentro de um dataframe Spark chamado df_nomes.

<p align="center"><img src="assets\Print_7.png"></p>

<p align="center"><img src="assets\Print_8.png"></p>

## Modificação do dataframe

Serão adicionadas três colunas ao dataframe:

- **Escolaridade**: será preenchida aleatoriamente com um dos três valores: 'Fundamental', 'Medio' e 'Superior'.
- **Pais**: será preenchida aleatoriamente com um dos treze países da América do Sul.
- **AnoNascimento**: será preenchida aleatoriamente com um ano entre 1945 e 2010.

## Filtragem e consulta de dados

Em seguida, será realizada uma série de operações para filtrar e consultar os dados. Essas operações incluem:

- Selecionar pessoas que nasceram neste século
- Contar o número de pessoas da geração 'Millennials' (nascidos entre 1980 e 1994)
- Obter a quantidade de pessoas de cada país para cada geração.

## Executando operações com Spark SQL

Algumas dessas operações serão repetidas usando Spark SQL, uma interface para executar consultas SQL no Spark.

## Executando o código

Para executar o código, é necessário ter o Apache Spark e o PySpark instalados em seu ambiente. Também será preciso de um arquivo de texto chamado 'nomes_aleatorios.txt' no mesmo diretório que o seu script Python.

Depois de satisfazer essas dependências, é possível executar o script Python que contém o código.

### Scripts

1. O primeiro script carrega os dados:

```python
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import col, when
from pyspark.sql.types import StringType

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv('nomes_aleatorios.txt', header=True)
df_nomes.show(5)
```

<p align="center"><img src="assets\Print_1.png"></p>

2. O segundo script renomeia a coluna e imprime o esquema:

```python
df_nomes = df_nomes.withColumnRenamed(df_nomes.columns[0], 'Nomes')
df_nomes.printSchema()
df_nomes.show(10)
```
<p align="center"><img src="assets\Print_2.png"></p>

3. O terceiro script adiciona as colunas Escolaridade, Pais e AnoNascimento. Para gerar valores aleatórios, foi usada a função when do Spark SQL para definir condições para cada novo valor de coluna:

```python
from pyspark.sql.functions import rand

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").when(rand() < 0.66, "Medio").otherwise("Superior"))

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 0.076, "Argentina").when(rand() < 0.153, "Bolívia")
    .when(rand() < 0.230, "Brasil").when(rand() < 0.307, "Chile")
    .when(rand() < 0.384, "Colômbia").when(rand() < 0.461, "Equador")
    .when(rand() < 0.538, "Guiana").when(rand() < 0.615, "Paraguai")
    .when(rand() < 0.692, "Peru").when(rand() < 0.769, "Suriname")
    .when(rand() < 0.846, "Uruguai").when(rand() < 0.923, "Venezuela")
    .otherwise("Guiana Francesa"))

df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (rand() * (2010 - 1945) + 1945).cast("int"))

df_nomes.show(5)
```

<p align="center"><img src="assets\Print_3.png"></p>

4. O quarto script seleciona as pessoas que nasceram e armazena o resultado em um novo DataFrame:

```python
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)
```

5. O quinto script faz o mesmo que o quarto, usando Spark SQL:

```python
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)
```

<p align="center"><img src="assets\Print_4.png"></p>

6. O sexto script conta o número de pessoas da geração Millennial (nascidos entre 1980 e 1994):

```python
df_millennials = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994))
print("Número de Millennials: ", df_millennials.count())
```

7. O sétimo script faz o mesmo que o sexto, usando Spark SQL:

```python
spark.sql("SELECT COUNT(*) as Number_of_Millennials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").show()
```

8. Finalmente, o oitavo script obtém a quantidade de pessoas de cada país para cada geração:

```python
df_resultado = spark.sql("""
SELECT Pais,
CASE 
    WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
    WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
    WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
    WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
    ELSE 'Outros'
END as Geracao,
COUNT(*) as Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_resultado.show()
```

<p align="center"><img src="assets\Print_5.png"></p>

<p align="center"><img src="assets\Print_6.png"></p>

## Dependências

- Python 3.6 ou superior
- Apache Spark 2.4.0 ou superior
- PySpark 2.4.0 ou superior
- Arquivo de dados de entrada: 'nomes_aleatorios.txt'

## Instalação

Para instalar o PySpark, você pode usar o pip:

`pip install pyspark`

## Considerações

O Spark é uma ferramenta de processamento distribuído e, portanto, é projetado para trabalhar com grandes conjuntos de dados. Para conjuntos de dados menores, as operações do Spark podem ser menos eficientes do que as operações correspondentes em ferramentas projetadas para dados em memória, como Pandas. 

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>