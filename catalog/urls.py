from django.urls import path

from catalog import views

urlpatterns = [
    path('<str:catalog_type>/',  views.see_all_catalog, name='see_all_catalog'),
    path('<str:catalog_type>/<str:catalog_name>',  views.see_all_pokemons_by_catalog, name='see_all_pokemon_by_catalog'),
]