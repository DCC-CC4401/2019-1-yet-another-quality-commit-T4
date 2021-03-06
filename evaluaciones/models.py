from django.db import models

from cursos.models import Curso, Equipo
from rubricas.models import Rubrica
from usuarios.models import Evaluador
from cursos.models import Equipo, Estudiante
import datetime

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
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, default=None)
    evaluadores = models.ManyToManyField(Evaluador)

    def __str__(self):
        return self.nombre

    @property
    def estado(self):
        hoy = datetime.datetime.now()
        default = "0"
        if (str(self.fecha_inicio) <= str(hoy) <= str(self.fecha_fin)):
            default = "1"
        if (str(hoy) > str(self.fecha_fin)):
            default = "0"
        if (str(hoy) < str(self.fecha_inicio)):
            default = "0"
        return default


    class Meta:
        verbose_name_plural = "Evaluaciones"
        unique_together = [['curso', 'nombre']]


class EvaluacionGrupo(models.Model):
    grupo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    presentador = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    fecha = models.DateField()

    def getGrupo(self):
        return self.grupo
    def getPresentador(self):
        return self.presentador
    def getResultados(self):
        return self.resultados
    def getFecha(self):
        return self.fecha

    def __str__(self):
        return self.grupo.nombre


class Resultados(models.Model):
    #evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    #equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    #Directory = models.CharField(default='/evaluaciones/storage/', max_length=60)
    #release_date = models.DateTimeField(default=datetime.now)
    evaluador = models.ForeignKey(Evaluador, on_delete=models.CASCADE)
    puntaje = models.CharField(max_length=100)
    evaluacion_grupo = models.ForeignKey(EvaluacionGrupo, on_delete=models.CASCADE)

    def getEvaluador(self):
        return self.evaluador
    def getPuntaje(self):
        return self.puntaje



