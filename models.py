from django.db import models

class EventoAsistido(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='static/images/eventos_asistidos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
