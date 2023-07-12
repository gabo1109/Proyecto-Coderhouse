from django.urls import path
from Inicio import views 

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('informe/', views.crear_informe, name='crear_informe'),
    path('busqueda/', views.buscar_informe, name='buscar_informe'),
    path('tabla/', views.tabla_informes, name='tabla_informes'),
    path('contacto/', views.contacto, name='contacto'),
    path('about/', views.about, name='about'),
    path('borrar/<int:informe_id>/', views.borrar_informe, name='borrar'),
    path('modificar/<int:informe_id>/', views.modificar_informe, name='modificar'),
    path('contacto_creado/', views.contacto_creado, name='contacto_creado'),
    path('lista_informes/', views.lista_informes, name='lista_informes')
]