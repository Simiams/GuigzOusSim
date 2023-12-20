import os

from django.shortcuts import render
from fuzzywuzzy import process
from unidecode import unidecode

from catalog.api import get_all_catalog, get_pokemons_by_catalog_name, get_all_pokemons, get_pokemon_by_names, \
    get_translation
from catalog.utils import get_url_by_catalog_name, get_theme_by_catalog, create_catalog
from dtos.CatalogDTO import CatalogDTO
from teams.models import PokemonTeam
from teams.views import convert_team_bdd_in_team_dto


# Create your views here.
def see_all_catalog(request, catalog_type):
    url = get_url_by_catalog_name(catalog_type)
    if not url: return not_found(request)
    res = get_all_catalog(url)
    catalogs = get_theme_by_catalog(res, catalog_type)
    for c in catalogs:
        print(c)
    return render(request, 'catalog/pages/catalogsTypes.html', {"catalog": catalogs})


async def see_all_pokemons_by_catalog(request, catalog_name, catalog_type):
    url = get_url_by_catalog_name(catalog_type)
    if not url: return not_found(request)
    max = request.GET.get('max', os.getenv("DEFAULT_MAX"))
    pokemons = await get_pokemons_by_catalog_name(catalog_type, url, catalog_name, max)
    teams = [convert_team_bdd_in_team_dto(t).to_json() async for t in PokemonTeam.objects.all()]
    display_button = len(pokemons) == int(max)
    catalog = create_catalog(catalog_type, catalog_name, pokemons)
    return render(request, 'catalog/pages/pokemonsByCatalogs.html', {"teams": teams,
                                                                     "catalog": catalog,
                                                                     "page_info": {"display_button": display_button,
                                                                                   "max_pokemon": len(pokemons) + 25}})


async def search_pokemon(request):
    query = unidecode(request.GET.get('q'))
    translated = get_translation(query)
    all_pokemons = get_all_pokemons()
    teams = [convert_team_bdd_in_team_dto(t).to_json() async for t in PokemonTeam.objects.all()]
    pokemon_to_find = translated if translated != query else query
    pokemons = process.extract(pokemon_to_find, [p["name"] for p in all_pokemons], limit=20)
    catalog = CatalogDTO("search", "search", pokemons=await get_pokemon_by_names([p[0] for p in pokemons]))
    return render(request, 'catalog/pages/pokemonsByCatalogs.html', {"teams": teams, "catalog": catalog,
                                                                 "page_info": {"display_search_form": True}})


def not_found(request):
    return render(request, 'base.html')
