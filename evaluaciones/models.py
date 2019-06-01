from django.db import models
from cursos.models import Curso, Equipo
from datetime import datetime

# Create your models here.

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

class Resultados(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Directory = models.CharField(default='/evaluaciones/storage/', max_length=60)
    release_date = models.DateTimeField(default=datetime.now)