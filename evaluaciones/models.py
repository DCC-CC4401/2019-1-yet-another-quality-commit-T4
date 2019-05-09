from django.db import models

# Create your models here.
class Integrante(models.Model):
    """Un turbo ejemplo"""
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Evaluador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # TODO: hacer bien esta wea, como tan flaite la contraseña
    contraseña = models.CharField(max_length=2)


    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name_plural = "Evaluadores"