from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

app_name = "core"

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True), name='redirect-home'),
    path("home/", views.home, name="home"),
    path('categoria/<str:title>/', views.detalle_categoria, name='detalle_categoria'),
    path('productos/<str:title>/', views.detalle_producto, name='detalle_producto'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register")

]

urlpatterns += [
    # Otras URL de la aplicación...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)