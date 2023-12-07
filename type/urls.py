from . import views
from django.urls import path

urlpatterns = [
    path('', views.see_types, name='see_types'),
]