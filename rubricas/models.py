from django.db import models

# Create your models here.
class Rubrica(models.Model):
    #Relation (nombre | codigoCurso | tarea | anno | semestre | aspecto | puntaje | contenido)
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
    cont = models.CharField(max_length=350)

    def __str__(self):
        return self.nombre
    def getNombre(self):
        return self.nombre
    def getCodigo(self):
        return self.codigo
    def getTarea(self):
        return self.tarea
    def getAnno(self):
        return self.anno
    def getSemester(self):
        return self.semester
    def getAspecto(self):
        return self.aspecto
    def getPuntaje(self):
        return self.aspecto
    def getCont(self):
        return self.cont


# Create your models here.
class RubricaX(models.Model):
    #Relation (nombre | codigoCurso | tarea | anno | semestre | aspecto | puntaje | contenido)
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
    

    def __str__(self):
        return self.nombre
    def getNombre(self):
        return self.nombre
    def getCodigo(self):
        return self.codigo
    def getTarea(self):
        return self.tarea
    def getAnno(self):
        return self.anno
    def getSemester(self):
        return self.semester
    def getPath(self):
        return self.nombre

    #def getPath(self):
    #    return self.path
    