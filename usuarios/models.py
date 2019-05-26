from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Aca deberian estar los modelos de los distintos usuarios que tengamos


class Administrador(models.Model):
    """Un turbo ejemplo"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aca deberian ir mas campos, por ahora esta lo basico

    def __str__(self):
        return self.user.username
