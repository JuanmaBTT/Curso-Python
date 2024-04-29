from django.urls import path
from . import views

app_name = "producto"


urlpatterns = [
    path("", views.home, name="home"),
    path("productocategoria/create", views.productocategoria_create, name="productocategoria_create"),
    path("productocategoria/buscar", views.productocategoria_buscar, name="productocategoria_buscar"),
    path("buscar/", views.buscar),

]
