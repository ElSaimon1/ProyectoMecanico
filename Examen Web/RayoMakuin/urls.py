#from django.conf.url import url
from django.urls import path
from . import views



urlpatterns = [
    path('formulario/', views.formulario, name='formulario'),
    path('', views.home, name='home'),
    path('login/', views.iniciar_Sesion, name='login'),
    path('logout/', views.cerraSesion, name='logout'),
    path('perfilMC/', views.perfilMC, name='perfilMC'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('listarRegistro/', views.listar_registro, name='listarRegistro'),
    path('listarRegistroListo/', views.listar_registros_listos, name='listarRegistroListo'),
    path('crearRegistro/', views.crear_registro, name='crearRegistro'),
    path('detalleRegistro/<int:detalle_id>/', views.detalleRegistro, name='detalleRegistro'),
    path('registroListo/<int:detalle_id>/', views.registroListo, name='registroListo'),
    path('eliminarRegistro/<int:detalle_id>/', views.EliminarRegistro, name='EliminarRegistro'),

]