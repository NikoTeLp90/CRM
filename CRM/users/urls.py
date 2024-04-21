from django.contrib import admin
from django.urls import path
from .views import home, createUser, login

urlpatterns = [
    path('', home.as_view(), name="index"),
    path('createuser/', createUser.as_view(), name = 'createuser'),
    path('login/', login.as_view(), name ="login"),
]
