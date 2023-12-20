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
endponts disponnible, une amélioration future serarais de réalisé un script de remplissage de la base de donnée avant de
lancer le serveurdjango

Pour la recherche par nom de chaque pokemon, on utilise de l'asynchronisme pour gagner en performance. De plus les
pokemons déjà requetés sont stocker dans une variable locale, on evite ainsi de re-requeter l'api à chaque rechargement
de la page.

## FRONTEND

Pour profiter de l'environnement de django, nous avons hoisis d'utiliser le systeme de template. L'inconvénient est que
le html est lourd, et qu'on doit jouer avec les dispaly (none, block, etc...)

## catalog

Ce package regroupe les fonctionnalité de recherche par catégorie de pokeon (type, pokedex, type d'oeuf, genre, etc...)


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