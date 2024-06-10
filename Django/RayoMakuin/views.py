from django.shortcuts import render

# Create your views here.



def Ejemplo(request):
    context={}
    return render(request, 'RayoMakuin/Ejemplo.html', context)

def formulario(request):
    context={}
    return render(request, 'RayoMakuin/formulario.html', context)

def home(request):
    context={}
    return render(request, 'RayoMakuin/home.html', context)

def login(request):
    context={}
    return render(request, 'RayoMakuin/login.html', context)

def perfilMC(request):
    context={}
    return render(request, 'RayoMakuin/perfilMC.html', context)

def registro(request):
    context={}
    return render(request, 'RayoMakuin/registro.html', context)

def servicio(request):
    context={}
    return render(request, 'RayoMakuin/servicio.html', context)

def base(request):
    context={}
    return render(request, 'RayoMakuin/base.html', context)

