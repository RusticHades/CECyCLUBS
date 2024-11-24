from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# Registrar el namespace
app_name = 'configuracion'

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('iniciar-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('', views.configuracion, name='configuracion'),
    path('buscar-usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('cambiar-rol/<int:usuario_id>/', views.cambiar_rol, name='cambiar_rol'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('buscar-club/', views.buscar_club, name='buscar_club'),
    path('editar-club/<int:club_id>/', views.editar_club, name='editar_club'),
    path('eliminar-club/<int:club_id>/', views.eliminar_club, name='eliminar_club'),
    path('usuario/<int:usuario_id>/', views.ver_usuario, name='ver_usuario'),
    path('expulsar_de_club/<int:club_id>/<int:usuario_id>/', views.expulsar_de_club, name='expulsar_de_club'),
    path('club/<int:club_id>/', views.ver_club, name='ver_club'),
    path('editar_publicacion/<int:publicacion_id>/', views.editar_publicacion, name='editar_publicacion'),
    path('editar_evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
]