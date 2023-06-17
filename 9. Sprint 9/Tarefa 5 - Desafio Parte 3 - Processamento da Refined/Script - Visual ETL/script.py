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
