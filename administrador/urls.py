from django.contrib import admin
from django.urls import path
from administrador import views
from usuarios.views import evaluadores, modify_evaluador, delete_evaluador


app_name = 'administrador'
urlpatterns = [
    path('lp/', views.landingpage, name='landing'), #Landing page de administrador

    path('ev/', evaluadores), #Evaluadores visto por admin
    path('ev/delete/', delete_evaluador),
    path('ev/modify/', modify_evaluador),
    path('rub/', views.rubricas), #Rubricas vistas por el admin
    path('eval/', views.evaluaciones) #Lista de evaluaciones de admin



]