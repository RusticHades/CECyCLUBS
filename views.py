from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, SolicitudClub, Publicacion, Evento, ImagenPublicacion, ImagenEvento
from django.core.files.storage import FileSystemStorage
import os

# Vista para ver los detalles de un club
def detalles_club(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)
    publicaciones = Publicacion.objects.filter(club=club)
    eventos = Evento.objects.filter(club=club)
    
    return render(request, 'detallesClub.html', {
        'club': club,
        'publicaciones': publicaciones,
        'eventos': eventos,
    })

# Vista para agregar una noticia
def agregar_noticia(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        imagenes = request.FILES.getlist('imagenes')

        # Crear la publicación
        publicacion = Publicacion.objects.create(club=club, titulo=titulo, contenido=contenido)

        # Definir el directorio para guardar las imágenes
        publicacion_folder = f'static/images/publicaciones/{club.nombre}/'
        os.makedirs(publicacion_folder, exist_ok=True)  # Crear la carpeta si no existe

        # Guardar las imágenes de la publicación
        for imagen in imagenes:
            fs = FileSystemStorage(location=publicacion_folder)
            filename = fs.save(imagen.name, imagen)
            image_path = os.path.join(publicacion_folder, filename)
            ImagenPublicacion.objects.create(publicacion=publicacion, imagen=image_path)

        return redirect('detalle_club', nombre=club.nombre)

    return render(request, 'agregarNoticia.html', {'club': club})

# Vista para agregar un evento
def agregar_evento(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        imagenes = request.FILES.getlist('imagenes')

        # Crear el evento
        evento = Evento.objects.create(club=club, titulo=titulo, descripcion=descripcion, fecha=fecha)

        # Definir el directorio para guardar las imágenes
        evento_folder = f'static/images/eventos/{club.nombre}/'
        os.makedirs(evento_folder, exist_ok=True)  # Crear la carpeta si no existe

        # Guardar las imágenes del evento
        for imagen in imagenes:
            fs = FileSystemStorage(location=evento_folder)
            filename = fs.save(imagen.name, imagen)
            image_path = os.path.join(evento_folder, filename)
            ImagenEvento.objects.create(evento=evento, imagen=image_path)

        return redirect('detalle_club', nombre=club.nombre)

    return render(request, 'agregarEvento.html', {'club': club})

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
        
        # Crea el club
        Club.objects.create(
            nombre=solicitud.nombre,
            descripcion=solicitud.descripcion,
            categoria=solicitud.categoria,
            imagen=image_path
        )
        
        # Cambiar el estado de la solicitud
        solicitud.estatus = 'aprobado'
        solicitud.save()
        return redirect('solicitudes')
    
    return render(request, 'implementarClub.html', {'solicitud': solicitud})

# Vista para mostrar los clubes agrupados por categoría
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
