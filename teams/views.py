from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import get_pokemon_by_id
from .models import Pokemon, PokemonTeam
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

    pokemons_by_team = [{"team": t, "pokemons": get_pokemon_by_id(t.members.all())} for t in pokemon_teams]
    pokemons_by_team_api = [ for p in pokemons_by_team]
    return render(request, 'homepage.html', {"pokemon_teams": "pokemons_by_team"})
