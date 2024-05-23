from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from cliente.models import Cliente, Pais


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico', max_length=50, required=True)
    nombre = forms.CharField(label='Nombre', max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    apellido = forms.CharField(label='Apellido', max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    documento = forms.CharField(label='Documento', max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    nacimiento = forms.DateField(label='Fecha de nacimiento', required=True, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    pais_origen_id = forms.ModelChoiceField(label='País de origen', queryset=Pais.objects.all(), required=True, widget=forms.Select(attrs={"class": "form-control"}))

    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={"class": "form-control"}), help_text='')
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={"class": "form-control"}), help_text='')

    username = forms.CharField(label='Nombre de usuario', max_length=150, help_text='', widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellido']
        user.email = self.cleaned_data['email']
        user.save()
        
        # Crear el cliente relacionado con el usuario
        Cliente.objects.create(
            user=user,            
            nombre=self.cleaned_data["nombre"],
            apellido=self.cleaned_data["apellido"],
            documento=self.cleaned_data["documento"],
            nacimiento=self.cleaned_data["nacimiento"],
            pais_origen_id=self.cleaned_data["pais_origen_id"]
        )
        
        return user