from django.shortcuts import render
from Inicio.forms import CrearInformeFormulario, CrearAccidenteFormulario
from Inicio.models import Informe, Accidente

# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_informe(request):
    mensaje = ""
    if request.method == "POST":
        formulario = CrearInformeFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            informe = Informe(fecha = info['fecha'], locacion = info['locacion'], tipo_avion = info['tipo_avion'], causa_accidente = info['causa_accidente'], descripcion_accidente = info['descripcion_accidente'])
            informe.save()
            mensaje = "Se creo el informe!"
        else:
            return render(request, 'inicio/crear_informe.html', {'formulario': formulario})

    formulario = CrearInformeFormulario()
    return render(request, 'inicio/crear_informe.html', {'formulario': formulario, 'mensaje': mensaje})

def buscar_informe(request):
    return render(request, 'inicio/accidente.html')

def accidentes(request):
    mensaje = ""
    if request.method == "POST":
        formulario = CrearAccidenteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            accidente = Accidente(location = info['location'], modelo = info['modelo'], fecha = info['fecha'])
            accidente.save()
            mensaje = f"El accidente fue guardado"
        else:
            return render(request, 'inicio/accidente.html', {'formulario': formulario})

    formulario = CrearAccidenteFormulario()
    return render(request, 'inicio/accidente.html', {'formulario': formulario, 'mensaje': mensaje})
