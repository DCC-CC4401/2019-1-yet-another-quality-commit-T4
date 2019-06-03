from django.contrib import admin

# Register your models here.
from .models import Evaluacion, EvaluacionGrupo, Resultados

admin.site.register(Evaluacion)
admin.site.register(EvaluacionGrupo)
admin.site.register(Resultados)

