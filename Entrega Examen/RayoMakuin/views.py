from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario, Tipo_servicio, Comuna
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import CrearRegistro
from django.utils import timezone
# Create your views here.

def formulario(request):
    context={}
    return render(request, 'RayoMakuin/formulario.html', context)

def home(request):
    context={}
    return render(request, 'RayoMakuin/home.html', context)

def perfilMC(request):
    context={}
    return render(request, 'RayoMakuin/perfilMC.html', context)

def base(request):
    context={}
    return render(request, 'RayoMakuin/base.html', context)

def iniciar_Sesion(request):
    if request.method == 'GET':
        return render(request, 'RayoMakuin/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'RayoMakuin/login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña estan mal'
            })
        else:
            login(request, user)
            return redirect('home')

def cerraSesion(request):
    logout(request)
    return redirect('home')

def register(request):
    
    if request.method == 'GET':
        return render(request, 'RayoMakuin/registro.html', 
                        {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('login')
            except IntegrityError:
                return render(request, 'RayoMakuin/registro.html',{
                                'form': UserCreationForm,
                                "error": 'El Usuario ya existe'
                                })
        return render(request, 'RayoMakuin/registro.html',{
            'form': UserCreationForm,
            "error": 'Las Contraseñas no son iguales'})

@login_required
def listar_registro(request):
    lista = Formulario.objects.filter(user = request.user, trabajoListo__isnull=True)
    return render(request, 'RayoMakuin/listarRegistros.html', {'listar': lista})

@login_required
def listar_registros_listos(request):
    lista = Formulario.objects.filter(user = request.user, trabajoListo__isnull=False).order_by
    ('-trabajoListo')
    return render(request, 'RayoMakuin/listarRegistros.html', {'listar': lista})

@login_required
def crear_registro(request):
    if request.method == 'GET':
        return render(request, 'RayoMakuin/crearRegistro.html',{
            'form' : CrearRegistro
        })
    else:
        try:
            form = CrearRegistro(request.POST)
            Nuevo_form = form.save(commit=False)
            Nuevo_form.user = request.user
            Nuevo_form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'RayoMakuin/crearRegistro.html',{
            'form' : CrearRegistro,
            'error' : 'Ingrese datos validos'
        })

@login_required
def detalleRegistro(request, detalle_id):
    if request.method == 'GET':
        registro = get_object_or_404(Formulario, pk=detalle_id, user = request.user)
        form = CrearRegistro(instance=registro)
        return render(request, 'RayoMakuin/detalleRegistro.html', {'registro': registro, 'form': form})
    else:
        try:
            registro = get_object_or_404(Formulario, pk=detalle_id, user = request.user)
            form = CrearRegistro(request.POST, instance=registro)
            form.save()
            return redirect('listarRegistro')
        except:
            return render(request, 'RayoMakuin/detalleRegistro.html', {'registro': registro, 'form': form,
                                                                        'error': 'Error al Actualizar los datos'})

@login_required
def registroListo(request, detalle_id):
    registro = get_object_or_404(Formulario, pk=detalle_id, user = request.user)
    if request.method == 'POST':
        registro.trabajoListo = timezone.now()
        registro.save()
        return redirect('listarRegistro')

@login_required
def EliminarRegistro(request, detalle_id):
    registro = get_object_or_404(Formulario, pk=detalle_id, user = request.user)
    if request.method == 'POST':
        registro.delete()
        return redirect('listarRegistro')
    return render(request, 'RayoMakuin/eliminar_registro.html', {'registro': registro})




