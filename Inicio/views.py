from django.shortcuts import render, redirect
from Inicio.forms import CrearInforme, BuscarInforme, FormularioContacto, ModificarInforme
from Inicio.models import Informe, Contacto

# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_informe(request):
    mensaje = ""
    if request.method == "POST":
        formulario = CrearInforme(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            informe = Informe(numero_caso = info['numero_caso'], fecha = info['fecha'], locacion = info['locacion'], tipo_avion = info['tipo_avion'], causa_accidente = info['causa_accidente'], descripcion_accidente = info['descripcion_accidente'])
            informe.save()
            mensaje = f"Informe {info['numero_caso']} creado correctamente"
        else:
            return render(request, 'inicio/crear_informe.html', {'formulario': formulario})

    formulario = CrearInforme()
    return render(request, 'inicio/crear_informe.html', {'formulario': formulario, 'mensaje':mensaje})

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

def contacto(request):
    formulario = FormularioContacto()
    if request.method == "POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            formulario = Contacto(nombre = info['nombre'], email = info['email'], mensaje = info['mensaje'], telefono = info['telefono'], fecha = info['fecha'])
            formulario.save()
        else:
            return render(request, 'inicio/contacto.html', {'formulario': formulario})

    formulario = FormularioContacto()
    return render(request, 'inicio/contacto.html', {'formulario': formulario})  

def about(request):
    return render(request, 'inicio/about.html')  

def borrar_informe(request, informe_id):
    informe = Informe.objects.get(id=informe_id)
    informe.delete()
    return redirect('Inicio:tabla_informes')

def modificar_informe(request, informe_id):
    informe_modificado = Informe.objects.get(id=informe_id)
    if request.method == 'POST':
        formulario = ModificarInforme(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            informe_modificado.fecha = info['fecha']
            informe_modificado.locacion = info['locacion']
            informe_modificado.tipo_avion = info['tipo_avion']
            informe_modificado.causa_accidente = info['causa_accidente']
            informe_modificado.descripcion_accidente = info['descripcion_accidente']
            informe_modificado.save()
            return redirect('Inicio:tabla_informes')
        else:
            return render(request, 'Inicio/modificar_informe.html', {'formulario':formulario})
    formulario = ModificarInforme
    return render(request, 'Inicio/modificar_informe.html', {'formulario':formulario})
    return redirect('Inicio:tabla_informes')

def contacto_creado(request):
    return render(request, 'Inicio/contacto_creado.html')

def lista_informes(request):
    formulario = BuscarInforme(request.GET)
    informe_encontrado = None
    if formulario.is_valid():
        numero_caso = formulario.cleaned_data['numero_caso']
        informe_encontrado = Informe.objects.all()
    else:
        print ("Error")

    formulario = BuscarInforme()
    return render(request, 'inicio/lista_informes.html', {'formulario': formulario, 'informe': informe_encontrado})
