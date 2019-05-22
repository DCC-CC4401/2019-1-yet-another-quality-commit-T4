from django.contrib import admin
from django.urls import path
from administrador import views

app_name = 'administrador'
urlpatterns = [
    path('lp/', views.landingpage, name='landing'), #Landing page de administrador

    path('ev/', views.evaluadores), #Evaluadores visto por admin
    path('ev/delete/', views.deleteEvaluador),
    path('ev/modify/', views.modifyEvaluador),
    path('rub/', views.rubricas), #Rubricas vistas por el admin
    path('eval/', views.evaluaciones) #Lista de evaluaciones de admin



    ]