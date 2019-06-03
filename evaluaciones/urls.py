from django.contrib import admin
from django.urls import path
from evaluaciones import views


app_name = 'evaluaciones'

urlpatterns = [
    path('a/<int:evaluacion_id>/<int:equipo_id>/<int:estudiante_id>', views.evaluacion),  # Evaluacion en curso vista por admin
    path('a/<int:evaluacion_id>', views.evadmin, name='ficha'),  # Evaluacion en curso vista por admin
    path('e/<int:evaluacion_id>/<int:equipo_id>/<int:estudiante_id>', views.evaluacion_evaluador),  # Evaluacion en curso vista por evaluador
    path('e/<int:evaluacion_id>', views.evev, name='ficha_evaluador'),  # Evaluacion en curso vista por evaluador
    path('mob/', views.evmobile),  # Evaluacion en curso version movil
    path('post/e', views.postev),  # Vista post entrega de evaluacion por evaluador
    path('post/a', views.postevadmin),  # Vista post entrega de evaluacion por admin
    path('a/data',views.postevresult, name='process_result'),
    path('e/data',views.postevresult_evaluador, name='process_result_evaluador'),
    path('e/admin/',views.evaluacion_admin),
]
