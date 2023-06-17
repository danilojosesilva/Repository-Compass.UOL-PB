# Processamento de dados - Camada Refined

Nesta tarefa, foi realizado o processamento dos dados da camada Trusted e seu armazenamento na camada Refined, de acordo com o modelo de dados definido.

## Passo a Passo

Aqui está o passo a passo detalhado do processo de processamento de dados:

1. Utilizando o Apache Spark, foram processados os dados provenientes da camada Trusted.

2. No AWS Glue, foram criadas as tabelas no AWS Glue Data Catalog para os dados provenientes da camada Trusted.

3. Utilizando o AWS Glue Visual ETL, foi feita a transformação e refinamento dos dados, seguindo o modelo de dados definido.

<p align="center"><img src="assets\Print_1.jpg"></p>

<p align="center"><img src="assets\Print_5.jpg"></p>

<p align="center"><img src="assets\Print_6.jpg"></p>

<p align="center"><img src="assets\Print_7.jpg"></p>

4. Foram aplicadas transformações nos dados, incluindo a remoção de duplicatas e a seleção das colunas necessárias.

<p align="center"><img src="assets\Print_2.jpg"></p>

5. Foi realizada a junção das tabelas "movies" e "tmdb15" com base na coluna "id", para obter todos os dados em um único esquema.

6. Foi aplicada uma consulta SQL para excluir as linhas em que a coluna "estudio" possui o valor "null".

<p align="center"><img src="assets\Print_3.jpg"></p>

7. Os dados foram divididos em três esquemas dimensionais: "facts_movies", "dim_studios" e "dim_movies", de acordo com o modelo de dados definido.

<p align="center"><img src="assets\Print_4.jpg"></p>

8. Os dados foram salvos na camada Refined no formato PARQUET. As tabelas foram armazenadas em diretórios específicos no bucket S3 "data-lake-danilo" da seguinte forma:
    - Tabela "facts_movies" foi salva no diretório 's3://data-lake-danilo/Refined/facts_movies/'.
    - Tabela "dim_studios" foi salva no diretório 's3://data-lake-danilo/Refined/dim_studios/'.
    - Tabela "dim_movies" foi salva no diretório 's3://data-lake-danilo/Refined/dim_movies/'.

<p align="center"><img src="assets\Print_14.jpg"></p>

<p align="center"><img src="assets\Print_15.jpg"></p>

<p align="center"><img src="assets\Print_16.jpg"></p>

<p align="center"><img src="assets\Print_17.jpg"></p>

## Script gerado pelo Visual ETL

A modelagem no Visual ETL gerou o seguinte Script para execução do job:

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node TB_tmdb
TB_tmdb_node1686929224438 = glueContext.create_dynamic_frame.from_catalog(
    database="trusted_db",
    table_name="tmdb15",
    transformation_ctx="TB_tmdb_node1686929224438",
)

# Script generated for node TB_movies
TB_movies_node1686929219298 = glueContext.create_dynamic_frame.from_catalog(
    database="trusted_db",
    table_name="movies",
    transformation_ctx="TB_movies_node1686929219298",
)

# Script generated for node TMDB
TMDB_node1687017571794 = ApplyMapping.apply(
    frame=TB_tmdb_node1686929224438,
    mappings=[
        ("estudio", "string", "estudio", "string"),
        ("id", "string", "id_tmdb", "string"),
        ("orcamento", "long", "orcamento", "bigint"),
        ("popularidade", "double", "popularidade", "double"),
        ("receita", "long", "receita", "bigint"),
    ],
    transformation_ctx="TMDB_node1687017571794",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1687019477385 = DynamicFrame.fromDF(
    TB_movies_node1686929219298.toDF().dropDuplicates(["id"]),
    glueContext,
    "DropDuplicates_node1687019477385",
)

# Script generated for node Movies
Movies_node1687017814402 = ApplyMapping.apply(
    frame=DropDuplicates_node1687019477385,
    mappings=[
        ("id", "string", "id_filmes", "string"),
        ("titulooriginal", "string", "titulooriginal", "string"),
        ("anolancamento", "string", "anolancamento", "int"),
        ("genero", "string", "genero", "string"),
        ("notamedia", "double", "notamedia", "double"),
        ("numerovotos", "int", "numerovotos", "int"),
    ],
    transformation_ctx="Movies_node1687017814402",
)

# Script generated for node Join
TMDB_node1687017571794DF = TMDB_node1687017571794.toDF()
Movies_node1687017814402DF = Movies_node1687017814402.toDF()
Join_node1687017937040 = DynamicFrame.fromDF(
    TMDB_node1687017571794DF.join(
        Movies_node1687017814402DF,
        (
            TMDB_node1687017571794DF["id_tmdb"]
            == Movies_node1687017814402DF["id_filmes"]
        ),
        "left",
    ),
    glueContext,
    "Join_node1687017937040",
)

# Script generated for node Database
Database_node1687018131322 = ApplyMapping.apply(
    frame=Join_node1687017937040,
    mappings=[
        ("estudio", "string", "estudio", "string"),
        ("id_tmdb", "string", "id_tmdb", "string"),
        ("orcamento", "bigint", "orcamento", "bigint"),
        ("popularidade", "double", "popularidade", "double"),
        ("receita", "bigint", "receita", "bigint"),
        ("id_filmes", "string", "id_filmes", "string"),
        ("titulooriginal", "string", "titulooriginal", "string"),
        ("anolancamento", "int", "anolancamento", "int"),
        ("genero", "string", "genero", "string"),
        ("notamedia", "double", "notamedia", "double"),
        ("numerovotos", "int", "numerovotos", "int"),
    ],
    transformation_ctx="Database_node1687018131322",
)

# Script generated for node Filter_studios!=null
SqlQuery0 = """
select * from myDataSource
where estudio is not null;
"""
Filter_studiosnull_node1687019652757 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"myDataSource": Database_node1687018131322},
    transformation_ctx="Filter_studiosnull_node1687019652757",
)

# Script generated for node Change Schema
ChangeSchema_node1687019811823 = ApplyMapping.apply(
    frame=Filter_studiosnull_node1687019652757,
    mappings=[
        ("estudio", "string", "estudio", "string"),
        ("id_tmdb", "string", "id_estudios", "string"),
        ("orcamento", "bigint", "orcamento", "bigint"),
        ("popularidade", "double", "popularidade", "double"),
        ("receita", "bigint", "receita", "bigint"),
        ("id_filmes", "string", "id_filmes", "string"),
        ("titulooriginal", "string", "titulooriginal", "string"),
        ("anolancamento", "int", "anolancamento", "int"),
        ("genero", "string", "genero", "string"),
        ("notamedia", "double", "notamedia", "double"),
        ("numerovotos", "int", "numerovotos", "int"),
    ],
    transformation_ctx="ChangeSchema_node1687019811823",
)

# Script generated for node facts_movies
facts_movies_node1687019882791 = ApplyMapping.apply(
    frame=ChangeSchema_node1687019811823,
    mappings=[
        ("id_estudios", "string", "id_estudios", "string"),
        ("orcamento", "bigint", "orcamento", "bigint"),
        ("popularidade", "double", "popularidade", "double"),
        ("receita", "bigint", "receita", "bigint"),
        ("id_filmes", "string", "id_filmes", "string"),
        ("notamedia", "double", "notamedia", "double"),
        ("numerovotos", "int", "numerovotos", "int"),
    ],
    transformation_ctx="facts_movies_node1687019882791",
)

# Script generated for node dim_studios
dim_studios_node1687019879021 = ApplyMapping.apply(
    frame=ChangeSchema_node1687019811823,
    mappings=[
        ("estudio", "string", "estudio", "string"),
        ("id_estudios", "string", "id_estudios", "string"),
    ],
    transformation_ctx="dim_studios_node1687019879021",
)

# Script generated for node dim_movies
dim_movies_node1687019874274 = ApplyMapping.apply(
    frame=ChangeSchema_node1687019811823,
    mappings=[
        ("id_filmes", "string", "id_filmes", "string"),
        ("titulooriginal", "string", "titulooriginal", "string"),
        ("anolancamento", "int", "anolancamento", "int"),
        ("genero", "string", "genero", "string"),
    ],
    transformation_ctx="dim_movies_node1687019874274",
)

# Script generated for node facts_movies_db
facts_movies_db_node1687020442477 = glueContext.getSink(
    path="s3://data-lake-danilo/Refined/facts_movies/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="facts_movies_db_node1687020442477",
)
facts_movies_db_node1687020442477.setCatalogInfo(
    catalogDatabase="refined_db", catalogTableName="facts_movies"
)
facts_movies_db_node1687020442477.setFormat("glueparquet")
facts_movies_db_node1687020442477.writeFrame(facts_movies_node1687019882791)
# Script generated for node dim_studios_db
dim_studios_db_node1687020547741 = glueContext.getSink(
    path="s3://data-lake-danilo/Refined/dim_studios/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="dim_studios_db_node1687020547741",
)
dim_studios_db_node1687020547741.setCatalogInfo(
    catalogDatabase="refined_db", catalogTableName="dim_studios"
)
dim_studios_db_node1687020547741.setFormat("glueparquet")
dim_studios_db_node1687020547741.writeFrame(dim_studios_node1687019879021)
# Script generated for node dim_movies_db
dim_movies_db_node1687020603097 = glueContext.getSink(
    path="s3://data-lake-danilo/Refined/dim_movies/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="dim_movies_db_node1687020603097",
)
dim_movies_db_node1687020603097.setCatalogInfo(
    catalogDatabase="refined_db", catalogTableName="dim_movies"
)
dim_movies_db_node1687020603097.setFormat("glueparquet")
dim_movies_db_node1687020603097.writeFrame(dim_movies_node1687019874274)
job.commit()

```

## Considerações Finais

O processamento dos dados da camada Trusted para a camada Refined foi concluído com sucesso. Utilizando o Apache Spark e o AWS Glue, os dados foram processados e refinados de acordo com o modelo de dados definido. As tabelas refinadas foram armazenadas na camada Refined no formato PARQUET, em diretórios específicos no bucket S3 "data-lake-danilo". O dados das tabelas foram conferido com o AWS Athena. As tabelas "facts_movies", "dim_studios" e "dim_movies" estão prontas para serem utilizadas na próxima fase do projeto, que envolve a camada de visualização dos dados.

<p align="center"><img src="assets\Print_8.jpg"></p>

<p align="center"><img src="assets\Print_9.jpg"></p>

<p align="center"><img src="assets\Print_10.jpg"></p>

<p align="center"><img src="assets\Print_11.jpg"></p>

<p align="center"><img src="assets\Print_12.jpg"></p>

<p align="center"><img src="assets\Print_13.jpg"></p>

<p align = "center">
Feito por <a href="https://www.linkedin.com/in/danilojosesilva/">Danilo José Silva</a> ! 
</p>