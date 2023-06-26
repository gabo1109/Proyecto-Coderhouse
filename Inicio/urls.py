from django.urls import path
from Inicio import views 

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('gatos/crear/', views.crear_gato, name='crear_gato')
]