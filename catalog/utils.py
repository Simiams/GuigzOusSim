import os

from catalog.constant import URL_BY_CATALOG, THEME_BY_CATALOG


def get_url_by_catalog_name(catalog_name):
    return os.getenv(URL_BY_CATALOG.get(catalog_name, None))


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

def get_theme_by_catalog(catalog, catalog_name):
    print("get_theme_by_catalog")
    for key, value in THEME_BY_CATALOG.items():
        print(key + " " + catalog_name)
        if key == catalog_name:
            for c in catalog:
                c["theme"] = THEME_BY_CATALOG[key].get(c["name"], None)
            return catalog
