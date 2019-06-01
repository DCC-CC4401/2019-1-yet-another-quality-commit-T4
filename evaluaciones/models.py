from django.db import models
from cursos.models import Curso
from rubricas.models import Rubrica
from datetime import datetime

# Create your models here.

class Integrante(models.Model):
    """Un turbo ejemplo"""
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre1

# Evaluador posee nombre, apellido, email, contraseña y está asociado a un curso
class Evaluador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # TODO: hacer bien esta wea, como tan flaite la contraseña
    contrasenna = models.CharField(max_length=10, default='inseguroxd')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name_plural = "Evaluadores"


# Evaluacion posee curso asociado, estado de evaluación (abierta, cerrada), fecha de inicio y fin, duracin esperada
# de presentacion y rubrica asociada (IMPORTANTE, DEFINIR RUBRICA)
# DEFINIR RUBRICA
class Evaluacion(models.Model):
    nombre = models.CharField(max_length=20)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)
    STATUS_CHOICES = (
        ("0", "Cerrada"),
        ("1", "Abierta"),
    )
    # TODO: como vamos a usar strings con numeros, que flaite
    estado = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, default=None)
    evaluadores = models.ManyToManyField(Evaluador)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Evaluaciones"
        unique_together = [['curso', 'nombre']]
