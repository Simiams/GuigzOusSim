import os

from asgiref.sync import sync_to_async
from django.shortcuts import render

from catalog.api import get_all_catalog, get_pokemons_by_catalog_id
from catalog.utils import get_url_by_catalog_name
from teams.models import PokemonTeam


# Create your views here.
def see_all_catalog(request, catalog):
    url = get_url_by_catalog_name(catalog)
    if not url: return not_found(request)
    res = get_all_catalog(url)
    return render(request, 'catalog/pages/index.html', {"catalog_name": catalog, "catalog": res})


async def see_all_pokemons_by_catalog(request, catalog, id):
    url = get_url_by_catalog_name(catalog)

    if not url: return not_found(request)
    max = request.GET.get('max', os.getenv("DEFAULT_MAX"))

    pokemons = await get_pokemons_by_catalog_id(catalog, url, id, max)

    teams = [t.id async for t in PokemonTeam.objects.all()]

    display_button = len(pokemons) == int(max)

    return render(request, 'catalog/pages/catalog.html', {"pokemons": pokemons, "teams": teams,
                                                          "page_info": {"display_button": display_button,
                                                                        "catalog_name": catalog, "id": id,
                                                                        "max_pokemon": len(pokemons) + 25}})


def not_found(request):
    return render(request, 'base.html')

## todo make obj DTO
