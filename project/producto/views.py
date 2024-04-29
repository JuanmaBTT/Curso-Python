from django.shortcuts import redirect, render

from . import forms,models

from django.http import HttpResponse


def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)

def productocategoria_create(request):
    if request.method == 'POST':
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:home')
    else:
        form = forms.ProductoCategoriaForm()    
    return render(request,"producto/productocategoria_create.html", context={"form": form})

def productocategoria_buscar(request):
    return render(request,"producto/productocategoria_buscar.html", )
def buscar(request):
    if request.GET ['consulta']:
        consulta = request.GET ['consulta']
        return render(request,"producto/busqueda.html")
    else:
        respuesta = f"No se enviaron datos."
    return HttpResponse(respuesta) 