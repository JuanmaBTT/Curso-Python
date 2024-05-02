from django.urls import path

app_name = "core"

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('productos/<str:title>/', views.detalle_producto, name='detalle_producto'),
]
