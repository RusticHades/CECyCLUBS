# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clubes, name='clubes'),
    path('<str:nombre>/', views.detalle_club, name='detalle_club'),
    path('solicitar_club', views.solicitar_club, name='solicitar_club'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
] 