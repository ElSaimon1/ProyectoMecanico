#from django.conf.url import url
from django.urls import path
from . import views



urlpatterns = [
    path('Ejemplo', views.Ejemplo, name='Ejemplo'),
    path('formulario', views.formulario, name='formulario'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('perfilMC', views.perfilMC, name='perfilMC'),
    path('registro', views.registro, name='registro'),
    path('servicio', views.servicio, name='servicio'),
    path('', views.base, name='base'),
]