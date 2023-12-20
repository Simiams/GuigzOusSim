# SETUP

### VENV

- python3 -m venv venv (créer un environnement virtuel)
- source venv/bin/activate (active l'environnement virtuel)

### REQUIREMENTS

- pip freeze > requirements.txt (créer un fichier requirements.txt)
- pip install -r requirements.txt (installe les dépendances necessaires)

# FONCTIONALITÉS

## Catalogue

Le catalogue permet de cherche tout les pokemons appartenant a un même ctalogues. On peux accéder au different catalog
depuis la homepage via les bouttons sur le panel de droite qui liste les type de catalogues (pokedex, type d'oeuf,
genre, type, etc...).En selectionnant un type de catalogue, on accède à une page listant tout les catalogues appartenant
à ce type (feu, eau, etc...). C'est en cliquant sur un cataloguespeifique qu'on peux voir apparaitre la liste des
pokemons (tout les pokemon de type feu, tout les pokemon du pokedex kanto, etc...).

Les pokemons sont afficher par tranche de 25 pour eviter de surcharger la page. En cliquant sut le boutton "voir plus",
25 de plus se rajoutent. Le deuxieme acces à a page est plus rapidegrace au cache.

Cliquer sur un pokemon affiche sa carte, on peut alors choisir de l'ajouter a une équipeau préalable créer via la home
page. On y reviendra...

## Equipes

La page déquipe ou la homepage permet de creer er supprimer une équipe, de voir lespokemon appartenant a une equipe et
de les supprimer.

La homepage permet l'accés au differetn catalogue mais aussi a la focntionnalité de recherche par nom. Un traducteur
francais y est integrés, vous pouvez donc entrer des nom de pokemon francais, une approximation est faite, vousverrez
par ordre de pertinence les pokemons dont le nom correspond plus ou moins à votre requete.

---

# TECHNIQUE

# BDD

La bdd sert uniquement pour le stockage des pokemons et des équipes.
Pour des soucis de simplicsité, on stocke en base uniquement le information suivante:

### Pokemon

- id
- id (coté PokeApi)

### Teams

- id
- name

### PokemonTeams

- id
- pokemon_id
- team_id

La table pokemon n'es pas nécessaire pour l'actuelle fonctioonnement de l'application mais par anticipation d'une
fonctionnalité de duel et de gestion des hp nous avons creer une table dédiée.

---

## BACKEND

le Back est syndé en 2 package principale:

- catalog
- teams
  Le catalog gére l'affichage des pokemons par catalogue ainsi que celui des type de cataolg
  Le package teams gére la gestion des équipes de pokemons et notre homepage

### POKEAPI

Pour utilisé un maximum l'apipokeapi, on ne stocke aucun pokemon en base de donnée, on les récupère directement via les
endponts disponnible, une amélioration future serarais 

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

# Ameliorations futures

- Ajouter une fonctionnalité de duel
    - Stocker en base les PV des pokemons
    - Calcule des dégats en fonction des types et des attaques
    - Systeme de level, chaque combat gagné incrementer le level du pokemon ainsi que ses stats
    - Un pokemon mort est supprimer de l'équipe, il faut donc le rajouter ce qui reset ces stats


- Ajouter une gestion des utilisateur
    - Nouvelle table en base + liaison des équipes à un utilisateur
    - Ajouter une fonctionnalité de login


- Ajouter un script de remplissage automatique de la base de donnée pour gagner en performance sur les recherche