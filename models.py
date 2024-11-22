from django.db import models
from django.conf import settings
from clubes.models import Evento 

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    club_id = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='eventos')
    usuario_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return f"Evento {self.id} - Club: {self.club.nombre} - Usuario: {self.usuario.username}"
