from django.contrib import admin

# Register your models here.
from .models import Administrador, Evaluador

admin.site.register(Administrador)
admin.site.register(Evaluador)