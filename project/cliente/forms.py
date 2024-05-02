from django import forms

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "nacimiento": forms.DateInput(attrs={"class": "form-control","type":"date"},format="%d/%m/%Y"),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aquí configuramos el queryset para el campo pais_origen
        self.fields['pais_origen_id'].queryset = models.Pais.objects.all()
