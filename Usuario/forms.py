from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label = "Nombre de usuario(maximo 8 caracteres)", max_length = 8)
    email = forms.EmailField(label = "Email")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class EditarUsuario(UserChangeForm):
    password = None
    first_name = forms.CharField(label = "Primer Nombre", max_length = 15)
    last_name = forms.CharField(label = "Apellido", max_length = 30)
    email = forms.EmailField(label = "Email")
    avatar = forms.ImageField(required = False)
    legajo = forms.IntegerField(label = "Legajo", min_value = 0)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']

