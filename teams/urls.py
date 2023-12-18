from . import views
from django.urls import path

urlpatterns = [
    path('get_all_teams/', views.get_all_teams, name='get_all_teams'),
    path('management_pokemon/', views.management_pokemon, name='management_pokemon'),
    path('add_team/', views.add_team, name='add_team'),
    path('', views.see_homepage, name='see_homepage'),
]