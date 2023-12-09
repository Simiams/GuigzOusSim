import os

import requests

def get_all_pokedexes():
    res = requests.get(os.getenv("GETPOKEDEX"))
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]
