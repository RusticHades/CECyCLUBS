# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, SolicitudClub

def clubes(request):
    clubes = Club.objects.all()
    
    # Agrupar los clubes por categoría
    categorias = {}
    for club in clubes:
        if club.categoria not in categorias:
            categorias[club.categoria] = []
        categorias[club.categoria].append(club)

    # Pasar el diccionario de categorías al template
    return render(request, 'clubes.html', {'clubes': categorias})


# Vista para mostrar los detalles de un club específico
def detalle_club(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)
    return render(request, 'detalle_club.html', {'club': club})

# Vista para mostrar el formulario de solicitud de club
def solicitar_club(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']
        actividades = request.POST['actividades']
        
        # Crear una nueva solicitud de club
        solicitud = SolicitudClub.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            actividades=actividades
        )
        solicitud.save()
        return redirect('solicitudes')
    
    return render(request, 'solicitarClub.html')

# Vista para mostrar todas las solicitudes de club
def solicitudes(request):
    solicitudes = SolicitudClub.objects.all()
    return render(request, 'solicitudes.html', {'solicitudes': solicitudes})
