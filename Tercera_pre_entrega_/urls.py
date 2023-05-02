"""Tercera_pre_entrega_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from herencia_HTML.views import index, mostrar_personas, mostrar_vehiculo, mostrar_mascotas, cargar_persona, BuscarPersonas, BuscarVehiculo, cargar_vehiculo, cargar_mascota, BuscarMascota

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('personas/', mostrar_personas, name="personas"),
    path('personas/crear', cargar_persona, name="personas-crear"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    
    path('vehiculos/', mostrar_vehiculo, name="vehiculos"),
    path('vehiculos/crear', cargar_vehiculo, name="vehiculos-crear"),
    path('vehiculos/list', BuscarVehiculo.as_view(), name="vehiculos-list"),

    path('mascotas/', mostrar_mascotas, name="mascotas"),
    path('mascotas/crear', cargar_mascota, name="mascotas-crear"),
    path('mascotas/list', BuscarMascota.as_view(), name="mascotas-list"),
    

]
