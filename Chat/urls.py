from django.urls import path
from Chat import views

app_name = 'Chat'

urlpatterns = [
    path('mensajes/', views.lista_mensajes, name='lista_mensajes'),
    path('mensajeenviado/', views.enviar_mensaje, name='enviar_mensaje'),
    path('chat/', views.chat, name='chat')
]