from django.shortcuts import render, redirect
from Inicio.forms import CrearInformeFormulario, BuscarInformeFormulario, FormularioContacto
from Inicio.models import Informe, Contacto

# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_informe(request):
    mensaje = ""
    if request.method == "POST":
        formulario = CrearInformeFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            informe = Informe(numero_caso = info['numero_caso'], fecha = info['fecha'], locacion = info['locacion'], tipo_avion = info['tipo_avion'], causa_accidente = info['causa_accidente'], descripcion_accidente = info['descripcion_accidente'])
            informe.save()
            mensaje = f"Informe {info['numero_caso']} creado correctamente"
        else:
            return render(request, 'inicio/crear_informe.html', {'formulario': formulario})

    formulario = CrearInformeFormulario()
    return render(request, 'inicio/crear_informe.html', {'formulario': formulario, 'mensaje': mensaje})

def buscar_informe(request):
    formulario = BuscarInformeFormulario(request.GET)
    informe_encontrado = None
    if formulario.is_valid():
        numero_caso = formulario.cleaned_data['numero_caso']
        informe_encontrado = Informe.objects.filter(numero_caso = numero_caso)
    else:
        print ("Informe no encontrado")

    formulario = BuscarInformeFormulario()
    return render(request, 'inicio/buscar_informe.html', {'formulario': formulario, 'informe': informe_encontrado})

def tabla_informes(request):    
    return render(request, 'inicio/tabla_informes.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')  

def about(request):
    return render(request, 'inicio/about.html')  
