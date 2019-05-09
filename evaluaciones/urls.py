from django.contrib import admin
from django.urls import path
from evaluaciones import views

urlpatterns = [
    path('e/', views.evaluacion), #Evaluacion en curso vista por evaluador
    path('a/', views.evadmin), #Evaluacion en curso vista por admin
    path('mob/', views.evmobile), #Evaluacion en curso version movil
    path('post/e', views.postev), #Vista post entrega de evaluacion por evaluador
    path('post/a', views.postevadmin) #Vista post entrega de evaluacion por admin

    ]