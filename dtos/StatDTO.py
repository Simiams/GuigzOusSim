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