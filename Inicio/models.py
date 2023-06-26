from django.db import models

# Create your models here.

class Gato(models.Model):
    nombre = models.CharField(max_length = 20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null = True)

#Por cada cambio que se haga en los modelos hay que hacer una migracion
#Escribir en consola 'python manage.py makemigrations' y despues escribir 'python manage.py migrate'