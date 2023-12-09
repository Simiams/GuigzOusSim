import os


def get_url_by_catalog_name(catalog_name):
    if catalog_name == "type":
        return os.getenv('GET_TYPE')
    if catalog_name == "pokedex":
        return os.getenv('GET_POKEDEX')
    else:
        return None