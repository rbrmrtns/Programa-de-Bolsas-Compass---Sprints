# %%

import logging
import boto3
from botocore.exceptions import ClientError
from datetime import datetime


def criar_bucket(nomeBucket):
    try:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=nomeBucket)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def carregar_arquivo(dadosObjeto, nomeBucket, keyArquivo):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.put_object(Body=dadosObjeto, Bucket=nomeBucket, Key=keyArquivo)
    except ClientError as e:
        logging.error(e)
        return False
    return True


bucket = "dl-filmes-series-rodrigo-martins"

timestampProcessamento = datetime.now()
anoProcessamento = timestampProcessamento.year
mesProcessamento = timestampProcessamento.month
if len(str(mesProcessamento)) <= 1:
    mesProcessamento = '0' + str(mesProcessamento)
diaProcessamento = timestampProcessamento.day
if len(str(diaProcessamento)) <= 1:
    diaProcessamento = '0' + str(diaProcessamento)

keyArquivo1 = f'RAW/Local/CSV/Movies/{anoProcessamento}/{mesProcessamento}/{diaProcessamento}/movies.csv'
keyArquivo2 = f'RAW/Local/CSV/Series/{anoProcessamento}/{mesProcessamento}/{diaProcessamento}/series.csv'

if __name__ == '__main__':
    criar_bucket(nomeBucket=bucket)
    
    with open('/csvs/movies.csv', encoding='utf8') as a:
        dados = a.read()
        carregar_arquivo(dadosObjeto=dados, nomeBucket=bucket, keyArquivo=keyArquivo1)
        
    with open('/csvs/series.csv', encoding='utf8') as a:
        dados = a.read()
        carregar_arquivo(dadosObjeto=dados, nomeBucket=bucket, keyArquivo=keyArquivo2)
        
# %%
