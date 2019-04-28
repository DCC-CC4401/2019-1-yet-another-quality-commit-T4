from django.contrib import admin
from django.urls import path
from rubricas import views

urlpatterns = [
    path('a/', views.rubadmin), #Rubricas visto por admin
    path('ficha/a', views.fichaadmin), #ficha de rubrica visto por admin
    path('ficha/e', views.fichaeval) #ficha de rubrica visto por evaluador
    ]