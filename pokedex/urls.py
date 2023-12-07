from . import views
from django.urls import path

urlpatterns = [
    path('',  views.see_all_pokedexes, name='index'),
    path('<str:id>', views.see_pokedex_by_id, name='pokedex'),
]