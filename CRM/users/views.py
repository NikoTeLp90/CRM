from django.shortcuts import render, redirect
from .models import usuarios, companies
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView, DeleteView, View
from .forms import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .utils import generate_random_password
from django.contrib.auth.views import LoginView
from django.http import Http404



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
    
class userCreationSuccess(View):
    model = usuarios
    template_name = "registration/usercreationsuccess.html"

class userList(ListView):
    model = usuarios
    template_name = "registration/listUsers.html"



class userEdit(UpdateView):
    model = usuarios
    template_name = "registration/edituser.html"
    form_class = editUserform
    success_url = reverse_lazy("index")



class userDelete(DeleteView):
    model = usuarios
    template_name = "registration/deleteuser.html"
    success_url = reverse_lazy("index")

class SearchUser(View):
    def get(self, request):
        return render(request, 'registration/searchuser.html')

class SearchResults(View):
    def get(self, request):
        search_term = request.GET.get('search_term', '')
        search_option = request.GET.get('search_option')

        if search_option == 'ID':
            results = usuarios.objects.filter(id=search_term)
        elif search_option == 'DNI':
            results = usuarios.objects.filter(dni=search_term)
        elif search_option == 'Nombre':
            results = usuarios.objects.filter(nombre__icontains=search_term)
        elif search_option == 'Apellido':
            results = usuarios.objects.filter(apellido__icontains=search_term)
        else:
            results = []

        return render(request, 'registration/search_results.html', {'results': results})

class suspenderHabilitarUsuario(View):
    def get(self, request, pk):
        usuario = usuarios.objects.get(pk=pk)
        if usuario.is_active:
            usuario.is_active = False
        else:
            usuario.is_active = True
        usuario.save()
        return redirect('index') 
    
##Companies

class createCompany(FormView):
    template_name = "companies/companyCreation.html"
    form_class = companyCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # Guardar la compañía en la base de datos
        form.save()
        return super().form_valid(form)


class companyIndex(View):
    def get(self, request):
        user = request.user
        companias_asignadas = companies.objects.filter(responsable=user)
        return render(request, 'companies/index.html', {'companias': companias_asignadas})
    

class CompanyIndexView(View):
    def get(self, request, company_id):
        try:
            company = companies.objects.get(id=company_id, responsable=request.user)
            context = {'company': company}
            return render(request, 'companies/company_index.html', context)
        except companies.DoesNotExist:
            raise Http404("No tienes acceso a esta compañía o no existe.")