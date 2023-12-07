from django.shortcuts import render

from pokedex.api import get_all_pokedexes


def see_all_pokedexes(request):
    pokedexes = get_all_pokedexes()
    return render(request, 'pokedex/pages/index.html', {"pokedexes":pokedexes})
def see_pokedex_by_id(request, id):
    return render(request, 'pokedex/pages/pokedex.html')

def see_home_page(request):
    return render(request, 'homePage.html')


