from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import get_pokemon_by_id
from dto.dtos import PokemonDTO
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

    pokemons_by_team = [{"team": t, "pokemons": convert_pokemon_bdd_in_pokemon_dto(t.members.all())} for t in
                        pokemon_teams]
    print(pokemons_by_team)
    return render(request, 'homepage.html', {"pokemon_teams": pokemons_by_team})


def convert_pokemon_bdd_in_pokemon_dto(pokemons_in_bdd):
    pokemons_in_api = []
    for pokemon_in_bdd in pokemons_in_bdd:
        pokemon_in_api = get_pokemon_by_id(pokemon_in_bdd.poke_api_id)
        pokemons_in_api.append(pokemon_in_api)
    return [PokemonDTO(p) for p in pokemons_in_api]


