from api_bacen import consulta_bc
from s3_upload import upload_to_s3
import yaml
import sys
from datetime import datetime

def extract_and_upload(date):
    year = date.strftime('%Y')
    month = date.strftime('%m')
    day = date.strftime('%d')
    for series in config['series']:
        json_data = consulta_bc(series)
        upload_to_s3(
            bucket=config['bucket'],
            schema='bacen',
            table=series,
            partition=date.strftime('%Y-%m-%d'),
            json_data=json_data
        )


if __name__ == '__main__':
    with open('config.yml') as f:
        config = yaml.safe_load(f)
