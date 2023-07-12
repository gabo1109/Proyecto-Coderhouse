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
    mensaje_contacto = ""
    if request.method == "POST":
        formulario1 = FormularioContacto(request.POST)
        if formulario1.is_valid():
            info1 = formulario1.cleaned_data
            informe1 = Contacto(nombre=info1['nombre'], email=info1['email'], mensaje=info1['mensaje'], telefono=info1['telefono'], fecha=info1['fecha'])
            informe1.save()
            return render(request, 'inicio/mensaje_enviado.html')
    else:
        formulario1 = FormularioContacto()  

    return render(request, 'inicio/contacto.html', {'formulario1': formulario1, 'mensaje': mensaje_contacto})

def mensaje_enviado(request):    
    return render(request, 'inicio/mensaje_enviado.html')   

def about(request):
    return render(request, 'inicio/about.html')

def borrar_informe(request, informe_id):
    informe = Informe.objects.get(id=informe_id)
    informe.delete()
    return redirect('Inicio:buscar_informe')
