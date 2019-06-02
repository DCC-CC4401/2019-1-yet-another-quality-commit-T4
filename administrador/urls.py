from django.urls import path
from administrador import views
from usuarios.views import evaluadores, modify_evaluador, delete_evaluador


app_name = 'administrador'
urlpatterns = [
    path('lp/', views.landingpage, name='landing'), #Landing page de administrador

    path('ev/', evaluadores), #Evaluadores visto por admin
    path('ev/delete/', delete_evaluador),
    path('ev/modify/', modify_evaluador),
    path('eval/delete/', views.deleteEvaluacion),
    path('eval/create/', views.createEvaluacion),
    path('eval/modify/', views.modifyEvaluacion),
    path('eval/', views.evaluaciones), #Lista de evaluaciones de admin
    path('rub/', views.rubricas), #Rubricas vistas por el admin

]
