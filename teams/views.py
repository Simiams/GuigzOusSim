from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dtos import *
from dtos.PokemonDTO import PokemonDTO
from dtos.TeamDTO import TeamDTO
from .api import get_pokemon_by_id
from .models import PokemonTeam, Pokemon
from .serializers import PokemonSerializer


# Create your views here.


def get_all_teams(request):
    teams = PokemonTeam.objects.all()
    serializer = PokemonSerializer(teams, many=True)
    return Response(serializer.data)


def see_homepage(request):
    pokemon_teams = PokemonTeam.objects.all()

    pokemons_by_team = [
        {"team": convert_team_bdd_in_team_dto(t), "pokemons": convert_pokemon_bdd_in_pokemon_dto(t.members.all())} for t
        in
        pokemon_teams]
    return render(request, 'homepage.html', {"pokemon_teams": pokemons_by_team})


def convert_pokemon_bdd_in_pokemon_dto(pokemons_in_bdd):
    pokemons_in_api = []
    for pokemon_in_bdd in pokemons_in_bdd:
        pokemon_in_api = get_pokemon_by_id(pokemon_in_bdd.poke_api_id)
        pokemon_in_api["id_in_bdd"] = pokemon_in_bdd.id
        pokemons_in_api.append(pokemon_in_api)
    return [PokemonDTO(p) for p in pokemons_in_api]


def convert_team_bdd_in_team_dto(team_in_bdd):
    return TeamDTO(team_in_bdd)


def add_pokemon_to_team(request):
    if request.method == 'POST':
        try:
            pokemon_id = int(request.data.get('pokemon_id'))
            team_id = int(request.data.get('team_id'))
            pokemon, created = Pokemon.objects.get_or_create(poke_api_id=pokemon_id)
            if created:
                pokemon.save()
            team = PokemonTeam.objects.get(id=int(team_id))

            if team.members.count() < 6:
                team.members.add(pokemon)
                team.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Team is already full'}, status=400)

        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid Pokemon ID or Team ID'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_team(request):
    if request.method == 'POST':
        try:
            team_name = request.data.get('team_name')
            team = PokemonTeam(name=team_name)
            team.save()
            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid Team name'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


def delete_pokemon_from_team(id_pokemon):
    entite = get_object_or_404(Pokemon, pk=id_pokemon)
    entite.delete()
    return JsonResponse({'status': 'success'})


@api_view(['POST'])
def management_pokemon(request):
    if request.data.get('management_type') == 'create':
        return add_pokemon_to_team(request)
    elif request.data.get('management_type') == 'delete':
        return delete_pokemon_from_team(int(request.data.get('pokemon_id')))
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid management type'}, status=400)
