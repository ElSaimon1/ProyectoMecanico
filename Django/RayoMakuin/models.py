from django.db import models

# Create your models here.

class Tipo_servicio(models.Model):
    id_tipo_ser = models.AutoField(db_column='id_tipo_ser', primary_key=True)
    Servicio = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self): 
        return str(self.Servicio)

class comuna(models.Model):
    id_comuna = models.AutoField(db_column='id_comuna', primary_key=True)
    comuna = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self): 
        return str(self.comuna)

class Formulario(models.Model):
    patente             = models.CharField(primary_key=True, max_length=6)
    marca               = models.CharField(max_length=20)
    modelo              = models.CharField(max_length=20)
    telefono            = models.CharField(max_length=45)
    id_tipo_ser         = models.ForeignKey('Tipo_servicio',on_delete=models.CASCADE, db_column='id_tipo_ser')
    comuna              = models.CharField(max_length=45)
    Detalles_servicio   = models.CharField(max_length=20) 
    Ingrese_archivo     = models.CharField(max_length=20)  


