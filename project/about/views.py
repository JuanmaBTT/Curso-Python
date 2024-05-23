from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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
    consulta_about = models.About.objects.all()
    context = {"about": consulta_about}
    return render(request, "about/index.html", context)

class AboutCreate(CreateView):
    model = models.About
    form_class = forms.AboutForm
    success_url = reverse_lazy("about:home")

class AboutUpdate(UpdateView):
    model = models.About
    form_class = forms.AboutForm
    success_url = reverse_lazy("about:about_list")

class AboutDelete(LoginRequiredMixin, DeleteView):
    model = models.About
    success_url = reverse_lazy("about:about_list")

class AboutList(ListView):
    model = models.About

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.About.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.About.objects.all()
        return object_list

class AboutDetail(DetailView):
    model = models.About