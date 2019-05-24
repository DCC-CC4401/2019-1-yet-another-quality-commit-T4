from django.db import models
from cursos.models import Curso

# Create your models here.

class Integrante(models.Model):
    """Un turbo ejemplo"""
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

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


# Evaluación posee curso asociado, estado de evaluación (abierta, cerrada), fecha de inicio y fin, duración esperada
# de presentación y rúbrica asociada (IMPORTANTE, DEFINIR RUBRICA)
# DEFINIR RUBRICA
class Evaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("0", "Cerrada"),
        ("1", "Abierta"),
    )
    # TODO: como vamos a usar strings con numeros, que flaite
    estado = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    fecha_inicio = models.CharField(max_length=200)
    fecha_fin = models.CharField(max_length=200)
    duracion_pres = models.CharField(max_length=200)