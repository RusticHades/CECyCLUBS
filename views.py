import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import Usuario


def registro_usuario(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo']
        email = request.POST['email']
        password = request.POST['password']
        rol = 'usuario'  # Asignamos el rol por defecto
        foto_perfil = request.FILES.get('foto_perfil')

        # Ruta base para guardar imágenes
        user_folder = f'static/images/fotos_perfil/{email}/'
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

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

from django.contrib.auth.decorators import user_passes_test

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