from django.urls import path
from Inicio import views 

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('busqueda/', views.buscar_informe, name='buscar_informe'),
    path('tabla/', views.tabla_informes, name='tabla_informes'),
    path('about/', views.about, name='about'),
    path('contacto_creado/', views.contacto_creado, name='contacto_creado'),

    #CBV
    path('crear_informe/', views.CrearInforme.as_view(), name='crear_informe'),
    path('lista_informes/', views.ListaInformes.as_view(), name='lista_informes'),
    path('borrar/<int:pk>/', views.BorrarInforme.as_view(), name='borrar'),
    path('modificar/<int:pk>/', views.ModificarInforme.as_view(), name='modificar'),
    path('contacto/', views.FormularioContacto.as_view(), name='contacto'),
    path('<int:pk>/', views.DetalleInforme.as_view(), name='detalle'),
    path('perfil_usuario/', views.PerfilUsuario.as_view(), name='perfil_usuario')
]