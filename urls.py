# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clubes, name='clubes'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/rechazar/<int:solicitud_id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('solicitud/implementar/<int:solicitud_id>/', views.implementar_solicitud, name='implementar_solicitud'),
    path('<str:nombre>/', views.detalle_club, name='detalle_club'),
    path('solicitar_club', views.solicitar_club, name='solicitar_club'),
] 