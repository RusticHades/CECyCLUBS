from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('eliminar-asistencia/<int:pk>/', views.eliminarAsistencia.as_view(), name='eliminarAsistencia'),
]