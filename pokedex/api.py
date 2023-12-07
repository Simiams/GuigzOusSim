import requests

def get_all_pokedexes():
    res = requests.get('https://pokeapi.co/api/v2/pokedex')
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]
