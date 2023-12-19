import json

from dtos.AbilityDTO import AbilityDTO
from dtos.StatDTO import StatDTO


class PokemonDTO:
    def __init__(self, p):
        self.id = p["id"]
        self.name = p["name"].capitalize()
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