from django.shortcuts import render
from .models import usuarios
from django.views.generic import TemplateView, CreateView, FormView, ListView
from .forms import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .utils import generate_random_password
from django.contrib.auth.views import LoginView


# Create your views here.



class home(TemplateView):
    template_name = "index.html"

class login(LoginView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("index")
    

class createUser(FormView):
    template_name = "registration/userCreation.html"
    form_class = userCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # Generar una contraseña aleatoria
        password = generate_random_password()
        # Establecer la contraseña en el usuario creado
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        # Enviar correo electrónico con la contraseña
        send_mail(
            'Inicio de sesión en CRM',
            f'Buenos dias {user.nombre} {user.apellido} \nTus datos para ingresar son: \n Nombre de usuario: {user.username}\nContraseña: {password}\n clickea el siguiente link para dirigirte al login: 127.0.0.1:8000/login \n Gracias por elegir nuestro CRM',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)

class userList(ListView):
    model = usuarios
    template_name = "registration/listUsers.html"


