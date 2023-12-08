from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import get_pokemon_by_id
from .models import PokemonTeam
from .serializers import PokemonSerializer


# Create your views here.


@api_view(['POST'])
def create_pokemon(request):
    if request.method == 'POST':
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def see_homepage(request):
    pokemon_teams = PokemonTeam.objects.all()
    for t in pokemon_teams:
        for p in t.members.all():
            print(p.id)

    pokemons_by_team = [{"team": t, "pokemons": convert_pokemon_in_bdd_in_pokemon_in_api(t.members.all())} for t in
                        pokemon_teams]

    return render(request, 'homepage.html', {"pokemon_teams": "pokemons_by_team"})


def convert_pokemon_in_bdd_in_pokemon_in_api(pokemon_in_bdd):
    pokemon_in_api = get_pokemon_by_id(pokemon_in_bdd.id)
    pokemon_in_api["team"] = pokemon_in_bdd.team
    return pokemon_in_api
