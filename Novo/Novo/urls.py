"""
URL configuration for Novo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path
from NovoApp.views import *  # Importa todas las vistas desde la aplicación NovoApp
from django.contrib.auth import views as auth_views
from NovoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('perifericos/', perifericos, name='perifericos'),
    path('laptops/', laptops, name='laptops'),
    path('componentes/', componentes, name='componentes'),
    path('contacto/', contacto, name='contacto'),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('carrito/', cart_view, name='carrito'), 
    path('checkout/', checkout, name='checkout'), # Ruta para el carrito
    path('home/', home_view, name='home'),
    path('logout/',logout_view, name='logout'),  # Ruta para cerrar sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('lockout/', lockout_view, name='lockout'),

    
]
