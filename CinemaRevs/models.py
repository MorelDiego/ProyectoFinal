from django.db import models
from django.utils.timezone import now

# Create your models here.
class Films(models.Model):
    titulo = models.CharField(max_length=40)
    año = models.IntegerField()
    duracion = models.IntegerField()
    genero = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=250)

class Reviews(models.Model):
    nombre = models.CharField(max_length=40)
    texto = models.CharField(max_length=250)
    fecha = models.DateField(default=now)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=90)
    mensaje = models.CharField(max_length=250)