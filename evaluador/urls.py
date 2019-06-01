from django.contrib import admin
from django.urls import path
from administrador import views

app_name = 'evaluador'
urlpatterns = [
    path('lp/', views.landingpage, name='landing') #Landing page de evaluador
]
