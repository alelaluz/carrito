from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

# definimos la salida para ver de forma facil a q hacemos referencia para ver los reportes

    def __str__(self):
        return f'{self.nombre}->{self.precio}'
