from django.db import models

# Create your models here.
class Rubrica(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    tarea = models.IntegerField()
    anno = models.IntegerField()
    SEMESTER_CHOICES = (
        ("1", "Otoño"),
        ("2", "Primavera"),
        ("3", "Verano"),
    )
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default="2")
    aspecto = models.CharField(max_length=350)
    puntaje = models.FloatField()
    descripcion = models.CharField(max_length=350)
