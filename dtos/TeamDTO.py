import json

class TeamDTO:
    def __init__(self, t):
        self.id = t.id
        self.name = t.name

    def __str__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
        })

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
        })