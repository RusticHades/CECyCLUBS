from django.urls import path, include
from configuracion import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('clubes/', include('clubes.urls')),
    path('eventos/', include('eventos.urls')),
    path('configuracion/', include('configuracion.urls')),
]