from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views import View
from .models import ProductoCategoria
from django.http import HttpResponse

from . import forms, models


def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")
    template_name= "producto/productocategoria_create.html"


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaBuscar(View):
    def get(self, request):
        return render(request, 'productocategoria_buscar.html', {'resultados': None})

    def post(self, request):
        palabra_buscar = request.POST.get('palabra_buscar', '')
        resultados = ProductoCategoria.objects.filter(nombre__icontains=palabra_buscar)
        return render(request, 'productocategoria_buscar.html', {'resultados': resultados})
def productocategoria_buscar(request):
    return render(request,"producto/productocategoria_buscar.html", )
def buscar(request):
    if request.GET ['consulta']:
        consulta = request.GET ['consulta']
        resultados = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        context = {"resultados": resultados}
        return render(request,"producto/busqueda.html", context)
    else:
        respuesta = f"No se enviaron datos."
    return HttpResponse(respuesta)