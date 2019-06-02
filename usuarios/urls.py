from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('process/', views.process_login, name='process'),
    path('e/lp/', views.eval_loged, name='success_login_eval'),
    path('e/eval/', views.evaluaciones_evaluador, name='evaluaciones_evaluador')
]