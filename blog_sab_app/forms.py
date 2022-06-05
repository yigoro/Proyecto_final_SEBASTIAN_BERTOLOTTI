import datetime
from django import forms
from django.forms import ModelForm
from blog_sab_app.models import Estudio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudioForm(forms.Form):
    universidad = forms.CharField(max_length=40, label='Universidad')
    anio_inicio = forms.IntegerField(label='Inicio')
    titulo = forms.CharField(max_length=40, label='Titulo')
    finalizado = forms.CharField(max_length=2, label='Finalizado')

class ViajesForm(forms.Form):
    destino = forms.CharField(max_length=40, label='Destino')
    nro_vuelo = forms.IntegerField(label='Vuelo')
    fecha = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    notas = forms.CharField(max_length=200, label='Notas')

class EmpleosForm(forms.Form):
    empresa = forms.CharField(max_length=30, label='Empresa')
    periodo = forms.IntegerField(label='Período')
    puesto = forms.CharField(max_length=40, label='Puesto')

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
