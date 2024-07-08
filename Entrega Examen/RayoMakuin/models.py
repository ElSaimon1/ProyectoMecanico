from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tipo_servicio(models.Model):
    id_tipo_ser = models.AutoField(db_column='id_tipo_ser', primary_key=True)
    Servicio = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self): 
        return str(self.Servicio)

class Comuna(models.Model):
    id_comuna = models.AutoField(db_column='id_comuna', primary_key=True)
    nom_comuna = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self): 
        return str(self.nom_comuna)

class Formulario(models.Model):
    user                = models.ForeignKey(User, on_delete = models.CASCADE)
    patente             = models.CharField(max_length=6)
    marca               = models.CharField(max_length=20)
    modelo              = models.CharField(max_length=20)
    telefono            = models.IntegerField(max_length=14)
    tipo_ser            = models.ForeignKey('Tipo_servicio',on_delete=models.CASCADE, db_column='id_tipo_ser')
    comuna              = models.ForeignKey('Comuna',on_delete=models.CASCADE, db_column='id_comuna')
    Detalles_servicio   = models.TextField(max_length=150)
    trabajoListo        = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.patente + '- by ' + self.user.username


