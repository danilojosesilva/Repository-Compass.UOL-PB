# AWS Lambda Function - Ingestão de Filmes de Terror do TMDB para o Amazon S3

Este repositório contém o código Python de uma função AWS Lambda. Essa função realiza a ingestão de dados de filmes de terror do TMDB (The Movie Database) e armazena os resultados em arquivos JSON no Amazon S3. O código é projetado para processar os filmes em lotes de 100. Ainda, o repositório conta com o projeto de ingestão de dados testado localmente como pode ser observado na pasta "Local Code".

![imagem](assets\Print_1.jpg) 

## Funcionalidades

A função realiza as seguintes ações:

1. **Leitura do CSV:** Lê um arquivo CSV chamado `movies.csv` armazenado no Amazon S3. O caminho do arquivo é `s3://data-lake-danilo/Raw/Local/CSV/Movies/2023/05/19/movies.csv`.

![imagem](assets\Print_2.jpg)

2. **Filtro de Filmes de Terror:** Filtra os filmes de terror do CSV e remove os IDs duplicados. Consideramos que a coluna do gênero é chamada "genero" e os filmes de terror são identificados como "horror".

3. **Criação de Lotes:** Divide o DataFrame filtrado em lotes de 100 filmes para processamento em lote.

4. **Requisição à API do TMDB:** Para cada lote, faz uma requisição à API do TMDB usando a chave de API fornecida. A requisição busca dados de popularidade e receita para cada filme, baseando-se no ID do filme.

5. **Criação do Dicionário de Dados:** Filtra os dados retornados da API do TMDB, criando um novo dicionário com as informações de ID, popularidade e receita.

6. **Conversão para JSON:** Converte os dados filtrados em formato JSON.

![imagem](assets\Print_3.jpg)

7. **Armazenamento no S3:** Salva os dados em arquivos JSON separados no Amazon S3. Os arquivos são armazenados no seguinte caminho: `s3://data-lake-danilo/Raw/TMDB/JSON/Movies/2023/05/19/`. O formato de nomeação dos arquivos é `movies_tmdb_000.json`, `movies_tmdb_001.json`, etc.

![imagem](assets\Print_5.jpg)

## Criação do Pacote de Dependências

O código desta função Lambda requer a biblioteca pandas, que não está incluída na runtime padrão do Lambda. Portanto, precisaremos criar um pacote de dependências com esta biblioteca e enviá-lo ao Lambda. Siga estas etapas para criar o pacote:

1. **Criação do Ambiente Virtual:** Primeiro, precisaremos criar um ambiente virtual Python para instalar a biblioteca pandas. Se você não tiver o virtualenv instalado, você pode instalá-lo com o seguinte comando:
   
        pip install virtualenv

Em seguida, crie um novo ambiente virtual Python 3.7 e ative-o com estes comandos:

       virtualenv -p python3.7 venv
       source venv/bin/activate


2. **Instalação da Biblioteca Pandas:** Com o ambiente virtual ativado, instale a biblioteca pandas com o seguinte comando:

        pip install pandas


3. **Criação do Pacote de Dependências:** Agora, precisamos criar um pacote de dependências com a biblioteca pandas. No diretório raiz do ambiente virtual, você encontrará uma pasta chamada "lib". Dentro dela, haverá outra pasta chamada "python3.7" (ou similar, dependendo da versão do Python que você usou). Dentro desta pasta, você encontrará uma pasta chamada "site-packages", que contém todas as bibliotecas instaladas no ambiente virtual.

Navegue até a pasta "site-packages" e crie um arquivo ZIP com todas as bibliotecas nela contidas. Você pode fazer isso com o seguinte comando:

       cd venv/lib/python3.7/site-packages
       zip -r9 ${OLDPWD}/minha-camada-pandas.zip .


Agora você tem um pacote ZIP chamado `minha-camada-pandas.zip` que contém a biblioteca pandas e todas as suas dependências. Você pode fazer o upload deste pacote para a AWS Lambda para criar uma camada de dependências.

OBS.: Os comandos de instalação foram feitos levando em consideração o ambiente linux. Para outros ambientes pode ocorrer alterações.

## Configuração do Ambiente

Antes de implementar a função Lambda, será necessário realizar as seguintes configurações:

1. **Criação do Bucket:** Crie um bucket no Amazon S3. Obs.: Mudar o nome na função Lambda de acordo com o bucket criado.

2. **Upload do CSV:** Faça upload do arquivo CSV `movies.csv` para o diretório no bucket do S3.

3. **Chave de API do TMDB:** Crie uma chave de API no TMDB e substitua pela sua chave de API nas variáveis de ambiente `API_KEY` da função Lambda.

![imagem](assets\Print_6.jpg)

4. **Criação da Função Lambda:** Crie uma função Lambda no AWS Management Console com as seguintes configurações:
   - Nome da função: `tmdb-movies-ingestion`
   - Runtime: Python 3.7
   - Timeout: Recomendado 10 minutos ou ajuste de acordo com suas necessidades.

![imagem](assets\Print_7.jpg)

![imagem](assets\Print_8.jpg)

5. **Criação da Camada Lambda (Layer):** Crie uma camada Lambda para incluir as dependências do Python:
   - Nome da camada: `pandas_requests`
   - Runtime compatível: Python 3.7
   - Faça upload do arquivo ZIP `minha-camada-pandas.zip` para a camada. Certifique-se de que o arquivo ZIP contém as bibliotecas `pandas` e `requests` no diretório `python`.

![imagem](assets\Print_9.jpg)

6. **Associação da Camada à Função Lambda:** Associe a camada `pandas_requests` à função Lambda `lambda_tmdb_ingest`.

7. **Permissões da Função Lambda:** Configure as permissões da função Lambda para acessar o bucket S3. A função precisa de permissões para ler o arquivo CSV e gravar os arquivos JSON no bucket.

8. **Código da Função Lambda:** Insira o código Python do arquivo `lambda_function.py` no editor de código da função Lambda e salve as alterações.

9. **Implantação da Função Lambda:** Salve e implante a função Lambda.

![imagem](assets\Print_4.jpg)

## Utilização

Após a configuração, você pode testar a função manualmente ou configurar um gatilho para executá-la automaticamente em intervalos regulares.

Ao ser executada, a função Lambda processará os filmes de terror contidos no arquivo `movies.csv`, buscará informações adicionais do TMDB para cada filme, filtrará as informações necessárias e armazenará os dados em arquivos JSON separados no bucket S3.

Você pode monitorar os logs da função Lambda para acompanhar o progresso e os resultados. Certifique-se de que as permissões adequadas estejam configuradas para permitir a gravação de logs.

## Considerações Finais

Este código de função Lambda permite a ingestão de dados de filmes de terror do TMDB para o Amazon S3, filtrando as informações relevantes e organizando-as em arquivos JSON separados. Este código pode ser adaptado e expandido para atender às necessidades específicas do seu projeto.

Certifique-se de substituir as informações relevantes, como a chave de API do TMDB, o nome do bucket S3 e o caminho do arquivo CSV, de acordo com a sua configuração.

Este README oferece uma visão geral do processo e dos passos necessários para configurar e usar a função Lambda. Revise e adapte essas instruções com base em suas próprias necessidades e no ambiente em que você está trabalhando.

Boa sorte e boa ingestão de dados!

<p align = "center">
Feito por Danilo José Silva! Entre em <a href="https://www.linkedin.com/in/danilojosesilva/">contato</a> !
</p>