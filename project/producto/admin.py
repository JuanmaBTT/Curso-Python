from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ProductoCategoria)
admin.site.register(models.Producto)
