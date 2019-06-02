from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('process/', views.process_login, name='process'),
    path('e/lp/', views.eval_loged, name='success_login_eval'),
    path('e/eval/', views.evaluaciones_evaluador, name='evaluaciones_evaluador'),
    path('a/lp/', views.landingpage, name='landing'), #Landing page de administrador
    path('a/ev/', views.evaluadores),  # Evaluadores visto por admin
    path('a/ev/delete/', views.delete_evaluador),
    path('a/ev/modify/', views.modify_evaluador),
    path('a/eval/delete/', views.deleteEvaluacion),
    path('a/eval/create/', views.createEvaluacion),
    path('a/eval/modify/', views.modifyEvaluacion),
    path('a/eval/', views.evaluaciones),  # Lista de evaluaciones de admin
    path('a/rub/', views.rubricas),  # Rubricas vistas por el admin

]