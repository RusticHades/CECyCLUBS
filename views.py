from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, SolicitudClub
from django.core.files.storage import FileSystemStorage
import os

def clubes(request):
    clubes = Club.objects.all()
    
    # Agrupar los clubes por categora
    categorias = {}
    for club in clubes:
        if club.categoria not in categorias:
            categorias[club.categoria] = []
        categorias[club.categoria].append(club)

    # Pasar el diccionario de categoras al template
    return render(request, 'clubes.html', {'clubes': categorias})

# Vista para mostrar los detalles de un club especifico
def detalle_club(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)
    return render(request, 'detallesClub.html', {'club': club})

# Vista para mostrar el formulario de solicitud de club
def solicitar_club(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']
        actividades = request.POST['actividades']
        
        # Crear una nueva solicitud de club
        SolicitudClub.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            actividades=actividades
        )
    
    return render(request, 'solicitarClub.html')

# Vista para mostrar las solicitudes pendientes de clubs
def solicitudes(request):
    solicitudes = SolicitudClub.objects.filter(estatus='pendiente')
    return render(request, 'solicitudes.html', {'solicitudes': solicitudes})

# Vista para rechazar una solicitud de club
def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudClub, id=solicitud_id)
    solicitud.estatus = 'rechazado'
    solicitud.save()
    return redirect('solicitudes')

# Vista para aprobar una solicitud e implementarla como club
def implementar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudClub, id=solicitud_id)
    
    if request.method == 'POST':
        imagen = request.FILES.get('imagen')
        
        if imagen:
            # Definimos el path para guardar la imagen en static
            club_folder = f'static/images/portadasClub/{solicitud.nombre}/'
            os.makedirs(club_folder, exist_ok=True)  # Crea la carpeta si no existe
            
            # Guardamos la imagen en la carpeta del club
            fs = FileSystemStorage(location=club_folder)
            filename = fs.save(imagen.name, imagen)
            image_path = os.path.join(club_folder, filename)
        
        # Crear el club con la ruta de imagen almacenada
        Club.objects.create(
            nombre=solicitud.nombre,
            descripcion=solicitud.descripcion,
            categoria=solicitud.categoria,
            imagen=image_path  # Guardar la ruta en el campo de imagen
        )
        
        # Cambiar el estado de la solicitud
        solicitud.estatus = 'aprobado'
        solicitud.save()
        return redirect('solicitudes')
    
    return render(request, 'implementarClub.html', {'solicitud': solicitud})
