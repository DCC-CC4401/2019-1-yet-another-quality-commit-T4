from django.contrib import admin

# Register your models here.
from .models import Curso, Equipo, Estudiante

admin.site.register(Curso)
admin.site.register(Equipo)
admin.site.register(Estudiante)
