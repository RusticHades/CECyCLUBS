# models.py
from django.db import models

# Modelo de Club
class Club(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='clubes/', blank=True, null=True)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Solicitud de Club
class SolicitudClub(models.Model):
    ESTATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    actividades = models.TextField()
    estatus = models.CharField(
        max_length=10,
        choices=ESTATUS_CHOICES,
        default='pendiente'
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
