import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_pokemon_by_id(id):
    if id is None or id == -1:
        return []
    try :
        res = requests.get(os.getenv('GET_POKEMON') + f'{id}')
        return res.json()
    except requests.exceptions.JSONDecodeError as e:
        print("[ERROR]" + e)
        return []