from django.db import models
from django.contrib.auth.models import User


class Pais(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="país")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "países"


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="país de origen"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.documento} "