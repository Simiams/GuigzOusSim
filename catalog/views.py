import os

from django.shortcuts import render

from catalog.api import get_all_catalog, get_pokemons_by_catalog_id, return_and_add_to_cache
from catalog.utils import get_url_by_catalog_name



# Create your views here.
def see_all_catalog(request, catalog):
    url = get_url_by_catalog_name(catalog)
    if not url : return not_found(request)
    res = get_all_catalog(url)
    return render(request, 'catalog/pages/index.html', {"catalog_name": catalog, "catalog": res})

async def see_all_pokemons_by_catalog(request, catalog, id):
    url = get_url_by_catalog_name(catalog)
    if not url : return not_found(request)
    pokemons = await get_pokemons_by_catalog_id(catalog, url, id, request.GET.get('start', 0))
    display_button = True if len(pokemons) < int(os.getenv("DEFAULT_LIMIT")) else False
    return render(request, 'catalog/pages/catalog.html', {"pokemons": pokemons, "page_info": {"display_button": display_button, "catalog_name": catalog, "id": id, "last_pokemon_index" : len(pokemons)}})
def not_found(request):
    return render(request, 'base.html')

