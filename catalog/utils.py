import os
from random import random

from catalog.constant import URL_BY_CATALOG, THEME_BY_CATALOG
from dtos.CatalogDTO import CatalogDTO


def get_url_by_catalog_name(catalog_type):
    return os.getenv(URL_BY_CATALOG.get(catalog_type, None))


def get_pokemons_urls_by_catalog_name(catalog_name, res):
    if catalog_name == "type":
        return [r["pokemon"]["url"] for r in res.json()['pokemon']]
    if catalog_name == "pokedex":
        return [r["pokemon_species"]["url"] for r in res.json()['pokemon_entries']]
    if catalog_name == "egg-group" or catalog_name == "habitat" or catalog_name == "growth-rate":
        return [r["url"] for r in res.json()['pokemon_species']]
    if catalog_name == "gender":
        return [r["pokemon_species"]["url"] for r in res.json()['pokemon_species_details']]
    else:
        return None


def get_pokemon_id_by_url(url):
    return url.split("/")[-2]


def get_theme_by_catalog(catalog, catalog_type):
    new_catalog = []
    for key, value in THEME_BY_CATALOG.items():
        if key == catalog_type:
            for c in catalog:
                if THEME_BY_CATALOG[key].get(c.name, None):
                    c.theme = THEME_BY_CATALOG[key].get(c.name, {}).copy()
                    c.theme["color"] = mitigate_color(THEME_BY_CATALOG[key].get(c.name, {})["color"], 50)
                    new_catalog.append(c)
    return new_catalog


def create_catalog(catalog_type, catalog_name, pokemons):
    return CatalogDTO(catalog_type, catalog_name, pokemons, theme=THEME_BY_CATALOG[catalog_type][catalog_name])


def mitigate_color(code_hex, correction):
    r = int(code_hex[1:3], 16)
    g = int(code_hex[3:5], 16)
    b = int(code_hex[5:7], 16)
    r = max(0, min(255, r + correction))
    g = max(0, min(255, g + correction))
    b = max(0, min(255, b + correction))
    nouveau_code_hex = "#{:02X}{:02X}{:02X}".format(int(r), int(g), int(b))
    return nouveau_code_hex

