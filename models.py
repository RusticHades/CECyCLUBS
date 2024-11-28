from django.conf import settings
from django.db import models

# Modelo del Club
class Club(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='clubes/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    miembros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='clubs', blank=True)  # Usar AUTH_USER_MODEL

    def __str__(self):
        return self.nombre

# Modelo de Evento
class Evento(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='eventos')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Modelo de Imagen asociada a un Evento
class ImagenEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='eventos/')
    
    def __str__(self):
        return f"Imagen para {self.evento.titulo}"

# Modelo de Publicación
class Publicacion(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='publicaciones')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Modelo de Imagen asociada a una Publicación
class ImagenPublicacion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='publicaciones/')
    
    def __str__(self):
        return f"Imagen para {self.publicacion.titulo}"

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
    correo = models.EmailField()  # Añadimos el campo correo

    def __str__(self):
        return self.nombre