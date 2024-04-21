from django.db import models

# Create your models here.


class usuarios (models.Model):

    username = models.CharField(max_length=50, required = True, unique= True)
    nombre = models.CharField(max_length= 50, required = True)
    apellido = models.CharField(max_length=50, required = True)
    