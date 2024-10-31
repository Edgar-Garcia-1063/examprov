from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id_proveedor=models.PositiveSmallIntegerField()
    nombre=models.CharField(max_length=100)
    contacto=models.CharField(max_length=100)
    telefono=models.PositiveSmallIntegerField()
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre