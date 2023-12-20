# SETUP

### VENV

- python3 -m venv venv (créer un environnement virtuel)
- source venv/bin/activate (active l’environnement virtuel)

### REQUIREMENTS

- pip freeze > requirements.txt (créer un fichier requirements.txt)
- pip install -r requirements.txt (installe les dépendances necessaires)

# FONCTIONNALITÉS

## Catalogue

Le catalogue permet de chercher tous les Pokémon appartenant à un même catalogue. On peut accéder aux différents
catalogues depuis la homepage via les boutons sur le panneau de droite qui liste les types de catalogues
(Pokedex, type d’œuf, genre, type, etc.). En sélectionnant un type de catalogue,
on accède à une page listant tous les catalogues appartenant à ce type (feu, eau, etc.).
C’est en cliquant sur des catalogues spécifiques qu'on peut voir apparaître la liste des Pokémon
(tous les Pokémon de type feu, tous les Pokémon du pokedex kanto, etc.).

Les Pokémon sont affichés par tranche de 25 pour éviter de surcharger la page. En cliquant sur le bouton "voir plus :",
25 de plus se rajoutent. Le deuxième accès à la page est plus rapide grace au cache.

Cliquer sur un Pokémon affiche sa carte, on peut choisir de l’ajouter à une équipe au préalable créé via la homepage.
On reviendra là-dessus plus tard.

## Équipes

La page d’équipe ou la homepage permet de créer er supprimer une équipe, de voir les Pokémon appartenant à une équipe et
de les supprimer.

La homepage permet l’accès aux différents catalogues, mais aussi a la fonctionnalité de recherche par nom. Un traducteur
français est intégré dans le traitement de la recherche, vous pouvez donc entrer des noms de Pokémon français, une
approximation est faite, vous verrez par ordre de pertinence les Pokémon dont le nom correspond plus ou moins à votre
requête.

---

# TECHNIQUE

# BDD

La bdd sert uniquement pour le stockage des Pokémon et des équipes.
Pour des soucis de simplicité, on stocke en base uniquement les informations suivantes :

### Pokémon

- id
- id (coté PokeApi)

### Teams

- id
- name

### PokémonTeams

- id
- Pokémon_id
- team_id

La table Pokémon n’est pas nécessaire pour l’actuel fonctionnement de l’application, mais par anticipation d’une
fonctionnalité de duel et de gestion des hp, nous avons créé une table dédiée.

---

## BACKEND

Le Back est scindé en 2 parties principales :

- catalog
- teams
  Le catalog gère l’affichage des Pokémon par catalogue ainsi que celui du type de catalog
  Le package teams gère la gestion des équipes de Pokémon et notre homepage

### POKEAPI

Pour utiliser un maximum l’api pokeapi, on ne stocke aucun Pokémon en base de données, on les récupère directement via
les endpoints disponibles, une amélioration future serait de réaliser un script de remplissage de la base de données
avant de lancer le serveur Django.

Pour la recherche par nom de chaque Pokémon, on utilise de l’asynchronisme pour gagner en performance. De plus, les
Pokémon déjà chargés sont stockés dans une variable locale, on évite ainsi de re-requêter l’api à chaque rechargement de
la page.

## FRONTEND

Pour profiter de l’environnement de Django, nous avons choisi d’utiliser le système de template. L’inconvénient est que
le html est lourd, et qu'on doit jouer avec les display (none, block, etc.)

## catalog

Ce package regroupe les fonctionnalités de recherche par catégorie de Pokémon (type, pokedex, type d’œuf, genre, etc.)

# Améliorations futures

- Ajouter une fonctionnalité de duel
- Stocker en base les PV des Pokémon
- Calcule des dégâts en fonction des types et des attaques
- Système de leveling, chaque combat gagné incrémente le level du Pokémon ainsi que ses stats
- Un Pokémon mort est supprimé de l’équipe, il faut donc le rajouter ce qui reset ses stats


- Ajouter une gestion de l’utilisateur
- Nouvelle table en base + liaison des équipes à un utilisateur
- Ajouter une fonctionnalité de login


- Ajouter un script de remplissage automatique de la base de données pour gagner en performance sur les recherches
  ¯¯¯¯¯