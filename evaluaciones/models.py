from django.db import models
from cursos.models import Curso, Equipo
from rubricas.models import Rubrica
from usuarios.models import Evaluador
from datetime import datetime

# Create your models here.


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


class Resultados(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Directory = models.CharField(default='/evaluaciones/storage/', max_length=60)
    release_date = models.DateTimeField(default=datetime.now)