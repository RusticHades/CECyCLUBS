from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from .models import Asistencia
from clubes.models import Evento
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from clubes.models import Evento

@login_required
def eventos(request):
    try:
        # Filtrar asistencias del usuario logueado
        asistencias = Asistencia.objects.filter(usuario_id=request.user)

        # Obtener los eventos a los que el usuario ha asistido
        eventos_asistidos = Evento.objects.filter(id__in=asistencias.values_list('club_id', flat=True)).order_by('fecha')
    except Asistencia.DoesNotExist:
        eventos_asistidos = []

    # Pasar tanto los eventos como las asistencias a la plantilla
    return render(request, 'eventos.html', {
        'eventos': eventos_asistidos,
        'asistencias': asistencias
    })

class eliminarAsistencia(DeleteView):
    model = Asistencia
    success_url = reverse_lazy('eventos')

    def get(self, request, *args, **kwargs):
        # Obtenemos la asistencia que queremos eliminar
        obj = self.get_object()
        # Eliminar la asistencia
        obj.delete()
        # Redirigir al usuario de vuelta al calendario de eventos
        return HttpResponseRedirect(self.success_url)