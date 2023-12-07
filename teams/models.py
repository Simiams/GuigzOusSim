from django.db import models


# Create your models here.
class Pokemon(models.Model):
    image = models.CharField(max_length=100)
    poke_api_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class PokemonTeam(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name + " || " + str(self.id)
