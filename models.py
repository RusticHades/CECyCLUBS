from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    foto_perfil = models.ImageField(upload_to='fotosPerfil/', blank=True, null=True)
    ROL_CHOICES = [
        ('usuario', 'Usuario'),
        ('administrador', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='usuario')

    def __str__(self):
        return self.nombre_completo
