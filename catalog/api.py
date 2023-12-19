import asyncio
import os

import httpx
import requests
from dotenv import load_dotenv

from catalog.utils import get_pokemons_urls_by_catalog_name, get_pokemon_id_by_url
from dtos.CatalogDTO import CatalogDTO
from dtos.PokemonDTO import PokemonDTO

load_dotenv()

cache = []


def get_all_catalog(catalog_url):
    print("[INFO][GetAllCatalog] " + catalog_url)
    res = requests.get(catalog_url)
    return [CatalogDTO(catalog_url.split("/")[-2], r["name"]) for r in res.json()['results']]


async def get_pokemons_by_catalog_name(catalog_type, catalog_url, catalog_name, max):
    print("[INFO][GetPokemonsByCatalogName] " + catalog_url + f'{catalog_name}')
    res = requests.get(catalog_url + f'{catalog_name}')
    pokemon_urls = get_pokemons_urls_by_catalog_name(catalog_type, res)
    pokemon_urls_not_in_cache = []
    pokemons_in_cache = []
    for url in pokemon_urls[0:int(max)]:
        pokemon_in_cache = get_pokemon_in_cache(catalog_type, catalog_name, get_pokemon_id_by_url(url))
        if pokemon_in_cache is None:
            pokemon_urls_not_in_cache.append(url)
        else:
            pokemons_in_cache.append(pokemon_in_cache)
    pokemons = await get_pokemons_by_urls(catalog_type, catalog_name, pokemon_urls_not_in_cache, pokemons_in_cache)

    return pokemons


async def get_pokemons_by_urls(catalog_name, id, pokemon_urls, pokemons):
    async_tasks = []
    for url in pokemon_urls:
        async_tasks.append(get_pokemon_by_url(url.replace("pokemon-species", "pokemon")))
    pokemon_responses = await asyncio.gather(*async_tasks)
    for response in pokemon_responses:
        add_pokemon_to_cache(catalog_name, id, response)
        pokemons.append(PokemonDTO(response))
    return pokemons


async def get_pokemon_by_url(url):
    async with httpx.AsyncClient() as client:
        print("[INFO][GetPokemonByUrl] " + url)
        res = await client.get(url)
        return res.json()


def add_pokemon_to_cache(catalog_name, id, pokemon):
    pokemon = PokemonDTO(pokemon)
    current_catalog = next((cat for cat in cache if cat.name == catalog_name and cat.id == id), None)
    if current_catalog:
        current_catalog.pokemons.append(pokemon)
    else:
        cache.append(CatalogDTO(catalog_name, id, [pokemon]))


def get_pokemon_in_cache(catalog_type, catalog_name, pokemon_id):
    for cat in cache:
        if cat.catalog_type == catalog_type and cat.name == catalog_name:
            for p in cat.pokemons:
                if int(p.id) == int(pokemon_id):
                    return p


def get_all_pokemons():
    print("[INFO][GetAllPokemons] " + os.getenv("GET_ALL_POKEMONS"))
    res = requests.get(os.getenv("GET_ALL_POKEMONS"))
    return res.json()['results'] if res.status_code == 200 else []


async def get_pokemon_by_names(names):
    pokemons = []
    async_tasks = []
    for name in names:
        async_tasks.append(get_pokemon_by_name(name))
    pokemon_responses = await asyncio.gather(*async_tasks)
    for response in pokemon_responses:
        pokemons.append(PokemonDTO(response))
    return pokemons


async def get_pokemon_by_name(name):
    url = os.getenv("GET_POKEMON") + name.lower()
    async with httpx.AsyncClient() as client:
        print("[INFO][GetPokemonByName] " + url)
        res = await client.get(url)
        return res.json()
