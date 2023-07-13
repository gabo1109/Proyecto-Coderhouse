from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as ingreso_web
from Usuario.forms import FormularioRegistro 

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

    formulario = FormularioRegistro
    return render (request, 'Usuario/registro.html', {'formulario': formulario})   