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
]