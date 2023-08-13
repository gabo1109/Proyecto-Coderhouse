from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    emisor = models.ForeignKey(User, on_delete = models.CASCADE)
    receptor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'receptor')
    mensaje = models.TextField()

    def __str__(self):
        return f"De {self.emisor} para {self.receptor}"