import json


class PokemonDTO:
    def __init__(self, p):
        self.id = p["id"]
        self.name = p["name"]
        self.sprite_front = p["sprites"]["front_default"]
        self.sprite_back = p["sprites"]["back_default"]
        self.type = p["types"]
        self.weight = p["weight"]
        self.height = p["height"]
        self.stats = [StatDTO(s) for s in p['stats']]
        self.abilities = [AbilityDTO(a) for a in p['abilities']]

    def __str__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "sprite_front": self.sprite_front,
            "sprite_back": self.sprite_back,
            "type": self.type,
            "weight": self.weight,
            "height": self.height,
            "stats": [s.to_json() for s in self.stats],
            "abilities": [a.to_json() for a in self.abilities]
        })


class StatDTO:
    def __init__(self, s):
        self.effort = s["effort"]
        self.base_stat = s["base_stat"]
        self.name = s["stat"]["name"]
        self.url = s["stat"]["url"]

    def to_json(self):
        return {
            "effort": self.effort,
            "base_stat": self.base_stat,
            "name": self.name,
            "url": self.url
        }


class AbilityDTO:
    def __init__(self, a):
        self.name = a["ability"]["name"]
        self.url = a["ability"]["url"]

    def to_json(self):
        return {
            "name": self.name,
            "url": self.url
        }
