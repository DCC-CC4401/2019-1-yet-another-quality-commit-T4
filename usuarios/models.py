from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Aca deberian estar los modelos de los distintos usuarios que tengamos
from cursos.models import Curso


class Administrador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aca deberian ir mas campos, por ahora esta lo basico

    def __str__(self):
        return self.user.username


class Evaluador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aca deberian ir mas campos, por ahora esta lo basico
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)


    def save(self, *args, **kwargs):
        super(Evaluador, self).save(*args, **kwargs)
        self.user.save()


    def __str__(self):
        return self.nombre + " " + self.apellido


    class Meta:
        verbose_name_plural = "Evaluadores"


