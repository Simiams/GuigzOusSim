import asyncio
import os

import httpx
import requests
from dotenv import load_dotenv

load_dotenv()


class Catalog:
    def __init__(self, name, id, pokemons):
        self.name = name
        self.id = id
        self.pokemons = pokemons
        self.last_index_pokemon = len(pokemons)


cache = []


def get_all_catalog(catalog_url):
    res = requests.get(catalog_url)
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]


async def get_pokemons_by_catalog_id(catalog_name, catalog_url, id, start):
    start, end = int(start), int(start) + int(os.getenv("DEFAULT_LIMIT"))
    async with (httpx.AsyncClient() as client):
        res = await client.get(catalog_url + f'{id}')
        pokemon_urls = [r["pokemon"]["url"] for r in res.json()['pokemon']]
        tasks = []
        for url in pokemon_urls[start:end]:
            pokemon_in_cache = await get_pokemon_in_cache(catalog_name, id, get_pokemon_id_by_url(url))
            print(url)
            if not pokemon_in_cache:
                print("not in cache")
                pokemon_from_api = await get_pokemon_by_url(url)
                print(type(pokemon_from_api))
                tasks.append(pokemon_from_api)
                add_pokemon_to_cache(catalog_name, id, pokemon_from_api)
            else:
                print("in cache")
                tasks.append(pokemon_in_cache)
    print(type(tasks))
    return await asyncio.gather(*tasks)


async def get_pokemon_by_url(url):
    print("get pokemon by url")
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        return res.json()


def return_and_add_to_cache(catalog_name, id, pokemons):
    current_catalog = next((cat for cat in cache if cat.name == catalog_name and cat.id == id), None)
    if current_catalog:
        current_catalog.pokemons.extend(pokemons)
        current_catalog.last_index_pokemon = len(current_catalog.pokemons)
        print(current_catalog.last_index_pokemon)
        return current_catalog
    else:
        new_catalog = Catalog(catalog_name, id, pokemons)
        cache.append(new_catalog)
        return new_catalog


def add_pokemon_to_cache(catalog_name, id, pokemon):
    print("add to cache")
    current_catalog = next((cat for cat in cache if cat.name == catalog_name and cat.id == id), None)
    if current_catalog:
        current_catalog.pokemons.append(pokemon)
    else:
        cache.append(Catalog(catalog_name, id, [pokemon]))
    print("added to cache")


# def is_in_cache(catalog_name, id, pokemon_id):
#     return True if any(cat.name == catalog_name and cat.id == id and pokemon_id in [p['id'] for p in cat.pokemons] for cat in cache) else False


def get_pokemon_in_cache(catalog_name, id, pokemon_id):
    print("get pokemon in cache")
    # loop = asyncio.get_event_loop()
    # return await loop.run_in_executor(None, get_pokemon_in_cache, catalog_name, id, pokemon_id)

    return next((cat for cat in cache if cat.name == catalog_name and cat.id == id and pokemon_id in [p['id'] for p in cat.pokemons]), None)


def get_pokemons_bu_range_in_cache(catalog_name, id, start, end):
    return next((cat for cat in cache if cat.name == catalog_name and cat.id == id), None).pokemons[start:end]


def get_pokemon_id_by_url(url):
    return url.split("/")[-2]

## todo convert to PokemonDTO
