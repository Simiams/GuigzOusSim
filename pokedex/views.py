from django.shortcuts import render

def see_all_pokedexes(request):
    return render(request, 'pokedex/see_all_pokedexes.html')
