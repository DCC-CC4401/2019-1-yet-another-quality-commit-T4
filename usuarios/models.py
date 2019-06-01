from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Aca deberian estar los modelos de los distintos usuarios que tengamos


class Administrador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aca deberian ir mas campos, por ahora esta lo basico

    def __str__(self):
        return self.user.username


class Evaluador(models.Model):
    # el mail va a ser el nombre de usuario del user de django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aca deberian ir mas campos, por ahora esta lo basico
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    @property
    def email(self):
        return self.user.username


    @email.setter
    def email(self, email):
        self.user.username = email


    def save(self, *args, **kwargs):
        super(Evaluador, self).save(*args, **kwargs)
        self.user.save()


    def __str__(self):
        return self.nombre + " " + self.apellido


    class Meta:
        verbose_name_plural = "Evaluadores"


