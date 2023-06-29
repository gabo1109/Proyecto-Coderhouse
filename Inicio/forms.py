from django import forms

class CrearInformeFormulario(forms.Form):
    numero_caso = forms.IntegerField()
    fecha = forms.DateField(label = "Fecha de suceso", required = True)
    locacion = forms.CharField(label = "Ubicacion de suceso", max_length = 100, required = True)
    tipo_avion = forms.CharField(label = "Tipo de avion", max_length = 100, required = True)
    causa_accidente = forms.CharField(label = "Causa Accidente", max_length = 1000, required = True)
    descripcion_accidente = forms.CharField(label = "Descripcion Accidente", max_length = 1000)

class BuscarInformeFormulario(forms.Form):
    numero_caso = forms.IntegerField(label = "Numero de caso", required = False)

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length = 100, required = True)
    email = forms.CharField(label = "Email", max_length = 100, required = True)
    mensaje = forms.CharField(label = "Mensaje", required = True)
    telefono = forms.CharField(label = "Telefono", max_length = 50, required = True)
    fecha = forms.DateTimeField(required = True)