from django.contrib import admin

# Register your models here.
from .models import Integrante, Curso

admin.site.register(Integrante)
admin.site.register(Curso)