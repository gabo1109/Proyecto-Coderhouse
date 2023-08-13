from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Chat.models import Chat
from Chat.forms import ChatForm

# Create your views here.

def chat(request):
    return render(request, 'Chat/chat.html')

@login_required
def lista_mensajes(request):
    mensajes = Chat.objects.filter(emisor = request.user) | Chat.objects.filter(receptor = request.user)
    context = {'mensajes': mensajes}
    return render(request, 'Chat/lista_mensajes.html', context)

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit = False)
            mensaje.emisor = request.user
            mensaje.save()
            mensajes = Chat.objects.filter(emisor = request.user) | Chat.objects.filter(receptor=request.user)
            context = {'mensajes': mensajes}
            return render(request, 'Chat/lista_mensajes.html', context)
    else:
        form = ChatForm()
    context = {'form': form}
    return render(request, 'Chat/mensaje_enviado.html', context)