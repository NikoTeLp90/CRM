from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.



class home(TemplateView):
    template_name = "index.html"


class createUser(CreateView):
    model = MODEL_NAME
    template_name = "TEMPLATE_NAME"

