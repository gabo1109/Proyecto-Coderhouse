from django.db import models

# Create your models here.

class Informe(models.Model):
    fecha = models.DateField(null = True)
    locacion = models.CharField(max_length = 100)
    tipo_avion = models.CharField(max_length = 100)
    causa_accidente = models.CharField(max_length = 1000)
    descripcion_accidente = models.CharField(max_length = 1000)


class Accidente(models.Model):
    crashid = models.IntegerField()
    fecha = models.DateField(null = True)
    location = models.CharField(max_length = 100)
    modelo = models.CharField(max_length = 100)


#Por cada cambio que se haga en los modelos hay que hacer una migracion
#Escribir en consola 'python manage.py makemigrations' y despues escribir 'python manage.py migrate'