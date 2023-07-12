from django.urls import path
from Inicio import views 

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('informe/', views.crear_informe, name='crear_informe'),
    path('busqueda/', views.buscar_informe, name='buscar_informe'),
    path('tabla/', views.tabla_informes, name='tabla_informes'),
    path('contacto/', views.contacto, name='contacto'),
    path('mensaje_enviado/', views.mensaje_enviado, name='mensaje_enviado'),
    path('about/', views.about, name='about'),
    path('borrar/<int:informe_id>/', views.borrar_informe, name='borrar')
]