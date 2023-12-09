from . import views
from django.urls import path

urlpatterns = [
    path('', views.see_all_types, name='see_types'),
    path('<str:id>', views.see_all_pokemons_by_type, name='pokemon_by_type'),
]