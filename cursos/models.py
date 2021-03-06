from django.db import models
from usuarios.models import Evaluador, Administrador

# Curso posee nombre, codigo, numero de seccion, año y semetre de realizacion
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    sex_number = models.IntegerField()
    anno = models.IntegerField()
    SEMESTER_CHOICES = (
        (1, "Otoño"),
        (2, "Primavera"),
        (3, "Verano"),
    )
    # TODO: como vamos a usar strings con numeros, que flaite
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default="2")
    equipos = models.ManyToManyField('Equipo')
    evaluadores = models.ManyToManyField(Evaluador)

    class Meta:
        unique_together = (('codigo', 'sex_number', 'anno', 'semester'),)

    # Para obtener el valor de la opcion del semestre, usar get_semester_display()
    def __str__(self):
        return self.nombre + " " + self.codigo + "-" + str(self.sex_number) + " " + str(self.anno) + " " + self.get_semester_display()


class Estudiante(models.Model):
    rut = models.BigIntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " " +self.apellido + " " + str(self.rut)


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    estudiantes = models.ManyToManyField('Estudiante')

    def __str__(self):
        return self.nombre