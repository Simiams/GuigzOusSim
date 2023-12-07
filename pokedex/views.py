from django.shortcuts import render


def see_all_pokedexes(request):
    return render(request, 'pokedex/pages/index.html')
def see_pokedex_by_id(request, id):
    return render(request, 'pokedex/pages/pokedex.html')
