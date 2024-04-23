from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = usuarios
        fields = ['username', 'email', 'password', 'password1']

class userCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    dni = forms.CharField(max_length=8, required=True)
    telefono = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=150, required=True)
        
    class Meta:
        model = usuarios
        fields = ['username', 'email', 'nombre', 'apellido', 'dni', 'telefono', 'direccion']

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get("username")
        dni = cleaned_data.get("dni")
        email = cleaned_data.get("email")
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        telefono = cleaned_data.get("telefono")
        direccion = cleaned_data.get("direccion")
        if not username:
            raise forms.ValidationError("El nombre de usuario es requerido")
        if not email:
            raise forms.ValidationError("El email es requerido")
        if not nombre:
            raise forms.ValidationError("El nombre es requerido")
        if not apellido:
            raise forms.ValidationError("El apellido es requerido")
        if not telefono:
            raise forms.ValidationError("El telefono es requerido")
        if not direccion:
            raise forms.ValidationError("La direccion es requerida")
        return cleaned_data
        

class editUserform(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    dni = forms.CharField(max_length=8, required=True)
    telefono = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=150, required=True)
        
    class Meta:
        model = usuarios
        fields = ['username', 'email', 'nombre', 'apellido', 'dni', 'telefono', 'direccion']

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get("username")
        dni = cleaned_data.get("dni")
        email = cleaned_data.get("email")
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        telefono = cleaned_data.get("telefono")
        direccion = cleaned_data.get("direccion")
        if not username:
            raise forms.ValidationError("El nombre de usuario es requerido")
        if not email:
            raise forms.ValidationError("El email es requerido")
        if not nombre:
            raise forms.ValidationError("El nombre es requerido")
        if not dni:
            raise forms.ValidationError("El DNI es requerido")
        if not apellido:
            raise forms.ValidationError("El apellido es requerido")
        if not telefono:
            raise forms.ValidationError("El telefono es requerido")
        if not direccion:
            raise forms.ValidationError("La direccion es requerida")
        return cleaned_data
    
class companyCreationForm(forms.ModelForm):
    pais = forms.CharField(max_length=50, required=True)
    actividad = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=250, required=True)
    responsable = forms.ModelChoiceField(queryset=usuarios.objects.all(), required=True)

    class Meta:
        model = companies
        fields = ['pais', 'actividad', 'descripcion', 'responsable']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data