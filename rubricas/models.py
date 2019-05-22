from django.db import models
from datetime import datetime
# Create your models here.


# Create your models here.
class Rubrica(models.Model):
    #Relation (nombreRubrica | durationMin | durationMax | path)
    nombre = models.CharField(max_length=200, unique=True)
    durationMin = models.IntegerField(default=0)
    durationMax = models.IntegerField()
    Directory = models.CharField(default='/rubricas/storage/',max_length=60)
    release_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nombre
    def get_name(self):
        return self.nombre
    def get_path(self):
        return self.Directory
    def get_max_duration(self):
        return self.durationMax
    def get_min_duration(self):
        return self.durationMin
