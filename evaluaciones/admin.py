from django.contrib import admin

# Register your models here.
from .models import Integrante, Evaluador, Curso, Evaluacion

admin.site.register(Integrante)
admin.site.register(Evaluador)
admin.site.register(Curso)
admin.site.register(Evaluacion)