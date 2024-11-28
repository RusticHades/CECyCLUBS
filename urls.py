from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.clubes, name='clubes'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('clubes/<str:nombre>/', views.detalles_club, name='detalle_club'),
    path('clubes/<str:nombre>/unirse/', views.unirse_club, name='unirse_club'),
    path('solicitud/rechazar/<int:solicitud_id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('solicitud/implementar/<int:solicitud_id>/', views.implementar_solicitud, name='implementar_solicitud'),
    path('<str:nombre>/agregar_noticia/', views.agregar_noticia, name='agregar_noticia'),
    path('<str:nombre>/agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('solicitar_club', views.solicitar_club, name='solicitar_club'),
    path('asistir-evento/<int:evento_id>/', views.asistir_evento, name='asistir_evento'),
    path('club/<str:nombre>/salir/', views.salir_club, name='salir_club'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)