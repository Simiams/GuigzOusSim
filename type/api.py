import requests

def get_all_types():
    res = requests.get('https://pokeapi.co/api/v2/type')
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]
