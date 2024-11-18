from django.shortcuts import render
from .models import EventoAsistido

def eventos(request):
    eventos = EventoAsistido.objects.all().order_by('fecha')
    return render(request, 'eventos.html', {'eventos': eventos})
