import os


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
                c.theme = THEME_BY_CATALOG[key].get(c.name, None)
                if c.theme:
                    new_catalog.append(c)
    return new_catalog


def create_catalog(catalog_type, catalog_name, pokemons):
    catalog = CatalogDTO(catalog_type, catalog_name, pokemons, theme=THEME_BY_CATALOG[catalog_type][catalog_name])
    return catalog
