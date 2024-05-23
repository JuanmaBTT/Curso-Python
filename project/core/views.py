from . import models
from django.templatetags.static import static
from django.http import HttpRequest,HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from producto.models import Producto, ProductoCategoria


from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    productos = Producto.objects.all()  # Obtener todos los productos (podrías filtrarlos según sea necesario)    
    productos_categoria = ProductoCategoria.objects.all()  # Obtener todos los productos (podrías filtrarlos según sea necesario)    
    context = {'productos': productos, 'productos_categoria': productos_categoria}
    return render(request, "core/index.html", context)

def detalle_producto(request, title):
    producto = get_object_or_404(Producto, nombre__iexact=title)
    return render(request, "core/detalle_mas_info.html", {"producto": producto})
def detalle_categoria(request, title):
    categoria_id = get_object_or_404(ProductoCategoria, nombre__iexact=title)
    productos = Producto.objects.filter(categoria_id=categoria_id)      # Pasa la categoría y los productos filtrados al contexto    
        # Imprimir los productos para depuración
    context = {'productos': productos, 'productos_categoria': categoria_id}    
    return render(request, "core/detalle_categoria.html", context)
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})



