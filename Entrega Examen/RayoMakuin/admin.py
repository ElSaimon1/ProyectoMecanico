from django.contrib import admin
from .models import Tipo_servicio, Formulario, Comuna

# Register your models here.

admin.site.register(Tipo_servicio)
admin.site.register(Formulario)
admin.site.register(Comuna)