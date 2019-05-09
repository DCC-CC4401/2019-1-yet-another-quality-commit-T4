from django.contrib import admin
from django.urls import path
from administrador import views

urlpatterns = [
    path('lp/', views.landingpage), #Landing page de administrador

    path('ev/', views.evaluadores), #Evaluadores visto por admin
    path('rub/', views.rubricas), #Rubricas vistas por el admin
    path('eval/', views.evaluaciones) #Lista de evaluaciones de admin



    ]