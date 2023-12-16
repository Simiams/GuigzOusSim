import os


def get_url_by_catalog_name(catalog_name):
    if catalog_name == "type":
        return os.getenv('GET_TYPE')
    if catalog_name == "pokedex":
        return os.getenv('GET_POKEDEX')
    if catalog_name == "egg-group":
        return os.getenv('GET_EGG_GROUP')
    if catalog_name == "gender":
        return os.getenv('GET_GENDER')
    if catalog_name == "habitat":
        return os.getenv('GET_HABITAT')
    if catalog_name == "growth-rate":
        return os.getenv('GET_GROWTH_RATE')
    else:
        return None
def get_pokemons_urls_by_catalog_name(catalog_name, res):
    if catalog_name == "type":
        return  [r["pokemon"]["url"] for r in res.json()['pokemon']]
    if catalog_name == "pokedex" :
        return [r["pokemon_species"]["url"] for r in res.json()['pokemon_entries']]
    if catalog_name == "egg-group" or catalog_name == "habitat" or catalog_name == "growth-rate":
        return [r["url"] for r in res.json()['pokemon_species']]
    if catalog_name == "gender":
        return [r["pokemon_species"]["url"] for r in res.json()['pokemon_species_details']]
    else:
        return None

def get_pokemon_id_by_url(url):
    return url.split("/")[-2]

POKEMON_TYPE_ICONS = {
    "fire": "img/types/fire.svg",
    "water": "img/types/water.svg",
    "grass": "img/types/grass.svg",
    "electric": "img/types/electric.svg",
    "ice": "img/types/ice.svg",
    "fighting": "img/types/fighting.svg",
    "poison": "img/types/poison.svg",
    "ground": "img/types/ground.svg",
    "flying": "img/types/flying.svg",
    "psychic": "img/types/psychic.svg",
    "bug": "img/types/bug.svg",
    "rock": "img/types/rock.svg",
    "ghost": "img/types/ghost.svg",
    "dark": "img/types/dark.svg",
    "dragon": "img/types/dragon.svg",
    "steel": "img/types/steel.svg",
    "fairy": "img/types/fairy.svg",
    "normal": "img/types/normal.svg",
    "unknown": "",
    "shadow": ""
}
