from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, verbose_name='su telefono') #verbose name es para la vista de admin
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre, self.apellido


class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.CharField(max_length=15)

    def __str__(self):
        return 'El servicio es %s y el precio es %s' % (self.nombre, self.precio)

class Pedido(models.Model):
    numero = models.IntegerField()
    Fecha = models.DateField()