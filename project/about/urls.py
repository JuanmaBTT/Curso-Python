from django.urls import path

app_name = "about"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
    path("about/create", views.about_create, name="about_create"),

]
