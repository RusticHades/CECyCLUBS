import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
from .models import Usuario
from clubes.models import Club, Publicacion, Evento

@login_required
def ver_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    publicaciones = club.publicaciones.all()
    eventos = club.eventos.all()

    if request.method == 'POST':
        if 'eliminar_publicacion' in request.POST:
            publicacion_id = request.POST.get('publicacion_id')
            publicacion = get_object_or_404(Publicacion, id=publicacion_id)
            publicacion.delete()
            messages.success(request, "Publicación eliminada exitosamente.")
            return redirect('configuracion:ver_club', club_id=club.id)
        
        if 'eliminar_evento' in request.POST:
            evento_id = request.POST.get('evento_id')
            evento = get_object_or_404(Evento, id=evento_id)
            evento.delete()
            messages.success(request, "Evento eliminado exitosamente.")
            return redirect('configuracion:ver_club', club_id=club.id)

    return render(request, 'verClub.html', {
        'club': club,
        'publicaciones': publicaciones,
        'eventos': eventos,
    })


@login_required
def ver_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    clubes = usuario.clubs.all()  # Obtiene los clubes a los que el usuario pertenece
    return render(request, 'verUsuario.html', {
        'usuario': usuario,
        'clubes': clubes,
    })

@login_required
def expulsar_de_club(request, club_id, usuario_id):
    if not request.user.is_authenticated or request.user.rol != 'administrador':
        return redirect('configuracion:inicio_sesion')

    club = get_object_or_404(Club, id=club_id)
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if usuario in club.miembros.all():
        club.miembros.remove(usuario)  # Elimina al usuario del club

    return redirect('configuracion:ver_usuario', usuario_id=usuario.id)

@login_required
def buscar_club(request):
    query = request.GET.get('query', '')
    clubes = Club.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'configuracion.html', {'clubes': clubes})

@login_required
def editar_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if request.method == 'POST':
        club.nombre = request.POST.get('nombre')
        club.descripcion = request.POST.get('descripcion')
        club.categoria = request.POST.get('categoria')
        if 'imagen' in request.FILES:
            club.imagen = request.FILES['imagen']
        club.save()
        messages.success(request, 'El club ha sido actualizado correctamente.')
        return redirect('configuracion:buscar_club')
    return render(request, 'editarClub.html', {'club': club})

@login_required
def eliminar_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    club.delete()
    messages.success(request, 'El club ha sido eliminado correctamente.')
    return redirect('configuracion:buscar_club')


def registro_usuario(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo']
        email = request.POST['email']
        password = request.POST['password']
        rol = 'usuario'  # Asignamos el rol por defecto
        foto_perfil = request.FILES.get('foto_perfil')

        # Ruta base para guardar imágenes
        user_folder = f'static/images/fotosPerfil/{email}/'
        os.makedirs(user_folder, exist_ok=True)  # Crear carpeta si no existe

        foto_url = None
        if foto_perfil:
            # Guardar la imagen en la carpeta del usuario
            fs = FileSystemStorage(location=user_folder)
            filename = fs.save(foto_perfil.name, foto_perfil)
            foto_url = os.path.join(user_folder, filename)  # Ruta relativa

        # Crear el usuario
        usuario = Usuario.objects.create_user(
            username=email,  # Usamos el email como username
            email=email,
            password=password,
            nombre_completo=nombre_completo,
            rol=rol,
            foto_perfil=foto_url,  # Guarda la ruta relativa
        )

        # Iniciar sesión automáticamente
        login(request, usuario)
        return redirect('configuracion:configuracion')

    return render(request, 'registro.html')

def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        usuario = authenticate(request, username=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('configuracion:configuracion')
        else:
            return render(request, 'iniciarSesion.html', {'error': 'Credenciales inválidas'})

    return render(request, 'iniciarSesion.html')


@login_required
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('configuracion:inicio_sesion')  # Redirige a la página de inicio de sesión

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        request.user.nombre_completo = request.POST['nombre_completo']
        request.user.email = request.POST['email']
        if 'foto_perfil' in request.FILES:
            foto_perfil = request.FILES['foto_perfil']

            # Ruta base para guardar imágenes del usuario
            user_folder = f'static/images/fotosPerfil/{request.user.email}/'
            os.makedirs(user_folder, exist_ok=True)  # Crear carpeta si no existe

            # Guardar nueva imagen
            fs = FileSystemStorage(location=user_folder)
            filename = fs.save(foto_perfil.name, foto_perfil)
            foto_url = os.path.join(user_folder, filename)  # Ruta relativa

            request.user.foto_perfil = foto_url  # Actualizar ruta en el modelo

        request.user.save()
        return redirect('configuracion:configuracion')

    return render(request, 'editarPerfil.html')


@login_required
def configuracion(request):
    return render(request, 'configuracion.html')


def es_administrador(usuario):
    return usuario.is_authenticated and usuario.rol == 'administrador'


@user_passes_test(es_administrador)
def buscar_usuario(request):
    query = request.GET.get('query', '')
    usuarios = Usuario.objects.filter(nombre_completo__icontains=query).exclude(pk=request.user.pk)
    return render(request, 'configuracion.html', {'usuarios': usuarios})


@user_passes_test(es_administrador)
def cambiar_rol(request, usuario_id):
    if request.method == 'POST':
        nuevo_rol = request.POST.get('rol')
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        usuario.rol = nuevo_rol
        usuario.save()
        return redirect('configuracion:configuracion')
    
@user_passes_test(es_administrador)
def eliminar_usuario(request, usuario_id):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        
        # Evitar que un administrador se elimine a sí mismo
        if usuario == request.user:
            return redirect('configuracion:configuracion')  # Opcional: muestra un mensaje de error
        
        usuario.delete()  # Elimina al usuario de la base de datos
        return redirect('configuracion:configuracion')
