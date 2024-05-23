from django.urls import path

app_name = "cliente"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
    path("cliente/list", views.ClienteList.as_view(), name="cliente_list"),
    path("cliente/create", views.PaisCreate.as_view(), name="pais_create"),
    path("cliente/detail/<int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    path("cliente/update/<int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),

]
