from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    nombre_usuario = forms.CharField(label = "Nombre de usuario(maximo 8 caracteres)", max_length = 8)
    email = forms.EmailField(label = "Email")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['nombre_usuario', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}