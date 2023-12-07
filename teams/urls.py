from . import views
from django.urls import path

urlpatterns = [
    path('create_pokemon/', views.create_pokemon, name='create_pokemon'),
    path('', views.see_homepage, name='see_homepage'),
]