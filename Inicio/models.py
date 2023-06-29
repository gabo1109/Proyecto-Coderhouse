from django.db import models

# Create your models here.

class Informe(models.Model):
    numero_caso = models.IntegerField()
    fecha = models.DateField(null = True)
    locacion = models.CharField(max_length = 100)
    tipo_avion = models.CharField(max_length = 100)
    causa_accidente = models.CharField(max_length = 1000)
    descripcion_accidente = models.CharField(max_length = 1000)

class Contacto(models.Model):
    nombre = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    mensaje = models.CharField(max_length = 1000)
    telefono = models.CharField(max_length = 50)
    fecha = models.DateTimeField(null = True)


#Por cada cambio que se haga en los modelos hay que hacer una migracion
#Escribir en consola 'python manage.py makemigrations' y despues escribir 'python manage.py migrate'