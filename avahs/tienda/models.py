from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precioAnterior = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    unidades = models.IntegerField(default=0)
    nuevo = models.BooleanField(default=False, null=False)
    descuento = models.BooleanField(default=False, null=False)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre