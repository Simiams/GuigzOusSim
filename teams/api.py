import requests

def get_pokemon_by_id(id):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
    return res.json()