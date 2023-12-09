import asyncio
import os

import httpx
import requests
from dotenv import load_dotenv

load_dotenv()

cache_pokemon = {}
last_pokeomn_index = {}


def get_all_types():
    res = requests.get(os.getenv('GET_TYPE'))
    return [{"name": r["name"], "id": r["url"].split("/")[-2]} for r in res.json()['results']]


async def get_pokemons_by_type_id(id, start):
    if start == 0: cache_pokemon.clear()
    start = int(start)
    end = start + 25
    last_pokeomn_index[id] = end
    async with (httpx.AsyncClient() as client):
        res = await client.get(os.getenv('GET_TYPE') + f'{id}')
        pokemons = [r["pokemon"]["url"] for r in res.json()['pokemon']]
        tasks = [get_pokemon_by_url(pokemon) for pokemon in pokemons[start:end]]
    return await asyncio.gather(*tasks)


async def get_pokemon_by_url(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        return res.json()


def get_last_pokemon_index(id):
    return last_pokeomn_index[id]

def get_cache_pokemon(id):
    return cache_pokemon[id]


def save_pokemon_in_cache(id, pokemons):
    if id in cache_pokemon:
        cache_pokemon[id].extend(pokemons)
    else:
        cache_pokemon[id] = pokemons
    return cache_pokemon[id]