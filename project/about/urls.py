from django.urls import path

app_name = "about"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
    path("about/create", views.AboutCreate.as_view(), name="about_create"),
    path("about/update/<int:pk>", views.AboutUpdate.as_view(), name="about_update"),
    path("about/detail/<int:pk>", views.AboutDetail.as_view(), name="about_detail"),
    path("about/delete/<int:pk>", views.AboutDelete.as_view(), name="about_delete"),
    path("about/list/", views.AboutList.as_view(), name="about_list"),
]
