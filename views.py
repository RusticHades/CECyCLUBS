from django.shortcuts import render
# inicio/views.py

from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html', {
        'usuario': request.user,
    })