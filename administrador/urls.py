from django.contrib import admin
from django.urls import path
from administrador import views

urlpatterns = [
    path('lp/', views.landingpage), #Landing page de administrador
    path('ev/', views.evaluadores) #Evaluadores visto por admin


    ]