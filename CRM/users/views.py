from django.shortcuts import render
from .models import usuarios
from django.views.generic import TemplateView, CreateView

# Create your views here.



class home(TemplateView):
    template_name = "index.html"


class createUser(CreateView):
    model = usuarios
    template_name = "registration/userCreation.html"

