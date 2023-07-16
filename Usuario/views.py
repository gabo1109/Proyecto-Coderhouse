from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as ingreso_web
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuario.forms import FormularioRegistro, EditarUsuario
from django.urls import reverse_lazy

# Create your views here.

def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contraseña = formulario.cleaned_data['password']
            user = authenticate(username = usuario, password = contraseña)
            ingreso_web(request, user)
            return redirect('Inicio:Inicio')
        else:
            return render(request, 'Usuario/login.html', {'formulario': formulario})

    formulario = AuthenticationForm()
    return render(request, 'Usuario/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ('Usuario:login')
        else:
            return render (request, 'Usuario/registro.html', {'formulario': formulario}) 

    formulario = FormularioRegistro()
    return render (request, 'Usuario/registro.html', {'formulario': formulario})   

@login_required
def editar_usuario(request):
    
    if request.method == 'POST':
        formulario = EditarUsuario(request.POST, instance = request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect ('Usuario:usuario_editado')
    else:       
        formulario = EditarUsuario(instance = request.user)

    return render (request, 'Usuario/editar_usuario.html', {'formulario': formulario})

def usuario_editado(request):
    return render (request, 'Usuario/usuario_editado.html')

class EditarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Usuario/editar_contraseña.html'
    success_url = reverse_lazy('Usuario:editar_usuario')