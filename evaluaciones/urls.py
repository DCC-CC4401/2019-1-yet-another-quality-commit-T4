from django.contrib import admin
from django.urls import path
from evaluaciones import views


app_name = 'evaluaciones'

urlpatterns = [
    path('e/<int:evaluacion_id>/<int:equipo_id>/<int:estudiante_id>', views.evaluacion),  # Evaluacion en curso vista por evaluador
    path('a/<int:evaluacion_id>', views.evadmin, name='ficha'),  # Evaluacion en curso vista por admin
    path('mob/', views.evmobile),  # Evaluacion en curso version movil
    path('post/e', views.postev),  # Vista post entrega de evaluacion por evaluador
    path('post/a', views.postevadmin),  # Vista post entrega de evaluacion por admin
    path('e/data',views.postevresult, name='process_result'),
    path('e/admin/',views.evaluacion_admin),
]
