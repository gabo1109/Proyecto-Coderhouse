from django.urls import path
from Inicio import views 

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('informe/', views.crear_informe, name='crear_informe'),
    path('busqueda/', views.buscar_informe, name='buscar_informe'),
    #path('accidente', views.accidentes, name='accidentes')
]