from django import forms

class CrearInformeFormulario(forms.Form):
    fecha = forms.DateField(label = "Fecha de suceso", required = False)
    locacion = forms.CharField(label = "Ubicacion de suceso", max_length = 100)
    tipo_avion = forms.CharField(label = "Tipo de avion", max_length = 100)
    causa_accidente = forms.CharField(label = "Causa Accidente", max_length = 1000)
    descripcion_accidente = forms.CharField(label = "Descripcion Accidente", max_length = 1000)

class CrearAccidenteFormulario(forms.Form):
    crashid = forms.IntegerField()
    fecha = forms.DateField(required = False)
    location = forms.CharField(max_length = 100)
    modelo = forms.CharField(max_length = 100)