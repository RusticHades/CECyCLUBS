# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clubes, name='clubes'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/rechazar/<int:solicitud_id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('solicitud/implementar/<int:solicitud_id>/', views.implementar_solicitud, name='implementar_solicitud'),
    path('<str:nombre>/', views.detalles_club, name='detalle_club'),
    path('<str:nombre>/agregar_noticia/', views.agregar_noticia, name='agregar_noticia'),
    path('<str:nombre>/agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('solicitar_club', views.solicitar_club, name='solicitar_club'),
    path('asistir-evento/<int:evento_id>/', views.asistir_evento, name='asistir_evento'),
] 