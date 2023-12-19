import json

from dtos.AbilityDTO import AbilityDTO
from dtos.StatDTO import StatDTO


class PokemonDTO:
    def __init__(self, p):
        self.id = p["id"]
        self.name = p["name"]
        self.sprite_front = p["sprites"]["front_default"]
        self.sprite_back = p["sprites"]["back_default"]
        self.type = p["types"][0]
        self.weight = p["weight"]
        self.height = p["height"]
        self.stats = [StatDTO(s) for s in p['stats']]
        self.abilities = [AbilityDTO(a) for a in p['abilities']]
        self.id_in_bdd = p["id_in_bdd"] if "id_in_bdd" in p else None

    def __str__(self):
        return json.dumps({
            "id": self.id,
            "id_in_bdd": self.id_in_bdd,
            "name": self.name,
            "sprite_front": self.sprite_front,
            "sprite_back": self.sprite_back,
            "type": self.type,
            "weight": self.weight,
            "height": self.height,
            "stats": [s.to_json() for s in self.stats],
            "abilities": [a.to_json() for a in self.abilities],
        })



{"id": 6, "id_in_bdd": 39, "name": "charizard",
 "sprite_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
 "sprite_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/6.png",
 "type": {"slot": 1, "type": {"name": "fire", "url": "https://pokeapi.co/api/v2/type/10/"}}, "weight": 905,
 "height": 17, "stats": [{"effort": 0, "base_stat": 78, "name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"},
                         {"effort": 0, "base_stat": 84, "name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"},
                         {"effort": 0, "base_stat": 78, "name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"},
                         {"effort": 3, "base_stat": 109, "name": "special-attack",
                          "url": "https://pokeapi.co/api/v2/stat/4/"},
                         {"effort": 0, "base_stat": 85, "name": "special-defense",
                          "url": "https://pokeapi.co/api/v2/stat/5/"},
                         {"effort": 0, "base_stat": 100, "name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}],
 "abilities": [{"name": "blaze", "url": "https://pokeapi.co/api/v2/ability/66/"},
               {"name": "solar-power", "url": "https://pokeapi.co/api/v2/ability/94/"}]}
