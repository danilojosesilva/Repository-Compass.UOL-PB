import boto3
import os
from datetime import datetime

# Configurar as credenciais da AWS
aws_access_key_id = 'AKIARQPIBSDDDQYK7SQS'
aws_secret_access_key = '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'
aws_region = 'us-east-1'

# Configurar o nome do bucket S3 e o diretório de origem dos arquivos CSV localmente
bucket_name = 'data-lake-danilo'

#padrão: <nome do bucket><camada de armazenamento><origem do dado><formato do dado><especificação do dado><data de processamento separada por ano\mes\dia><arquivo>

# Criar uma instância do cliente S3
s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=aws_region)

# Obter a data atual para a nomenclatura do diretório
current_date = datetime.now().strftime('%Y/%m/%d')

# Diretórios e arquivos a serem carregados no S3
data_to_upload = [
    {
        'local_path': os.path.join('movies.csv'),
        's3_key': f'Raw/Local/CSV/Movies/{current_date}/movies.csv'
    },
    {
        'local_path': os.path.join('series.csv'),
        's3_key': f'Raw/Local/CSV/Series/{current_date}/series.csv'
    }
]

# Percorrer os arquivos e fazer upload para o S3
for data in data_to_upload:
    local_path = data['local_path']
    s3_key = data['s3_key']

    # Fazer upload do arquivo para o S3
    s3_client.upload_file(local_path, bucket_name, s3_key)

    print(f'Arquivo {local_path} enviado para o bucket {bucket_name} com sucesso! Caminho no S3: {s3_key}')