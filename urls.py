# inicio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Define una ruta básica a tu vista principal
]
