from django.urls import path
from Usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'Usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'Usuario/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar/', views.editar_usuario, name='editar_usuario'),
    path('perfil/editado/', views.usuario_editado, name='usuario_editado'),
    path('perfil/editar/contraseña', views.EditarContraseña.as_view(), name='editar_contraseña')
]