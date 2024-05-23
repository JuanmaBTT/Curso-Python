from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.
from . import forms,models


def home(request):
    consulta_clientes = models.Cliente.objects.all()
    context = {"clientes": consulta_clientes}
    return render(request, "cliente/index.html", context)

class ClienteList(ListView):
    model = models.Cliente

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Cliente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cliente.objects.all()
        return object_list
    
class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")

class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")

class PaisCreate(CreateView):
    model = models.Pais
    form_class = forms.PaisForm
    success_url = reverse_lazy("cliente:home")
    template_name= "cliente/pais_create.html"
