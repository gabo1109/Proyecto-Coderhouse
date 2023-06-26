from django.urls import path
from Inicio import views 

urlpatterns = [
    path('', views.inicio, name='Inicio')
]