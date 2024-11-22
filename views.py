from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, SolicitudClub, Publicacion, Evento, ImagenPublicacion, ImagenEvento
from django.core.files.storage import FileSystemStorage
import os
from django.contrib.auth.decorators import login_required

def detalles_club(request, nombre):
    # Obtén el club
    club = get_object_or_404(Club, nombre=nombre)
    
    # Filtra las publicaciones y eventos
    publicaciones = Publicacion.objects.filter(club=club)
    eventos = Evento.objects.filter(club=club)
    
    # Obtén los miembros del club
    miembros = club.miembros.all()

    # Verificar si el usuario es miembro del club
    es_miembro = request.user in club.miembros.all()

    # Pasar los miembros con la URL de la imagen correctamente
    for miembro in miembros:
        if miembro.foto_perfil:
            miembro.foto_perfil_url = '/' + miembro.foto_perfil.name
        else:
            miembro.foto_perfil_url = None  # Si no hay foto, asigna None

    return render(request, 'detallesClub.html', {
        'club': club,
        'publicaciones': publicaciones,
        'eventos': eventos,
        'miembros': miembros,
        'es_miembro': es_miembro,
    })


# Vista para agregar una noticia
@login_required
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

        # Guardar las imágenes si existen
        if imagenes:
            for imagen in imagenes:
                fs = FileSystemStorage(location=publicacion_folder)
                filename = fs.save(imagen.name, imagen)
                image_path = os.path.join(publicacion_folder, filename)
                ImagenPublicacion.objects.create(publicacion=publicacion, imagen=image_path)

        return redirect('detalle_club', nombre=club.nombre)

    return render(request, 'agregarNoticia.html', {'club': club})

# Vista para agregar un evento
@login_required
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

        # Guardar las imágenes si existen
        if imagenes:
            for imagen in imagenes:
                fs = FileSystemStorage(location=evento_folder)
                filename = fs.save(imagen.name, imagen)
                image_path = os.path.join(evento_folder, filename)
                ImagenEvento.objects.create(evento=evento, imagen=image_path)

        return redirect('detalle_club', nombre=club.nombre)

    return render(request, 'agregarEvento.html', {'club': club})

@login_required
def unirse_club(request, nombre):
    club = get_object_or_404(Club, nombre=nombre)

    # Agregar al usuario al club
    club.miembros.add(request.user)
    return redirect('detalle_club', nombre=club.nombre)


# Vista para mostrar el formulario de solicitud
@login_required
def solicitar_club(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        actividades = request.POST['actividades']
        
        # Crear una nueva solicitud de club sin la descripción
        SolicitudClub.objects.create(
            nombre=nombre,
            categoria=categoria,
            actividades=actividades
        )
    
    return render(request, 'solicitarClub.html')


# Vista para mostrar las solicitudes pendientes de clubs
@login_required
def solicitudes(request):
    solicitudes = SolicitudClub.objects.filter(estatus='pendiente')
    return render(request, 'solicitudes.html', {'solicitudes': solicitudes})

# Vista para rechazar una solicitud de club
@login_required
def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudClub, id=solicitud_id)
    solicitud.estatus = 'rechazado'
    solicitud.save()
    return redirect('solicitudes')

# Vista para aprobar una solicitud e implementarla como club
@login_required
def implementar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudClub, id=solicitud_id)
    
    if request.method == 'POST':
        # Recuperar los datos enviados por el formulario
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']
        imagen = request.FILES.get('imagen')

        image_path = None  # Inicializamos por si no hay imagen

        if imagen:
            # Definimos el path para guardar la imagen en static
            club_folder = f'static/images/portadasClub/{nombre}/'
            os.makedirs(club_folder, exist_ok=True)  # Crea la carpeta si no existe
            
            # Guardamos la imagen en la carpeta del club
            fs = FileSystemStorage(location=club_folder)
            filename = fs.save(imagen.name, imagen)
            image_path = os.path.join(club_folder, filename)

        # Crear el club con los datos actualizados del formulario
        Club.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
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

    # Si hay una búsqueda, filtrar los clubes por nombre
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        clubes = clubes.filter(nombre__icontains=busqueda)  # Filtrar por nombre del club (case-insensitive)

    # Agrupar los clubes por categoría
    categorias = {}
    for club in clubes:
        if club.categoria not in categorias:
            categorias[club.categoria] = []
        categorias[club.categoria].append(club)

    # Pasar el diccionario de categorías al template
    return render(request, 'clubes.html', {'clubes': categorias, 'busqueda': busqueda})


from eventos.models import EventoAsistido

@login_required
def asistir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    # Crear un registro en la tabla de eventos asistidos
    EventoAsistido.objects.create(
        nombre=evento.titulo,
        descripcion=evento.descripcion,
        fecha=evento.fecha,
        imagen=evento.imagenes.first().imagen.url if evento.imagenes.exists() else None,
    )
    return redirect('detalle_club', nombre=evento.club.nombre)
