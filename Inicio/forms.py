from django import forms

class CrearInformeFormulario(forms.Form):
    numero_caso = forms.IntegerField()
    fecha = forms.DateField(label = "Fecha de suceso", required = False)
    locacion = forms.CharField(label = "Ubicacion de suceso", max_length = 100)
    tipo_avion = forms.CharField(label = "Tipo de avion", max_length = 100)
    causa_accidente = forms.CharField(label = "Causa Accidente", max_length = 1000)
    descripcion_accidente = forms.CharField(label = "Descripcion Accidente", max_length = 1000)

class BuscarInformeFormulario(forms.Form):
    numero_caso = forms.IntegerField(label = "Numero de caso")