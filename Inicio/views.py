from django.shortcuts import render, redirect
from Inicio.forms import CrearInforme, BuscarInforme, FormularioContacto, ModificarInforme
from Inicio.models import Informe, Contacto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def about(request):
    return render(request, 'inicio/about.html')  

class CrearInforme(CreateView):
    model = Informe
    template_name = 'inicio/CBV/crear_informe_CBV.html'
    fields = ['numero_caso', 'fecha','locacion', 'tipo_avion', 'causa_accidente','descripcion_accidente']
    success_url = reverse_lazy('Inicio:crear_informe')

def buscar_informe(request):
    formulario = BuscarInforme(request.GET)
    informe_encontrado = None
    if formulario.is_valid():
        numero_caso = formulario.cleaned_data['numero_caso']
        informe_encontrado = Informe.objects.filter(numero_caso = numero_caso)
    else:
        print ("Informe no encontrado")

    formulario = BuscarInforme()
    return render(request, 'inicio/buscar_informe.html', {'formulario': formulario, 'informe': informe_encontrado})

def tabla_informes(request):    
    return render(request, 'inicio/tabla_informes.html')

class ListaInformes(ListView):
    model = Informe
    template_name = 'inicio/CBV/lista_informes_CBV.html'
    context_object_name = 'informe'

class BorrarInforme(DeleteView):
    model = Informe
    template_name = 'inicio/CBV/borrar_informe_CBV.html'
    success_url = reverse_lazy('Inicio:lista_informes')

class ModificarInforme(UpdateView):
    model = Informe
    template_name = 'inicio/CBV/modificar_informe_CBV.html'
    fields = ['fecha','locacion', 'tipo_avion', 'causa_accidente','descripcion_accidente']
    success_url = reverse_lazy('Inicio:lista_informes')

class DetalleInforme(DetailView):
    model = Informe
    template_name = 'inicio/CBV/detalle_informe_CBV.html'

class FormularioContacto(CreateView):
    model = Contacto
    template_name = 'inicio/CBV/contacto_CBV.html'
    fields = ['nombre', 'email', 'mensaje', 'telefono','fecha']
    success_url = reverse_lazy('Inicio:crear_informe')

def contacto_creado(request):
    return render(request, 'Inicio/contacto_creado.html')