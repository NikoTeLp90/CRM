from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class usuarios(AbstractUser):
    # Campos de usuario
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(blank=True, null= True, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50)
    password = models.CharField(max_length=128, default='')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
    def save(self, *args, **kwargs):
        if not self.password:
            self.password = make_password(None)  # Genera una contraseña encriptada si no se proporciona ninguna
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    

