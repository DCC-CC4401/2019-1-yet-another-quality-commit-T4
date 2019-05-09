from django.contrib import admin
from django.urls import path
from cursos import views

urlpatterns = [
    path('a/', views.curadmin), #Cursos de administrador


    ]