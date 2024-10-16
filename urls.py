from django.urls import path
from . import views

urlpatterns = [
    path('', views.clubes, name='clubes'),
    path('<str:nombre>/', views.detalle_club, name='detalle_club'),
]
