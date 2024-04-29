from django import forms

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "nacimiento": forms.DateTimeInput(attrs={"class": "form-control"}),
            "pais_origen_id": forms.TextInput(attrs={"class": "form-control"}),
        }
