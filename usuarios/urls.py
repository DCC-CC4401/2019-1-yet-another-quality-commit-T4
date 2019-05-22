from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('process/', views.process_login, name='process'),
]