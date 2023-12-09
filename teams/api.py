import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_pokemon_by_id(id):
    res = requests.get(os.getenv('GET_POKEMON') + f'{id}')
    return res.json()
