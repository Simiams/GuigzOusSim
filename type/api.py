import requests

def get_all_types():
    res = requests.get('https://pokeapi.co/api/v2/type')
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]

def get_pokemons_by_type_id(id):
    res = requests.get(f'https://pokeapi.co/api/v2/type/{id}')
    pokemons = [r["pokemon"]["url"] for r in res.json()['pokemon']]
    return [get_pokemon_by_url(pokemon) for pokemon in pokemons]

def get_pokemon_by_url(url):
    res = requests.get(url)
    return res.json()