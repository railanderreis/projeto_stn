import pandas as pd
import requests
from backoff import on_exception, constant
from ratelimit import limits, RateLimitException
import logging


logging.getLogger().setLevel(logging.INFO)

@on_exception(constant, RateLimitException, interval=60, max_tries=3)
@limits(calls=20, period=60)
@on_exception(constant,
              requests.exceptions.HTTPError,
              max_tries=3,
              interval=10)
def consulta_bc(cod):
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{cod}/dados?formato=json'
    consult = pd.read_json(url)
    consult['data'] = pd.to_datetime(consult['data'], dayfirst=True)

    logging.info(f'Getting data from API with: {consult}')

    response = requests.get(consult)
    response.raise_for_status()

    return response.json()









