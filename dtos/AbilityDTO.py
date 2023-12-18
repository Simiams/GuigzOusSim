class AbilityDTO:
    def __init__(self, a):
        self.name = a["ability"]["name"]
        self.url = a["ability"]["url"]

    def to_json(self):
        return {
            "name": self.name,
            "url": self.url
        }