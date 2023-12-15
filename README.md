# SETUP
pip install -r requirements.txt (installe les dépendances necessaires)

# BDD
```
Username: guigsoussim
password: guigsoussim
```
Pour des soucis de simplicité, on stocke en base uniquement le information suivante:



# BACKEND
## catalog

Ce package regroupe les fonctionnalité de recherche par catégorie de pokeon (type, pokedex, type d'oeuf, genre, etc...)

### EndPoints

- https://pokeapi.co/api/v2/pokemon/
- https://pokeapi.co/api/v2/pokedex/
- https://pokeapi.co/api/v2/type/
- https://pokeapi.co/api/v2/egg-group/
- https://pokeapi.co/api/v2/gender/
- https://pokeapi.co/api/v2/pokemon-habitat/
- https://pokeapi.co/api/v2/growth-rate/


Il retourne une liste de pokemon avec leurs nom et url.

Pour chaque urls, on vies récupérer toutes les informations sur le pokemon. Pour des soucis de performance, on execute
ces requêtes en asynchrone avec une gestion de cache, un pokemon déjà appeler est sauvegarder en local et ne sera plus
appeler.

De plus, les pokemons s'affiche par vaque de 25 (DEFAULT_MAX)

## teams

ce package rassemble les fonctionnalité de gestion des équipes de pokemons.

### Actions possible
- Créer une équipe
- Voir ses pokemons par équipe
- Accéder au differents catalogues pour ajouter des pokemons à son équipe
