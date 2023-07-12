from django.urls import path
from Usuario import views

app_name = 'Usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
]