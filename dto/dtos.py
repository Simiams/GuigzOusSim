class PokemonDTO:
    # def __init__(self, name, sprite_front, sprite_back, type, weight, height, stats, abilities):
    #     self.name = name
    #     self.sprite_front = sprite_front
    #     self.sprite_back = sprite_back
    #     self.type = type
    #     self.weight = weight
    #     self.height = height
    #     self.stats = stats
    #     self.abilities = abilities

    def __str__(self):
        return f"{self.name} - {self.type} - {self.weight} - {self.height} - {self.stats} - {self.abilities}"

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


class StatDTO:
    # def __init__(self, effort, base_stat, name, url):
    #     self.effort = effort
    #     self.base_stat = base_stat
    #     self.name = name
    #     self.url = url

    def __str__(self):
        return f"{self.name} - {self.effort} - {self.base_stat}"

    def __init__(self, s):
        self.effort = s["effort"]
        self.base_stat = s["base_stat"]
        self.name = s["stat"]["name"]
        self.url = s["stat"]["url"]


class AbilityDTO:
    # def __init__(self, name, url):
    #     self.name = name
    #     self.url = url

    def __str__(self):
        return f"{self.name}"

    def __init__(self, a):
        self.name = a["ability"]["name"]
        self.url = a["ability"]["url"]
