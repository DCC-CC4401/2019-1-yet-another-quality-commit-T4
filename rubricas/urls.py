from django.contrib import admin
from django.urls import path
from rubricas import views
from django.conf.urls import include,url


urlpatterns = [
    path('a/', views.rubadmin), #Rubricas visto por admin
    path('ficha/a', views.fichaadmin), #ficha de rubrica visto por admin
    path('ficha/e', views.fichaeval), #ficha de rubrica visto por evaluador
    path('ficha/data',views.data),
    path('a/delete_rubric',views.deleterubric),
    path('a/ver_rubrica',views.verrubrica),
    path('a/modificar_rubrica',views.modificarrubrica),
    ]