from django.urls import path
from Usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'Usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'Usuario/logout.html'), name='logout')
]