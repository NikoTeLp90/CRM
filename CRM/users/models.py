from django.db import models

# Create your models here.


class usuarios (models.Model):

    username = models.CharField(max_length=50, unique= True),
    nombre = models.CharField(max_length= 50),
    apellido = models.CharField(max_length=50),
    dni = models.IntegerField(max_length=8, unique= True),

