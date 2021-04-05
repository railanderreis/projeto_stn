import pandas as pd
import zipfile36
import urllib.request
import boto3

s3 = boto3.client('s3')

url = 'http://dadosabertos.pgfn.gov.br/Dados_abertos_Nao_Previdenciario.zip'

urllib.request.urlretrieve(url, 'ativos.zip')

with zipfile36.ZipFile('ativos.zip', 'r') as zipped:
    zipped.extractall('/scripts/arq/')
