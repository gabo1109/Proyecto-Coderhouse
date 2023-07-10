from django.shortcuts import render
from Inicio.forms import CrearInformeFormulario, BuscarInformeFormulario
from Inicio.models import Informe

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
            #mensaje = f"Se creo el informe nro {numero_caso}!"
            return render(request, 'inicio/tabla_informes.html')
        else:
            return render(request, 'inicio/crear_informe.html', {'formulario': formulario})

    formulario = CrearInformeFormulario()
    return render(request, 'inicio/crear_informe.html', {'formulario': formulario, 'mensaje': mensaje})

def buscar_informe(request):
    formulario = BuscarInformeFormulario(request.GET)
    if formulario.is_valid():
        numero_caso = formulario.cleaned_data['numero_caso']
    else:
        print("No es valido")
    print(numero_caso)

    return render(request, 'inicio/buscar_informe.html', {'formulario': formulario})


def tabla_informes(request):
    return render(request, 'inicio/tabla_informes.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')  

def about(request):
    return render(request, 'inicio/about.html')  