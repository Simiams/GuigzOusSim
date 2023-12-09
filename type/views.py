from django.shortcuts import render

from dto.dtos import PokemonDTO
from type.api import get_all_types, get_pokemons_by_type_id, get_last_pokemon_index, save_pokemon_in_cache


# Create your views here.
def see_all_types(request):
    types = get_all_types()
    return render(request, 'types/pages/index.html', {"types": types})


async def see_all_pokemons_by_type(request, id):
    pokemons = [PokemonDTO(p) for p in await get_pokemons_by_type_id(id, request.GET.get('start', 0))]
    display_button = (True, False)[len(pokemons) < 25]
    pokemons = save_pokemon_in_cache(id, pokemons)
    las_pokemon_index = get_last_pokemon_index(id)
    return render(request, 'types/pages/type.html', {"pokemons": pokemons,
                                                     "page_info": {"display_button": display_button, "id": id,
                                                                   "last_pokemon_index": las_pokemon_index}})
