from django.db import models

class About(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
